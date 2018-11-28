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
#include <functional>
#include <numeric>
#include <queue>

using namespace std;

#define FOR(i, N, M)  for(int i = (int)(N); i <= (int)(M); ++ i)
#define FORD(i, N, M) for (int i = (int)(N); i >= (int)(M); -- i)
#define FORI(it, x)   for (__typeof((x).begin()) it = (x).begin(); it != (x).end(); ++it)
#define REP(i, N)     for(int i = 0; i != (int)(N); ++ i)
#define ALL(c) c.rbegin(), c.rend() 

int L,N,C;
long long t;
long tsum;

inline void solve() { 
  cin >> L >> t >> N >> C;
  vector<int> ai(C);
  REP(i,C) cin >> ai[i];
 
  vector<long long> rests;
  long long sum = 0;
  REP(i, N) {
    long long len = 2*ai[i % C];
    sum += len;
    if(sum >= t){
      rests.push_back(min(len, sum - t)); 
    }
  }

  sort(ALL(rests));
  //cout << " " << rests[0] << " " << rests[1] << endl;
  long long spare = 0;
  REP(i, L){
    //cout << "spare " << rests[i] << endl;
    spare += rests[i] / 2 ;
  }


  cout << (sum - spare);
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
