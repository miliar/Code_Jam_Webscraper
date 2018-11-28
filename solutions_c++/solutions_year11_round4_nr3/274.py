#include<stdio.h>
#include<string>
#include <string.h>
#include<math.h>
#include<utility>
#include<algorithm>
#include<vector>
#include<ctype.h>
#include<map>
#include <iostream>
using namespace std;

#define MAXN 1000010ll
typedef long long ll;
bool isPrime[MAXN];

bool flag[MAXN];

void init()
{
	memset(isPrime,true,sizeof(isPrime));
	int sta=2;
	while(sta<MAXN)
	{
		isPrime[sta]=true;
		for(int i=sta*2;i<MAXN;i+=sta)
			isPrime[i]=false;
		sta++;
		while(sta<MAXN&&!isPrime[sta])
			sta++;
	}
}

ll calcMax(ll N)
{
	if(N==1)return 0;
	ll res=0;
	for(ll i=2;i<=min(MAXN,N);i++)
	{
		if(isPrime[i])
		{
			for(ll j=i*i;j<=N;j*=i)
			{
					res++;
			}
		}
	}
	return res+1;
}

/*
int calcMin(int N)
{
	int res=0;
	for(int i=2;i<=N;i++)
	{
		res+=isPrime[i];
	}
	return res;
}*/


int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	init();
	int t,ct=1;
	scanf("%d",&t);
	
	while(t--)
	{
		ll N;
		scanf("%lld",&N);
		printf("Case #%d: ",ct++);
		printf("%lld\n",calcMax(N));
	}
	return 0;
}
