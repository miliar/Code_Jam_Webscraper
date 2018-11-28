#include <map>
#include <set>
#include <cmath>
#include <stack>
#include <queue>
#include <bitset>
#include <cctype>
#include <cstdio>
#include <string>
#include <vector>
#include <complex>
#include <cstdlib>
#include <cstring>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <valarray>
#include <algorithm>
#include <functional>

#define REP(i,a,b) for((i)=(a);(i)<(b);(i)++)
#define rep(i,b)   REP(i,0,b)
#define FOR(i,c)   for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c)     (c).begin(), (c).end()

using namespace std;
typedef long long ll;
const double eps = 1e-10;
const int inf = 1<<28;

typedef pair<int,int> P;

int main() {
//  freopen("dbg.in", "r", stdin);
  int i, j, tc, tcc = 1;
  scanf("%d", &tc);  
  for (; tc--; ) {    
    int n; cin >> n;
    vector<P> v(n);
    rep(i, n) {
      char c; int t, u;
      cin >> c >> t;
      if (c == 'O') u = 0;
      if (c == 'B') u = 1;
      v[i] = P(u, t);
    }
    int opos = 1, bpos = 1, res = 0;
    int dtime = 0, prev;
    P p;
    prev = v[0].first;
    rep(i, n) {
      p = v[i];
      if (p.first == 0) {
        if (prev == p.first) {
          res += abs(opos - p.second) + 1;
          dtime += abs(opos - p.second) + 1;
        } else {
          res += max(1, abs(opos - p.second) - dtime + 1);
          dtime = max(1, abs(opos - p.second) - dtime + 1);
        }
        prev = p.first;        
        opos = p.second;        
      } else {
        if (prev == p.first) {
          res += abs(bpos - p.second) + 1;
          dtime += abs(bpos - p.second) + 1;
        } else {
          res += max(1, abs(bpos - p.second) - dtime + 1);
          dtime = max(1, abs(bpos - p.second) - dtime + 1);
        }
        prev = p.first;
        bpos = p.second;        
      }
    }
    printf("Case #%d: ", tcc++);
    cout << res << endl;
  }
  
  return 0;
  
}
