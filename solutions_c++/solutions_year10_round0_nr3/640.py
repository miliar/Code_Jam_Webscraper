#include<stdio.h>
#include<iostream>
using namespace std;
int da[1010];
long long lp[1010];
long long js[1010];
long long ans;
int main()
{
	freopen("c.in","r",stdin);
	freopen("zc.out","w",stdout);
	long long z,i,j,k,r,n;
	scanf("%I64d",&z);
	for(long long y=1;y<=z;y++)
	{
		scanf("%I64d%I64d%I64d",&r,&k,&n);
		for(i=0;i<n;i++)
			scanf("%I64d",da+i);
		for(i=0;i<n;i++)
		{
			js[i]=da[i];
			for(j=i+1;;j++)
			{
				if(j%n==i || js[i]+da[j%n]>k)
					break;
				js[i]+=da[j%n];
			}
			lp[i]=j%n;
			//cout<<i<<" "<<js[i]<<" "<<lp[i]<<endl;
		}
		ans=0;
		j=0;
		while(r--)
		{
			ans+=js[j];
			j=lp[j];
		}
		printf("Case #%I64d: %I64d\n",y,ans);
	}
	return 0;
}
