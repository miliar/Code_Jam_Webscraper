#include<string>
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<fstream>
using namespace std;
int N,S,P,T;
int data[5000];
void solve(int num)
{
	int Ans=0;
	for(int i=1;i<=N;i++)
	{
		int now=data[i];
		if(now%3==0)
		{
			int a=now/3;
			if(a>=P)
			Ans++;
			else if(a==P-1&&S>0&&a-1>=0)
			S--,Ans++;
		}
		else if(now%3==1)
		{
			int a=now/3;
			if(a+1>=P)
			Ans++;
		}
		else if(now%3==2)
		{
			int a=now/3;
			if(a+1>=P)
			Ans++;
			else if(a+1==P-1&&S>0)
			S--,Ans++;
		}
	}
	printf("Case #%d: %d\n",num,Ans);
}
int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&T);
	for(int tt=1;tt<=T;tt++)
	{
		scanf("%d%d%d",&N,&S,&P);
		for(int i=1;i<=N;i++)
		scanf("%d",&data[i]);
		solve(tt);
	}
	return 0;
}