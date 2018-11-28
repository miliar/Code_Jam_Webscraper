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

    int X,Y,A;
    scanf ("%i %i %i",&X,&Y,&A);

    FOR(x1,0,X+1) FOR(x2,0,X+1) FOR(y1,0,Y+1) FOR(y2,0,Y+1) {
      if (abs(x1*y2-x2*y1) == A) {
	printf ("Case #%i: 0 0 %i %i %i %i\n",run,x1,y1,x2,y2);
	goto next;
      }
    }

    printf ("Case #%i: IMPOSSIBLE\n",run);
  next:
    ;
  }

  return 0;
}
