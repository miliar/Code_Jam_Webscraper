#define SOLVE "C-large"
#include <iostream>
#define CLS(x) memset(x,0,sizeof(x))
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
typedef long double ld;
#include <cmath>
#define X xxx
#define MN 1024
int n;
ld X[MN][3], P[MN];

struct Cube {
	ld C[4][2];
	void intersect(Cube b) {
		REP(c,4) {
			C[c][0] >?= b.C[c][0];
			C[c][1] <?= b.C[c][1];
		}
	}
	bool good() {
		REP(c,4) if (C[c][0] > C[c][1]) return 0;
		return 1;
	}
};

int main () {
	assert(freopen (SOLVE ".in", "r", stdin));
	assert(freopen (SOLVE ".out", "w", stdout));
	int kases = GI;
	REP(kase, kases) {
		printf("Case #%d: ", kase+1);
		n = GI; REP(i,n) cin >> X[i][0] >> X[i][1] >> X[i][2] >> P[i];
		ld ans, lo = 0, hi = 1e12;
		REP(repeat, 500) {
			ans = (lo + hi)/2;
			Cube cur, nc; REP(c,4) cur.C[c][0] = -1e100, cur.C[c][1] = +1e100;
			REP(i,n) {
				REP(f,4) {
					ld now = 0;
					REP(ii,3) if(f&(1<<ii)) now += X[i][ii]; else now -= X[i][ii];
					nc.C[f][0] = now - P[i]*ans;
					nc.C[f][1] = now + P[i]*ans;
				}
				cur.intersect(nc);
			}
			//dbg(ans); dbge(cur.good());
			if(cur.good()) hi = ans; else lo = ans;
		}
		printf("%.12lf\n", (double)ans);
	}
	return 0;
}
