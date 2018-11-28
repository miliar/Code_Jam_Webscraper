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
#include <functional>
#include <numeric>

using namespace std;

#define FOR(i, N, M)  for(int i = (int)(N); i <= (int)(M); ++ i)
#define FORD(i, N, M) for (int i = (int)(N); i >= (int)(M); -- i)
#define FORI(it, x)   for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)
#define REP(i, N)     for(int i = 0; i != (int)(N); ++ i)

inline void solve() { 
  vector<int> candy;  
  int N, c;
  cin >> N;
  FOR(i,1,N) {
    cin >> c;
    candy.push_back(c);
  }
  int sum = accumulate(candy.begin(), candy.end(), 0);
  int mini = *min_element(candy.begin(), candy.end());
  int res = sum - mini;

  while(true) {
    bool fin = true;
    int ones = 0;
    FORI(it, candy){
      int n = *it;
      if(n != 0) fin = false;
      ones += n & 1;
      *it >>= 1;
    }
    if(fin) break;
    if(ones % 2 != 0) {
      cout << "NO";
      return;
    }
  }

  cout << res;
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
