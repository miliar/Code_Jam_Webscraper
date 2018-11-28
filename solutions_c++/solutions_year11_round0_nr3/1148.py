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


int main() {  
//  freopen("dbg.in", "r", stdin);
  int i, j, tc, tcc = 1;
  scanf("%d", &tc);  
  for (; tc--; ) {
    int n; cin >> n;
    vector<int> v(n);
    rep(i, n) cin >> v[i];
    sort(ALL(v));
    int res = 0;
    rep(i, n) res = res ^ v[i];
            
    printf("Case #%d: ", tcc++);
    if (res == 0) {
      cout << (accumulate(ALL(v), 0) - v[0]) << endl;
    } else puts("NO");
    
  }
  
  return 0;
  
}
