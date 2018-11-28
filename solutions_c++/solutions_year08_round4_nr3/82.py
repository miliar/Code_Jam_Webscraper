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

#define SZ 1011
ld POS[SZ][5];
int N;

ld POW(ld x, ld y, ld z) {
  ld ret = 0;
  REP (i, N) {
    ret = max(ret, (abs(x - POS[i][0]) + abs(y - POS[i][1]) + abs(z - POS[i][2])) / POS[i][3]);
  }
  return ret;
}

int main(int argc, char **argv) {
	COND = argc >= 2 && argv[1][0] == 'q';
	int T;
	cin  >> T;
	FOR (my, 1, T) {
	  DB(my);
	  cin >> N;
	  REP (i, N) {
	    cin >> POS[i][0] >> POS[i][1] >> POS[i][2] >> POS[i][3];
	  }

	  ld POS[3] = {};
	  ld wsp = (ld)1e3;
	  ld ret = POW(POS[0], POS[1], POS[2]);
	  //  DB(ret);
	  //  DB(POW(1.5, 2, 0));
	  while (wsp >= 1e-15) {
	    int cnt = 0;
	    while (++cnt <= 1000) {
	      ld NPOS[3];
	      
	      NPOS[0] = POS[0] + (rand() % 101 - 50) * wsp;
	      NPOS[1] = POS[1] + (rand() % 101 - 50) * wsp;
	      NPOS[2] = POS[2] + (rand() % 101 - 50) * wsp;
	      
	      ld nret = POW(NPOS[0], NPOS[1], NPOS[2]);
	      //	      if (nret <= 10) DB(nret);
	      if (nret < ret) { DB(nret<<" "<<ret);
		ret = nret;
		REP (i, 3) POS[i] = NPOS[i];
		//	DB(POW(NPOS[0], NPOS[1], NPOS[2]));
		//	DB(POW(POS[0], POS[1], POS[2]));
		
		cnt = 0;
	      }
	    }
	    //	    DB(cnt);
	    wsp /= 2;
	  }
	  //	  DB(wsp<<" "<<POS[0]<<" "<<POS[1]<<" "<<POS[2]);
	  //	  DB(POW(POS[0], POS[1], POS[2] - 0.5));
	  printf("Case #%d: %.9lf\n", my, (double)ret);
	}
	return 0;
}
