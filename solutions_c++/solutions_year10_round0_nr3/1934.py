// ggc3.cpp : Defines the entry point for the console application.
//
#include "stdafx.h"
  
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <list>
#include <iostream>
#include <string>
#include <vector>
#include <deque>
#include <map>
#include <algorithm>
using namespace std;

#define rep(i,n) for(int i=0; i<n; i++)
#define forr(i,a,b) for (int i=a; i<=b; i++)
#define ford(i,a,b) for (int i=a; i>=b; i--)
#define mset(a,b) memset(a,b,sizeof(a))
#define sz(a) int( a.size() )
#define all(A) A.begin(),A.end()
#define sqr(q) q*q
#define mp(a,b) make_pair(a,b)
#define pb(a) push_back(a)
#define X first
#define Y second

typedef long long i64;
typedef vector<int> VI;
typedef vector< VI > VVI;
typedef pair<int,int> PII;
typedef vector<string> VS;


int k[1200];
PII standing[1200];
int K,R,n;

void form()
{
	int sum=0;
	int t=0;
	while (t<n && sum+k[t]<=K) sum+=k[t++];
	
	t%=n;
	standing[0]=mp(sum,t);

	forr(i,1,n-1)
	{
		sum=standing[i-1].X-k[i-1];
		t=standing[i-1].Y;
		if (t==i) sum+=k[t], t=(t+1)%n;
		while (t!=i && sum+k[t]<=K)
		{
			sum+=k[t];
			t=(t+1)%n;
		}
		standing[i]=mp(sum,t);
	}
}

i64 ans;
int main()
{
	freopen("g3.in","r",stdin);
	freopen("g3.out","w",stdout);
	int tescase;
	scanf("%d",&tescase);

	int test=1;
	while (tescase--)
	{
		scanf("%d %d %d",&R,&K,&n);
		rep(i,n) scanf("%d",&k[i]);

		form();

		ans=0;

		int t=0;
		rep(i,R)
		{
			ans+=i64( standing[t].X );
			t=standing[t].Y;
		}

		printf("Case #%d: ",test); test++;
		cout << ans << endl;
	}



	
	return 0;
}

