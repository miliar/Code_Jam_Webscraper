#include<cstdio>
#include<iostream>
using namespace std;

unsigned int ans[10002];

int main()
{
	unsigned int T,N,K;
	unsigned int numberbase;
	unsigned int caseNum=1,pos=1;
	scanf("%d",&T);
	for(int i=1;i<=T;i++)
	{
		scanf("%d%d",&N,&K);
		numberbase=1;
		while(N--)
		{
			numberbase*=2;
		}
		if(K==0)
		{
			ans[pos++]=0;
			continue;
		}
		if((K+1)%numberbase==0)
		{
			ans[pos++]=1;
		}
		else
		{
			ans[pos++]=0;
		}
	}
	for(int i=1;i<=T;i++)
	{
		if(ans[i]==1)
			printf("Case #%d: ON\n",i);
		else
			printf("Case #%d: OFF\n",i);
	}
	return 0;
}