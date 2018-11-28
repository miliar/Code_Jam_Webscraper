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
#define FORALL(it,x) for (typeof(x.begin()) it=x.begin(); it!=x.end(); it++)

typedef vector <int> VI;
typedef vector <VI> VVI;
typedef long long LL;
typedef vector<LL> VLL;
typedef vector<VLL> VVLL;
typedef vector<double> VD;
typedef vector<VD> VVD;
typedef vector <string> VS;

const LL MOD = 10007;

void solve () {
  int X,Y,P;
  scanf ("%i %i %i",&Y,&X,&P);

  VVI forb(Y, VI(X, 0));
  VVLL cnt(Y, VLL(X, 0));

  REP(i,P) {
    int y,x;
    scanf ("%i %i",&y,&x);
    forb[y-1][x-1]=1;
  }

  cnt[0][0]=1;
  REP(y,Y) REP(x,X) if (!forb[y][x]) {
    if (y>=2 && x>=1) cnt[y][x] = (cnt[y][x]+cnt[y-2][x-1]) % MOD;
    if (x>=2 && y>=1) cnt[y][x] = (cnt[y][x]+cnt[y-1][x-2]) % MOD;
  }

  printf ("%lli",cnt[Y-1][X-1]);
}

int main () {

  int runs;
  scanf ("%i\n",&runs);

  for (int run=1; run<=runs; run++) {
    printf ("Case #%i: ",run);
    solve();
    printf ("\n");
  }

  return 0;
}
