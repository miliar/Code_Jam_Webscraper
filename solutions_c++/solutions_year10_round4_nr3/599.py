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

#define fr first
#define sc second

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
  vector<vector<bool> > empty(120, vector<bool>(120, false));
  int C;
  cin >> C;
  for (int ca = 1; C--; ++ca) {
    cerr << "ca = " << ca << endl;
    vector<vector<bool> > v = empty;
    int r;
    cin >> r;
    for (int ir = 0; ir < r; ++ir) {
      int x1, y1, x2, y2;
      cin >> x1 >> y1 >> x2 >> y2;
      for (int i = y1; i <= y2; ++i) {
        for (int j = x1; j <= x2; ++j) {
          v[i][j] = true;
        }
      }
    }
    int t = 0;
    for (; v != empty; ++t) {
      vector<vector<bool> > w = empty;
      for (int i = 1; i < int(w.size()); ++i) {
        for (int j = 1; j < int(w[i].size()); ++j) {
          if (v[i][j]) {
            if (v[i-1][j] || v[i][j-1]) w[i][j] = true;
            else w[i][j] = false;
          }
          else {
            if (v[i-1][j] && v[i][j-1]) w[i][j] = true;
            else w[i][j] = false;
          }
        }
      }
      v = w;
    }
    cout << "Case #" << ca << ": " << t << endl;
  }
}
