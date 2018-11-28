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

vector<string> W;
int ok[20][30];

int main() {
  int L, D, N;
  cin >> L >> D >> N;
  REP(d,D) { string S; cin >> S; W.push_back(S); }
  FOR(n,1,N) {
    string P;
    cin >> P;
    int kde = 0;
    REP(l,L) {
      REP(i,26) ok[l][i] = 0;
      if (P[kde]=='(') {
        ++kde;
        while (P[kde]!=')') {
          ok[l][ P[kde]-'a' ] = 1;
          ++kde;
        }
        ++kde;
      } else {
        ok[l][ P[kde]-'a' ] = 1;
        ++kde;
      }
    }
    int res = 0;
    REP(d,D) {
      int good = 1;
      REP(l,L) good &= ok[l][ W[d][l]-'a' ];
      res += good;
    }
    cout << "Case #" << n << ": " << res << endl;
  }
  return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
