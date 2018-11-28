#include <algorithm>
#include <iomanip>
#include <iostream>
#include <cmath>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <vector>

#define FR first
#define SC second

using namespace std;

const int INF = 1000000000;

template <class Ta, class Tb> inline Tb cast(Ta a) {
  stringstream ss;
  ss << a;
  Tb b;
  ss >> b;
  return b;
}

int main() {
  int T;
  cin >> T;
  for (int ca = 1; T--; ++ca) {
    cerr << "ca = " << ca << endl;
    int n, W, L;
    cin >> n >> W >> L;
    vector<pair<int, int> > r(n);
    for (int i = 0; i < n; ++i) {
      cin >> r[i].FR;
      r[i].SC = i;
    }
    sort(r.begin(), r.end());
    vector<pair<int, int> > ans(n);
    int y0 = -INF, x0 = -INF, nxt_y0 = -INF;
    for (int i = n-1; i >= 0; --i) {
      int y = max(0, y0+r[i].FR);
      if (y > L) {
        cerr << "ERROR: y out of range" << endl;
      }
      int x = max(0, x0+r[i].FR);
      if (x > W) { // end of row
        y0 = nxt_y0;
        nxt_y0 = -INF;
        x0 = -INF;
        y = max(0, y0+r[i].FR);
        if (y > L) {
          cerr << "ERROR: y out of range" << endl;
        }
        x = max(0, x0+r[i].FR);
      }
      ans[r[i].SC] = pair<int, int>(x, y);
      nxt_y0 = max(nxt_y0, y+r[i].FR);
      x0 = max(x0, x+r[i].FR);
    }
    cout << "Case #" << ca << ":";
    for (int i = 0; i < n; ++i) {
      cout << " " << ans[i].FR << " " << ans[i].SC;
    }
    cout << endl;
  }
}
