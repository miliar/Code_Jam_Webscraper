using namespace std;
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <list>
#include <set>
#include <algorithm>
#include <utility>
#include <functional>
#include <numeric>
#include <math.h>
#include <string.h>
#include <ctype.h>
#include <stdio.h>

typedef long long LL;
typedef vector<LL> VI;
typedef vector<VI> VVI;
typedef vector<VVI> VVVI;
typedef vector<string> VS;
typedef istringstream ISS;

#define PB push_back
#define ALL(x) ((x).begin()),((x).end())
#define FOR(i,c) for(typeof(c.begin()) i=c.begin(); i!=c.end(); ++i)
#define REP(i,n) for(int i=0; i<(n); ++i)

const int infty = 999999999;

#define DEBUGGING 1

#if defined(DEBUGGING)
#define debug(...) printf(__VA_ARGS__)
#else
#define debug(...)
#endif

int P;
VI miss;
VVI cost;
VVVI best;

int main()
{
	int nruns;
	cin >> nruns;

	for(int run=1; run<=nruns; run++) {

		cin >> P;
		miss = VI(1<<P);
		cost = VVI(P);
		REP(i,1<<P) cin >> miss[i];
		REP(i,P) {
			int n = 1<<(P-i-1);
			cost[i] = VI(n);
			REP(j,n) cin >> cost[i][j];
		}

		best = VVVI(P+1);
		REP(i,P+1) best[i] = VVI(1<<(P-i),VI(P+1,infty));

		REP(i,1<<P) best[0][i][miss[i]] = 0;

		for(int i=1; i<=P; i++) {
//			debug("i = %d\n",i);
			REP(j,1<<(P-i)) {
				REP(m1,P+1) REP(m2,P+1) {
					int m = min(m1,m2);
					best[i][j][m] <?= best[i-1][2*j][m1] + best[i-1][2*j+1][m2] + cost[i-1][j];
					if ( m>0 )
						best[i][j][m-1] <?= best[i-1][2*j][m1] + best[i-1][2*j+1][m2];
				}
			}
		}

		long long res = infty;
		REP(m,P+1) res <?= best[P][0][m];
		printf("Case #%d: %lld\n",run,res);
	}

	return 0;
}
