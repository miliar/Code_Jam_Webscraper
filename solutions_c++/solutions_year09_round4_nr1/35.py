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
#define REP(i,n) for(int i=0;i<(int)(n);++i)
// }}}

/////////////////// CODE WRITTEN DURING THE COMPETITION FOLLOWS ////////////////////////////////

int main() {
  int T;
  cin >> T;
  FOR(t,1,T) {
    int N;
    cin >> N;
    vector<int> last(N,-1);
    REP(n,N) {
      string line;
      cin >> line;
      REP(j,N) if (line[j]=='1') last[n] = j;
    }
    int res = 0;
    REP(j,N-1) {
      int k=j;
      while (last[k] > j) ++k;
      while (k > j) { ++res; swap( last[k], last[k-1] ); --k; }
    }
    cout << "Case #" << t << ": " << res << endl;
  }
  return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
