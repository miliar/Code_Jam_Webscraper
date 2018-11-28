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
#include <cassert>

using namespace std;

#define FOR(i, N, M)  for(int i = (int)(N); i <= (int)(M); ++ i)
#define FORD(i, N, M) for (int i = (int)(N); i >= (int)(M); -- i)
#define FORI(it, x)   for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)
#define REP(i, N)     for(int i = 0; i != (int)(N); ++ i)
#define ALL(c) c.begin(), c.end() 

#define MAXN 50

int R,C,tmp;
char field[MAXN][MAXN];

inline void solve() { 
  cin >> R >> C;
  char tc;
  REP(i,R) REP(j,C){
    do { cin >> tc; } while(tc != '.' && tc != '#');
    field[i][j] = tc;
  }

  bool poss= true;
  REP(i,R) REP(j,C) {
    if(field[i][j] == '#'){
      if(i+1 >= R || j+1 >= C) {
        poss = false;
        goto done; // :P
      }
      if(field[i][j+1] != '#' || field[i+1][j] != '#' || field[i+1][j+1] != '#') {
        poss = false;
        goto done;
      }
      // set
      field[i][j] = field[i+1][j+1]  = '/' ;
      field[i][j+1] = field[i+1][j] = '\\';
    }
  }
done:;
     cout << endl;
  if(!poss){
    cout << "Impossible" << endl;
  } else{
    REP(i,R) { 
      REP(j,C){
        cout << field[i][j];
      }
      cout << endl;
    }
  }
}

int main() {
  int TESTS;
  cin >> TESTS;
  FOR(test, 1, TESTS) {
    cout << "Case #" << test << ":";
    solve();
  }
} 
