// code jam A.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include<stdio.h>
bool on[33],p[33];
int main()
{
	freopen("a.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int test,cas,n,k,i,j;
	scanf("%d",&test);
	for (cas=1;cas<=test;cas++)
	{
		scanf("%d%d",&n,&k);
		for (i=0;i<n;i++) on[i]=p[i]=0;
		p[0]=1;
		for (i=1;i<=k;i++)
		{
			for (j=0;j<n;j++)
			{
				if (p[j]) on[j]=!on[j];
			}
			for (j=1;j<n;j++)
			{
				if (p[j-1]&&on[j-1]) p[j]=1;
				else p[j]=0;
			}
			//for (j=0;j<n;j++) printf("%d %d\n",p[j],on[j]);
		}
		if (p[n-1]&&on[n-1]) printf("Case #%d: ON\n",cas);
		else printf("Case #%d: OFF\n",cas);
	}
	return 0;
}

