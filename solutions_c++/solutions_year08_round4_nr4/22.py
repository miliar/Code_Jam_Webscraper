#define SOLVE "D-large"

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
const int MN = (1 << 20), MK = 16;
int K; string S;
int IncTab[MK][MK], Tab[MK][MK];
int dp[1 << MK][MK][MK];
int go(int f, int u, int first) {
	if(1+f == (1<<K)) return IncTab[first][u];
	int &res = dp[f][u][first];
	if (res == -1) {	
		res = INF;
		REP(v, MK) if (!(f& (1<<v))) res <?= Tab[u][v] + go(f|(1<<v), v, first);
	}
	return res;
}

int main () {
	assert(freopen (SOLVE ".in", "r", stdin));
	assert(freopen (SOLVE ".out", "w", stdout));
	int kases = GI;
	REP(kase, kases) {
		printf("Case #%d: ", kase+1);
		K = GI; cin >> S; assert(S.sz%K == 0);
		memset(IncTab, 0, sizeof(IncTab));
		memset(Tab, 0, sizeof(Tab));
		REP(p1,K) REP(p2,K) if(p1!=p2) {
			REP(b, S.sz/K) {
				if(b) IncTab[p1][p2] += S[(b-1)*K+p2] != S[b*K+p1];
				Tab[p1][p2] += S[b*K+p1] != S[b*K+p2];
			}
		}
		memset(dp,-1,sizeof(dp));
		int res = INF; REP(p1,K) res <?= 1 + go(1 << p1, p1, p1);
		cout << res << endl;
	}
	return 0;
}
