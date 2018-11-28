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

inline void solve() { 
  int N,L,H;
  cin >> N >> L >> H;
  vector<int> oth(N);
  REP(i,N) cin >> oth[i];
  FOR(freq, L, H){
    bool poss = true;
    FORI(it, oth){
      int n = *it;
      if(n % freq != 0 && freq % n != 0) {
        poss = false;
        break;
      }

    }
    if(!poss) continue;
    cout << freq;
    return;
  }
  cout << "NO";
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
