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
#define CLEAR(t) memset((t),0,sizeof(t))
#define FOR(i,a,b) for(int i=(int)(a);i<=(int)(b);++i)
#define REP(i,n) for(int i=0;i<(int)(n);++i)
// }}}

/////////////////// CODE WRITTEN DURING THE COMPETITION FOLLOWS ////////////////////////////////

int A[480][480], B[480][480];

bool step() {
  bool one = false;
  FOR(x,1,470) FOR(y,1,470) {
    if (A[x][y]) {
      if (!A[x-1][y] && !A[x][y-1]) B[x][y]=0; else B[x][y]=1, one=true;
    } else {
      if (A[x-1][y] && A[x][y-1]) B[x][y]=1, one=true; else B[x][y]=0;
    }
  }
  return one;
}

int main() {
  int T;
  cin >> T;
  FOR(t,1,T) {
    int R;
    cin >> R;
    CLEAR(A);
    REP(r,R) {
      int x1, y1, x2, y2;
      cin >> x1 >> y1 >> x2 >> y2;
      FOR(x,x1,x2) FOR(y,y1,y2) A[x][y] = 1;
    }
    for (int steps=1; ; ++steps) {
      if (!step()) {
        cout << "Case #" << t << ": " << steps << endl;
        break;
      }
      memcpy(A,B,sizeof(A));
    }
  }
  return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
