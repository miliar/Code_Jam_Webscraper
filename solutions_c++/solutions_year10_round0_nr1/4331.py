#include <cstdio>
#include <iostream>
#include <map>
using namespace std;

map< pair<long long,long long>,bool >dpmap;

bool dp(long long n,long long k)
{
	if(k==0)return 0;
	if(n==0)return 1;
	if(k==1)return (n==1);
	pair<long long,long long>tmp;
	tmp=make_pair(n,k);
	if(dpmap.count(tmp))return dpmap[tmp];
	dpmap[tmp]=dp(n,k-1)^dp(n-1,k-1);
	return dpmap[tmp];
}

bool brute(long long n,long long k)
{
	bool s[40]={1,0},p[40]={1,0};
	for(long long i=0;i<k;i++)
	{
		for(int j=1;j<=n;j++)
		{
			if(p[j-1])
			{
				s[j]=!s[j];
			}
		}
		for(int j=1;j<=n;j++)
		{
			p[j]=s[j]&p[j-1];
		}
	}
	return p[n];
}

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	long long T,N,K;
	scanf("%lld",&T);
		for(long long t=1;t<=T;t++)
		{
			scanf("%lld%lld",&N,&K);
			//bool flag=dp(N,K);
			bool flag2=brute(N,K);
			//if(flag!=flag2)printf("Case #%lld: ERROR\n",t);
			if(flag2)printf("Case #%lld: ON\n",t);
			else printf("Case #%lld: OFF\n",t);
		}
	return 0;
}
