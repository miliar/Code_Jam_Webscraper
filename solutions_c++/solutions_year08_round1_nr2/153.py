#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Shop {
public:
  void input() {
    cin >> n >> m;
    cs.resize(m, vector<int>(n,-1));
    for (int i = 0; i < m; ++i) {
      int t;
      cin >> t;
      for (int j = 0; j < t; ++j) {
        int x, y;
        cin >> x >> y;
        cs[i][x-1] = y;
      }
    }
#if 0
    for (int i = 0; i < m; ++i) {
      for (int j = 0; j < n; ++j) {
        cout << ' ' << cs[i][j];
      }
      cout << endl;
    }
#endif
  }
  void calc() {
  }
  void output() {
    vector<int> tbl(n, 0);
    for (;;) {
      bool fin=true;
      for (int i = 0; i < m; ++i) {
        bool ok = false;
        int mal = -1;
        for (int j = 0; j < n; ++j) {
          if (cs[i][j]==tbl[j]) { ok=true; break; }
          else if (cs[i][j]==1) mal=j;
        }
        if (!ok) {
          if (mal<0) {
            cout << " IMPOSSIBLE" << endl;
            return;
          } else {
            tbl[mal]=1;
          }
        }
        fin = fin && ok;
      }
      if (fin) break;
    }
    for (int i = 0; i < n; ++i) {
      cout << ' ' << tbl[i];
    }
    cout << endl;
  }
private:
  int n, m;
  vector<vector<int> > cs;
};

int main() {
  int c;
  cin >> c;
  for (int i = 1; i <= c; ++i) {
    Shop s;
    s.input();
    s.calc();
    cout << "Case #" << i << ":";
    s.output();
  }
}
