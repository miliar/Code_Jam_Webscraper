//#include "stdafx.h"
#include "iostream"
using namespace std;

int findmax(int,int);

int main()
{
	freopen("test.in","r",stdin);
	freopen("test.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		int N,S,p, n[100+1];
		scanf("%d%d%d",&N,&S,&p);
		for(int i=0;i<N;i++)scanf("%d",&n[i]);
		int ret1=0, ret2=0, vis[100+1]={0};

		for(int i=0;i<N;i++)
		{
			int maxn=findmax(n[i],1);
			if(maxn>=p){ret1++;vis[i]=1;}
		}
		for(int i=0;i<N;i++)if(vis[i]==0)
		{
			int maxn=findmax(n[i],2);
			if(maxn>=p){ret2++;vis[i]=1;}
		}
		printf("%s%d%s%d\n", "Case #",t ,": ",ret1+(ret2>S?S:ret2));

	}
	return 0;
}

int findmax(int sum, int type)
{
	if(type==1)
	{
		if((sum+2)%3==0&&(sum+2)/3>=1)return (sum+2)/3;
		if((sum+1)%3==0&&(sum+1)/3>=1)return (sum+1)/3;
		if((sum)%3==0&&(sum)/3>=0)return (sum)/3;

	}
	else if(type==2)
	{
		if((sum+4)%3==0&&(sum+4)/3>=2)return (sum+4)/3;
		if((sum+2)%3==0&&(sum+2)/3>=2)return (sum+2)/3;
		if((sum+3)%3==0&&(sum+3)/3>=2)return (sum+3)/3;
	}
	return -1;
}