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
#include <sstream>
using namespace std;

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

struct event {
  int PR[2];
  int peron;
  bool operator < (const event &rhs) const {
    return PR[0] < rhs.PR[0];
  }
};

#define SZ 2400

event EV[SZ];

int main(int argc, char **argv) {
  COND = argc >= 2 && argv[1][0] == 'q';
  ios::sync_with_stdio(false);
  int N;

  cin >> N;
  FOR (mycase, 1, N) {
    int T, NA, NB;
    cin >> T >> NA >> NB;
    
    int RET[2] = {0, 0};
    int LOC[SZ][2] = {};
    int SIZE[2] = {NA, NB};
    DB(T<<" "<<NA<<" "<<NB);
    int id = 0;
    REP (G, 2) {
      REP (ii, SIZE[G]) { 
	REP (j, 2) {
	  string tmp; cin >> tmp;
	  stringstream ss(tmp);
	  int h, m; char cc;
	  ss >> h >> cc >> m;
	  EV[id].PR[j] = h * 60 + m;
	}
	EV[id].peron = G;
	id++;
      }
    }
    sort(EV, EV + NA + NB);
    int K = NA + NB;
    int CNT[2] = {};
    REP (tim, SZ) {
      REP (pr, 2)
	CNT[pr] += LOC[tim][pr];

      REP (i, K) if (EV[i].PR[0] == tim) {
	int pr = EV[i].peron;
	CNT[pr]--;
	if (CNT[pr] < 0) CNT[pr]++, RET[pr]++;
	LOC[EV[i].PR[1] + T][1-pr]++;
      }
    }
    printf("Case #%d: %d %d\n", mycase, RET[0], RET[1]);
  }


  return 0;
}
