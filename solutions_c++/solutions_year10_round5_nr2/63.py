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
#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define SIZE(t) ((int)((t).size()))
// }}}

/////////////////// CODE WRITTEN DURING THE COMPETITION FOLLOWS ////////////////////////////////

int B[128];

int main() {
  int T;
  cin >> T;
  FOR(t,1,T) {
    vector<int> minLogs(100000,1987654321);
    minLogs[0] = 0;
    int S = SIZE(minLogs);

    long long L;
    int N;
    cin >> L >> N;

    REP(n,N) cin >> B[n];
    sort( B, B+N );

    int goodSteps = 0;
    int kde = 0;
    while (1) {
      ++kde;
      if (kde == S) {
        minLogs.resize( S + 100000, 1987654321 );
        S += 100000;
      }
      // dp
      REP(n,N) if (kde >= B[n]) minLogs[kde] = min( minLogs[kde], minLogs[ kde-B[n] ] + 1 );
      // check for termination
      if (kde >= B[N-1]) if (minLogs[kde]==1987654321 || minLogs[kde] == minLogs[kde - B[N-1]] + 1) ++goodSteps;
      int prev = kde - B[N-1];
      if (prev >= B[N-1]) if (minLogs[prev]==1987654321 || minLogs[prev] == minLogs[prev - B[N-1]] + 1) --goodSteps;
      if (goodSteps == B[N-1]) break;
    }
    int privela = (L - kde) % B[N-1];
    if (privela > 0) kde = (kde - B[N-1] + privela);
    if (minLogs[kde] == 1987654321) {
      cout << "Case #" << t << ": IMPOSSIBLE" << endl;
    } else {
      long long greedy = (L - kde) / B[N-1];
      cout << "Case #" << t << ": " << (greedy + minLogs[kde]) << endl;
    }
  }
  return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
