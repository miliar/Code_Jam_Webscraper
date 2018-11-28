using namespace std;
 
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <ctype.h>
#include <string.h>
#include <string>
#include <sstream>
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <functional>
 
#define PB push_back
#define SZ size()
#define REP(v, hi) for (int v=0; v<(hi); v++)
#define REPD(v, hi) for (int v=((hi)-1); v>=0; v--)
#define FOR(v, lo, hi) for (int v=(lo); v<(hi); v++)
#define FORD(v, lo, hi) for (int v=((hi)-1); v>=(lo); v--)
 
typedef vector <int> VI;
typedef vector <VI> VVI;
typedef long long LL;
typedef vector<LL> VLL;
typedef vector<VLL> VVLL;
typedef vector<double> VD;
typedef vector<VD> VVD;
typedef vector <string> VS;
 
int main () {

  int runs;
  scanf ("%i\n",&runs);

  for (int run=1; run<=runs; run++) {

    int N; scanf ("%i",&N);
    
    VD p(N);
    VVD x(N,VD(3));
    REP(i,N) scanf ("%lf %lf %lf %lf",&x[i][0],&x[i][1],&x[i][2],&p[i]);
        
    double lo=0, hi=1e7;

    REP(times,100) {
      double P = (lo+hi)/2;

      VD bound(1<<3,1e9);
      REP(msk,1<<3) REP(i,N) {
	double tmp = P*p[i];
	REP(j,3) if (msk&(1<<j)) tmp+=x[i][j]; else tmp-=x[i][j];
	bound[msk] <?= tmp;
      }

      int ok=1;
      REP(msk,1<<3) if (-bound[(1<<3)-1-msk] > bound[msk]) ok=0;

      if (ok) hi=P; else lo=P;
    }
    
    printf ("Case #%i: %.9lf\n",run, lo);
  }

  return 0;
}
