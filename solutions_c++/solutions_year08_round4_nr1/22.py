#define SOLVE "A-large"
#include <iostream>
#include <map>
#include <queue>
#include <sstream>
#include <algorithm>
#include <vector>
#include <cassert>
#include <string>
#include <cstdio>
#define dbg(x) cerr << #x << " -> '" << (x) << "'\t"
#define dbge(x) cerr << #x << " -> '" << (x) << "'\n"
#define GI ({int t; scanf("%d",&t);t;})
#define LET(x,a) __typeof(a) x(a)
#define FOR(i,a,b) for(LET(i,a);i!=(b);++i)
#define REP(i,n) FOR(i,0,n)
#define EACH(it,v) FOR(it,(v).begin(), (v).end())
#define sz size()
#define pb push_back
#define cs c_str()
#define INF ((int)(1e8))
using namespace std;

typedef long long LL;
typedef pair<int,int> PII;

#define MM 20000
#define fixed ifixe
bool fixed[MM], isand[MM];
int dp[MM][2], M, V;

int go(int u, int v) {
	if (u > M) return 0;
	if (u > (M-1)/2) return v == fixed[u] ? 0 : INF;
	int &res = dp[u][v];
	if (res == -1) {
		res = INF;
		REP(igate,2) if(!fixed[u] || isand[u] == igate)
		REP(v1,2) REP(v2,2) {
			int vv = igate ? (v1&v2) : (v1|v2);
			if (vv == v) {
				res <?= (igate != isand[u]) + go(2*u, v1) + go(2*u+1, v2);
			}
		}
	}
	return res;
}

int main () {
	assert(freopen (SOLVE ".in", "r", stdin));
	assert(freopen (SOLVE ".out", "w", stdout));
	int kases = GI;
	REP(kase, kases) {
		printf("Case #%d: ", kase+1);
		M = GI, V = GI;
		memset(dp, -1, sizeof(dp));
		FOR(m,1,M+1) {
			if (m <= (M-1)/2) {
				isand[m] = GI;
				fixed[m] = !GI;
			} else {
				fixed[m] = GI;
			}
		}
		int a = go(1,V);
		if (a == INF) puts("IMPOSSIBLE");
		else cout << a << endl;
	}
	return 0;
}
