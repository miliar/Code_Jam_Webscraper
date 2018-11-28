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

int dp[105][105];
vector<int> mas;
int P;

int go(int pos,int ost)
{
	if (pos==0)
		return 0;
	if (ost==-1)
		return -10000;
	if (dp[pos][ost]!=-1)
		return dp[pos][ost];
	int res=0;
	if (3*P-2<=mas[pos])
		res=max(res,go(pos-1,ost)+1);
	if (ost && 3*P-4<=mas[pos] && mas[pos]>=2 && mas[pos]<=28)
		res=max(res,go(pos-1,ost-1)+1);
	res=max(res,go(pos-1,ost));
	return dp[pos][ost]=res;
}

void solve()
{
	int test=ri();
	fr(testing,1,test)
	{
		int n=ri(),s=ri();P=ri();
		memset(dp,-1,sizeof(dp));
		mas.clear();
		mas.resize(n+1);
		fr(i,1,n)
			mas[i]=ri();
		printf("Case #%d: ",testing);
		cout << go(n,s) << endl;
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

	//#ifndef ONLINE_JUDGE
	//	printf("\n\ntime-%.3lf",clock()*1e-3);
	//#endif

	return 0;
}