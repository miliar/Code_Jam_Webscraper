#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <iomanip>
#include <algorithm>
#include <vector>
#include <string>
#include <set>
#include <map>
using namespace std;

typedef long long ll;

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int test_count;
  cin >> test_count;
  for (int test_index = 0; test_index < test_count; ++test_index) {
    int n, m, d;
    cin >> n >> m >> d;
    vector<string> s(n);
    getline(cin, s[0]);
    for (int i = 0; i < n; ++i)
      getline(cin, s[i]);
    int res = -1;
    for (int k = 3; k <= max(n, m); ++k) {
      int tt = 0;
      for (int i = 0; i <= n - k; ++i)
        for (int j = 0; j <= m - k; ++j) {
          double yC = i + (double)k / 2;
          double xC = j + (double)k / 2;
          double masX = 0, masY = 0;
          for (int y = i; y < i + k; ++y)
            for (int x = j; x < j + k; ++x) {
              if (y == i && (x == j || x == j + k - 1) || y == i + k - 1 && (x == j || x == j + k - 1)) continue;
              masX += (x + .5 - xC) * (d + (s[y][x] - '0'));
              masY += (y + .5 - yC) * (d + (s[y][x] - '0'));
            }
          if (masX == 0 && masY == 0)
            res = k;
        }
    }
    cout << "Case #" << test_index + 1 << ": ";
    if (res == -1)
      cout << "IMPOSSIBLE" << endl;
    else
      cout << res << endl;
    
  }
  return 0;
}