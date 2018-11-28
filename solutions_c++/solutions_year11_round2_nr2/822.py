#include <algorithm>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define FOR(i, N, M)  for(int i = (int)(N); i <= (int)(M); ++ i)
#define FORD(i, N, M) for (int i = (int)(N); i >= (int)(M); -- i)
#define FORI(it, x)   for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)
#define REP(i, N)     for(int i = 0; i != (int)(N); ++ i)

inline void solve() { 
  int C,D; cin >> C >> D;
  vector<int> pos;
  REP(c,C) {
    int P,V; cin >> P >> V;
    REP(j, V)
      pos.push_back(P);
  }
  
  vector<int> move(pos.size());
  move[0] = 0;
  int lastpos = pos[0];
  FOR(i, 1, pos.size() - 1){
    int nextpos = max(lastpos + D, pos[i]);
    move[i] = nextpos - pos[i];
    lastpos = nextpos;
  }
  
  int mn = *min_element(move.begin(), move.end());
  int mx = *max_element(move.begin(), move.end());
  cout << (mx - mn) / 2.;
}

int main() {
  int TESTS;
  cin >> TESTS;
  FOR(test, 1, TESTS) {
    cout << "Case #" << test << ": ";
    solve();
    cout << endl;
  }
} 
