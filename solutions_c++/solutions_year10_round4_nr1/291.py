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

inline bool sym(vector<vector<int> >& e) {
  int siz = int(e.size());
  for (int i = 0; i < siz; ++i) {
    for (int j = 0; j <= i; ++j) {
      int si = j, sj = i;
      if (e[i][j] != -1 && e[si][sj] != -1 && e[i][j] != e[si][sj]) {
        return false;
      }
    }
  }
  for (int i = 0; i < siz; ++i) {
    for (int j = 0; j <= siz-1-i; ++j) {
      int si = siz-1-j, sj = siz-1-i;
      if (e[i][j] != -1 && e[si][sj] != -1 && e[i][j] != e[si][sj]) {
        return false;
      }
    }
  }
  return true;
}

int main() {
  int T;
  cin >> T;
  for (int ca = 1; T--; ++ca) {
    cerr << "ca = " << ca << endl;
    int k;
    cin >> k;
    vector<vector<int> > d(k, vector<int>(k));
    for (int i = 0; i < k; ++i) {
      for (int j = 0; j <= i; ++j) {
        cin >> d[i-j][j];
      }
    }
    for (int i = 0; i < k-1; ++i) {
      for (int j = 0; j < k-1-i; ++j) {
        cin >> d[k-1-j][1+i+j];
      }
    }
    int mnsiz = -1;
    for (int siz = k; mnsiz == -1; ++siz) {
      vector<vector<int> > e(siz, vector<int>(siz, -1));
      for (int y = 0; y+k-1 < siz && mnsiz == -1; ++y) {
        for (int x = 0; x+k-1 < siz && mnsiz == -1; ++x) {
          if (y == 0 || x == 0 || y+k-1 == siz-1 || x+k-1 == siz-1) {
            for (int i = 0; i < k; ++i) {
              for (int j = 0; j < k; ++j) {
                e[y+i][x+j] = d[i][j];
              }
            }
            if (sym(e)) mnsiz = siz;
            for (int i = 0; i < k; ++i) {
              for (int j = 0; j < k; ++j) {
                e[y+i][x+j] = -1;
              }
            }
          }
        }
      }
    }
    cout << "Case #" << ca << ": " << mnsiz*mnsiz - k*k << endl;
  }
}
