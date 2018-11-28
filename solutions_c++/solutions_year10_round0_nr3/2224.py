// code jam C.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include<stdio.h>
long long par[1003],next[1003],arr[1003],pos[1003],ans[10003];

int main()
{
	freopen("c.txt","r",stdin);
	freopen("out.txt","w",stdout);
	long long test,cas,r,k,n,i,j,p,sum,q,len;
	scanf("%lld",&test);
	for (cas=1;cas<=test;cas++)
	{
		scanf("%lld%lld%lld",&r,&k,&n);
		for (i=0;i<n;i++) scanf("%lld",&arr[i]);
		for (i=0;i<n;i++)
		{
			pos[i]=-1;
			par[i]=0;
			for (j=i;;)
			{
				if (par[i]+arr[j]<=k)
				{
					par[i]+=arr[j];
				}
				else
				{
					next[i]=j;
					break;
				}
				j=(j+1)%n;
				if (j==i)
				{
					next[i]=j;
					break;
				}
			}
		}
		p=sum=ans[0]=0;
		for (i=1;i<=r;i++)
		{
			if (pos[p]==-1)
			{
				pos[p]=i;
				sum+=par[p];
				ans[i]=sum;
				p=next[p];
			}
			else
			{
				q=sum-ans[pos[p]-1];
				sum=ans[pos[p]-1];
				len=i-pos[p];
				r=r-pos[p];
				//printf("%lld\n",r);
				sum+=(r/len)*q+ans[pos[p]+r%len]-ans[pos[p]-1];
				break;
			}
		}
		printf("Case #%lld: %lld\n",cas,sum);
	}
	return 0;
}

