// another fine solution by misof
// #includes {{{
#include <algorithm>
#include <numeric>

#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <stack>

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cassert>

#include <cmath>
#include <complex>
using namespace std;
// }}}

/////////////////// PRE-WRITTEN CODE FOLLOWS, LOOK DOWN FOR THE SOLUTION ////////////////////////////////

// pre-written code {{{
#define FOR(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define FORD(i,a,b) for(int i=(int)(a);i>=(int)(b);--i)
#define REP(i,n) for(int i=0;i<(int)(n);++i)
// }}}

/////////////////// CODE WRITTEN DURING THE COMPETITION FOLLOWS ////////////////////////////////

long long ZLE = 12345678901234LL;
long long best[12][10000];
int vstup[10000];
int P;

long long solve(int kde, int skipped) {
  if (kde >= (1<<P)) {
    // terminal node
    if (skipped <= vstup[kde]) return 0;
    return ZLE;
  } else {
    long long &res = best[skipped][kde];
    if (res < ZLE) return res;
    long long case1 = solve(2*kde,skipped+1) + solve(2*kde+1,skipped+1);
    long long case2 = vstup[kde] + solve(2*kde,skipped) + solve(2*kde+1,skipped);
    res = min( case1, case2 );
    return res;
  }
}

int main() {
  int T;
  cin >> T;
  FOR(t,1,T) {
    cin >> P;
    FORD(p,P,0) REP(i,1<<p) cin >> vstup[ (1<<p) + i ];
    // for (int i=1; i<(1<<(P+1)); ++i) cout << vstup[i] << " "; cout << endl;
    memset(best,0x3f,sizeof(best));
    cout << "Case #" << t << ": " << solve(1,0) << endl;
  }
  return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
