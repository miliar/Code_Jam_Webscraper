#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int T;

struct q {
  int a, b, c, d;
  q(int _a, int _b, int _c, int _d) : a(_a), b(_b), c(_c), d(_d) {}
};

vector<q> data[25000];

inline int area(int x1, int y1, int x2, int y2) {
  float a = sqrtf(x1 * x1 + y1 * y1), b = sqrtf(x2 * x2 + y2 * y2), c = 
    sqrtf((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
  float a2 = sqrtf((a + b - c) * (a - b + c) * (- a + b + c) * (a + b + c));
  return (int)(a2 / 2.0f + 0.5f);
}

int main() {
  for (int x1 = 0; x1 <= 50; x1++) for (int y1 = 0; y1 <= 50; y1++)
    for (int x2 = 0; x2 <= 50; x2++) for (int y2 = 0; y2 <= 50; y2++) {
      int a = area(x1, y1, x2, y2);
      data[a].push_back(q(x1, y1, x2, y2));
    }


  cin >> T;
  for (int nn = 1; nn <= T; nn++) {
    int n, m, a; cin >> n >> m >> a;
    for (int i = 0; i < data[a].size(); i++) {
      q qq = data[a][i];
      if (qq.a <= n && qq.c <= n && qq.b <= m && qq.d <= m) {
        cout << "Case #" << nn << ": 0 0 " << qq.a << " " << qq.b << " " << qq.c << " " << qq.d << endl;
        goto end;
      }
    }

    cout << "Case #" << nn << ": " << "IMPOSSIBLE" << endl;
end:;
  }

  return 0;
}