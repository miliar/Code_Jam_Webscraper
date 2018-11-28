#include <string.h>
#include <stdio.h>
#include <iostream>
#include <algorithm>
using namespace std;
#define maxn 1000009
#define LL long long
int f[maxn],g[maxn];
void init()
{
	memset(f,0,sizeof(f));
	f[1]=1;
	f[2]=2;
	for(int i=1;i<=1000000;i++)
	{
		g[i]=f[i]+i-1;
		for(int j=g[i];;j--)
		{
			if(f[j])
				break;
			f[j]=i;
		}
	}
	/*
	for(int i=1;i<=6;i++)
	{
		printf("%d %d\n",f[i],g[i]);
	}*/
}
int main()
{
	init();
	int Q,A1,A2,B1,B2;
	scanf("%d",&Q);
	for(int t=1;t<=Q;t++)
	{
		scanf("%d%d%d%d",&A1,&A2,&B1,&B2);
		LL sum=(LL)(A2-A1+1)*(B2-B1+1);
		int lf,rt;
		for(int i=A1;i<=A2;i++)
		{
			lf=max(f[i],B1);
			rt=min(g[i],B2);
			if(lf<=rt)
				sum-=(rt-lf+1);
		}
		printf("Case #%d: %I64d\n",t,sum);
	}
	return 0;
}
