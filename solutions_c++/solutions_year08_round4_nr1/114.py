#include <cstdio>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <numeric>
#include <cmath>
#include <cstdlib>
#include <iostream>
using namespace std;

#define VV vector
#define X first
#define Y second
#define MP make_pair
#define PB push_back
typedef long long ll;
typedef double D;
typedef long double ld;
typedef vector<int> VI;
typedef pair<int,int> PII;
#define REP(i,n) for(int i=0;i<(n);i++)
#define FOR(i,a,b) for(VAR(i,a);i<=(b);++i)
#define FORD(i,a,b) for(VAR(i,a);i>=(b);--i)
#define FORE(a,b) for(VAR(a,(b).begin());a!=(b).end();++a)
#define VAR(a,b) __typeof(b) a=(b)
#define SIZE(a) ((int)((a).size()))
#define ALL(x) (x).begin(),(x).end()
#define CLR(x,a) memset(x,a,sizeof(x))

int COND = 0;

#define DB(x) { if (COND) { cerr << __LINE__ << " " << #x << " " << x << endl; } }


#define SZ ((int)1e4 + 111)

int VAL[SZ];
int COST[SZ][2];
int F, L;

int TYPE[SZ][2];
#define INF 0x3f3f3f3f

int main(int argc, char **argv) {
	COND = argc >= 2 && argv[1][0] == 'q';
	int C;
	cin >> C;
	FOR (my, 1, C) {
	  CLR(COST, 0x3f);

	  int M, V; 
	  cin >> M >> V;;
	  F = (M - 1) / 2;
	  L = (M + 1) / 2;
	  REP (i, F) cin >> TYPE[i][0] >> TYPE[i][1];
	  REP (i, L) {
	    int x; cin >> x;
	    COST[F + i][x] = 0;
	  }
	  FORD (i, F - 1, 0) {
	    if (TYPE[i][0] == 0) {
	      REP (a, 2) REP (b, 2)
		COST[i][a || b] = min(COST[i][a || b], COST[2 * i + 1][a] + COST[2 * i + 2][b]);
	    }
	    else {
	      REP (a, 2) REP (b, 2)
		COST[i][a && b] = min(COST[i][a && b], COST[2 * i + 1][a] + COST[2 * i + 2][b]);
	    }

	    if (TYPE[i][1]) {
	      REP (a, 2) REP (b, 2)
		COST[i][a || b] = min(COST[i][a || b], 1 + COST[2 * i + 1][a] + COST[2 * i + 2][b]);

	      REP (a, 2) REP (b, 2)
		COST[i][a && b] = min(COST[i][a && b], 1 + COST[2 * i + 1][a] + COST[2 * i + 2][b]);
	    }

	    // 0 OR
	    

	    // 1 AND
	    DB(i<<" "<<COST[i][0]<<" "<<COST[i][1]);
	  }

	  if (COST[0][V] == INF) cout << "Case #" << my << ": IMPOSSIBLE" << endl;
	  else {
	    cout << "Case #" << my << ": " << COST[0][V] << endl;
	  }


	}
	

	return 0;
}
