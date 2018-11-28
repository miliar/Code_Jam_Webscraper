#include <cstdio>
#include <iostream>
#include <string>
#include <algorithm>
#include <cmath>
#include <vector>
#include <stack>
#include <queue>
#include <list>
#include <map>
#include <set>
#include <stdlib.h>
#include <sstream>
#include <assert.h>

#include <time.h>
#pragma comment(linker, "/STACK:20000000")

#define fr(i,a,b) for(int i=(int)(a);i<=(int)(b);i++)
#define fd(i,a,b) for(int i=(int)(a);i>=(int)(b);i--)
#define mp make_pair
#define pb push_back
#define ll long long

using namespace std;

int ri(){int x;scanf("%d",&x);return x;}
ll rll(){ll x;scanf("%lld",&x);return x;}

const int MAXN=1e4+10;

pair<ll,ll> mas[MAXN];
double dp[MAXN];

#define sqr(x) (x)*(x)

double check(int v2,double x)
{
	double xx=mas[v2].first-x;
	return sqr(mas[v2].second)-sqr(xx)>=1e-9;
}

double get(int v1,int v2)
{
	double dist=(double)mas[v2].first-mas[v1].first;
	double LEFT=mas[v1].first,RIGHT=mas[v2].first;
	fr(i,1,50)
	{
		double MID=LEFT+RIGHT;
		MID/=2;
		if (check(v2,MID))
			RIGHT=MID;
		else
			LEFT=MID;
	}
	double k2=(double)mas[v2].first-RIGHT;
	double k3=(double)mas[v2].second;
	if (k3>=dist)
		k3=dist;
	return sqrt(sqr(k3)+sqr(k2));
}

void solve()
{
	int test=ri();
	fr(testing,1,test)
	{
		int n=ri();
		fr(i,1,n)
			mas[i].first=rll(),mas[i].second=rll();
		memset(dp,0,sizeof(dp));
		ll finish=rll();
		dp[1]=mas[1].first;
		fr(i,1,n)
		{
			if (!dp[i])
				continue;
			fr(j,i+1,n)
			{
				if (mas[i].first+dp[i]/*mas[i].second*/>=mas[j].first)
				{
					double pf=get(i,j);
					dp[j]=max(dp[j],min(pf,(double)mas[j].second));
				}
				else
					break;
			}
		}
		bool yes=false;
		fr(i,1,n)
			if (dp[i] && (double)mas[i].first+dp[i]+1e-10>=(double)finish)
				yes=true;
		printf("Case #%d: %s\n",testing, yes ? "YES" : "NO" );
	}
	
}

int main()
{
	#ifndef ONLINE_JUDGE
		freopen("C:/Users/CleRIC/Desktop/Универ/acm.timus.ru/input.txt","rt",stdin);
		freopen("C:/Users/CleRIC/Desktop/Универ/acm.timus.ru/output.txt","wt",stdout);
	#else
		//freopen("input.in","rt",stdin);
		//freopen("output.out","wt",stdout);
	#endif

	solve();

	#ifndef ONLINE_JUDGE
		printf("\n\ntime-%.3lf",clock()*1e-3);
	#endif

	return 0;
}