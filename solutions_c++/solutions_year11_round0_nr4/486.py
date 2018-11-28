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
  int N,tmp;
  cin >> N;
  vector<int> nums;
  FOR(i,1,N) { cin >> tmp; nums.push_back(tmp - 1); }
  vector<int> vis(N, false);
  double res = 0;
  FOR(i,0,N-1) if(!vis[i]) {
    int len = 0, curr = i;
    do{
      vis[curr] = true;
      ++len;
      curr = nums[curr];
    } while(!vis[curr]);
    if (len != 1)
      res += len;
  }
  cout << fixed << res;
}

int main() {
  cout.precision(6);
  int TESTS;
  cin >> TESTS;
  FOR(test, 1, TESTS) {
    cout << "Case #" << test << ": ";
    solve();
    cout << endl;
  }
} 
