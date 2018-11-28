#define SOLVE "B-large"
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

#define MM 2001
int N, M;
vector<PII> G[MM];
bool malted[MM];

int main () {
	assert(freopen (SOLVE ".in", "r", stdin));
	assert(freopen (SOLVE ".out", "w", stdout));
	int kases = GI;
	REP(kase, kases) {
		printf("Case #%d: ", kase+1);
		N = GI; M = GI;
		REP(i,N) malted[i] = 0;
		REP(m,M) {
			G[m].clear();
			int T = GI;
			while (T--) {
				int a= GI, b = GI;
				G[m].pb(PII(a-1,b));
			}
		}
		redo:;
			REP(m,M) {
				int idx = -1;
				EACH(v,G[m]) if (malted[v->first] == v->second) goto good; else if(v->second) idx = v->first;
				if (idx == -1) goto imp;
				malted[idx] = 1;
				goto redo;
				good:;
			}
		REP(i,N) printf("%d%c", malted[i], i == N-1 ? '\n':' ');
		
		continue;
		imp: puts("IMPOSSIBLE");
	}
	return 0;
}
