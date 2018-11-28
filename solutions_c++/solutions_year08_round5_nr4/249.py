#include <cstdio>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>
#include <map>
#include <set>
#include <cctype>
#include <iostream>
#include <cassert>
#include <numeric>

using namespace std;

typedef vector<int> VI;
typedef vector<string> VS;
typedef long long LL;

#define ALL(a) (a).begin(),(a).end()
#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define CLR(v,a) memset(v,a,sizeof(v))
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
#define MOD 10007

int t, n, m, r;
int tab[101][101], dp[101][101];
int dx[2]={1,2};
int dy[2]={2,1};

int main()
{
	scanf("%d", &t);
	FOR(tCase,1,t) {
		scanf("%d %d %d", &n, &m, &r);
		CLR(tab,0); REP(i,r) { int x,y; scanf("%d %d", &x, &y); tab[x-1][y-1]=1; }
		CLR(dp,0); dp[0][0]=1;
		REP(i,n) REP(j,m) REP(k,2) {
			int ni=i+dx[k], nj=j+dy[k];
			if (ni<n&&nj<m&&tab[ni][nj]==0)
				dp[ni][nj]=(dp[ni][nj]+dp[i][j])%MOD;
		}
		printf("Case #%d: %d\n", tCase, dp[n-1][m-1]);
	}
	return 0;
}
