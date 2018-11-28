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
// }}}

/////////////////// CODE WRITTEN DURING THE COMPETITION FOLLOWS ////////////////////////////////

int main() {
  int T;
  cin >> T;
  FOR(t,1,T) {
    set<int> todo;
    map<int,int> pocet;
    int C;
    cin >> C;
    while (C--) {
      int P, V;
      cin >> P >> V;
      if (V > 1) todo.insert(P);
      pocet[P] = V;
    }
    int steps = 0;
    while (!todo.empty()) {
      int kde = *todo.begin();
      todo.erase( todo.begin() );
      ++steps;
      pocet[kde] -= 2;
      pocet[kde-1] += 1;
      pocet[kde+1] += 1;
      for (int d=-1; d<=+1; ++d) if (pocet[kde+d]>1) todo.insert(kde+d);
    }
    cout << "Case #" << t << ": " << steps << endl;
  }
  return 0;
}
// vim: fdm=marker:commentstring=\ \"\ %s:nowrap:autoread
