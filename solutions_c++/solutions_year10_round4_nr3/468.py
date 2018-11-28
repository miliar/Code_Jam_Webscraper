#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <functional>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <valarray>
#include <vector>
#include <ext/algorithm>
#include <ext/hash_map>
#include <ext/hash_set>
#include <ext/numeric>
using namespace std;
using namespace __gnu_cxx;
 
#define F(i,a,b)for(int i=a;i<b;++i)
#define rep(i,n)F(i,0,n)
#define all(a)a.begin(),a.end()
template<class T>vector<T>&operator<<(vector<T>& v,T t){v.push_back(t);return v;} 

typedef pair<int, int> pii;

#define MX 20000
int grid[MX][MX];
int buf[MX][MX];

int main() {
  int T;
  cin >> T;
  for (int t = 1; t <= T; ++t) {
    memset(grid, 0, sizeof(grid));
    int R;
    cin >> R;
    int count;
    rep(r,R) {
      int x1, y1, x2, y2;
      cin >> x1 >> y1 >> x2 >> y2;
      F(i, x1, x2+1) {
        F(j, y1, y2+1) {
          grid[i][j] = 1;
          count++;
        }
      }
    }
    int res = 0;
    while (count > 0) {
      count = 0;
      res++;
      memset(buf, 0, sizeof(buf));
      F(i,1, MX) F(j,1, MX) {
        if (grid[i][j] && (grid[i-1][j] || grid[i][j-1])) {
          buf[i][j] = 1;
          count++;
        }
        if (grid[i-1][j] && grid[i][j-1]) {
          buf[i][j] = 1;
          count++;
        }
      }
      memcpy(grid, buf, sizeof(buf));
    }
    printf("Case #%d: %d\n", t, res);
  }
}
