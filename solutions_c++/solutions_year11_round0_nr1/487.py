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
  int N;
  cin >> N;
  int pos[2] = {1,1};
  int lastmove = 0, totaltime = 0;
  char last = 'x'; 
  FOR(i, 1, N) {
    char type;
    int newpos;
    cin >> type; 
    cin >> newpos;

    int idx = 0; if(type == 'O') idx = 1;

    int movetime = abs(pos[idx] - newpos) + 1;
    if(last != type)
      movetime = max(1, movetime - lastmove);
    pos[idx] = newpos;
    totaltime += movetime;
    if(last == type)
      lastmove += movetime;
    else
      lastmove = movetime;

    last = type;
  }

  cout << totaltime;
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
