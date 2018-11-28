#include <cstdio>
#include <cassert>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <iostream>

using namespace std;

#define maxn 110

int a[2][maxn][maxn];

int main (void) {
  int tn;
  scanf("%d", &tn);

  for (int t = 1; t <= tn; t++) {
    printf("Case #%d: ", t);

    memset(a, 0, sizeof(a));
    int r;
    cin >> r;
    for (int i = 0; i < r; i++) {
      int xa, xb, ya, yb;
      cin >> xa >> ya >> xb >> yb;
      for (int x = xa; x <= xb; x++) {
        for (int y = ya; y <= yb; y++) {
          a[0][x][y]  = 1;
        }
      }
    }
    int cnt = 0, _ = 0, f = 1;
    while (f) {
      f = 0;
      cnt++;
      for (int i = 1; i + 1 < maxn; i++) {
        for (int j = 1; j + 1 < maxn; j++) {
          if (a[_][i][j]) {
            f = 1;
          }
          if (a[_][i][j] && !a[_][i - 1][j] && !a[_][i][j - 1]) {
            a[1 - _][i][j] = 0;
          } else if (a[_][i][j] || a[_][i - 1][j] && a[_][i][j - 1]) {
            a[1 - _][i][j] = 1;
          } else {
            a[1 - _][i][j] = 0;
          }
        }
      }
      memset(a[_], 0, sizeof(a[_]));
      _ ^= 1;
    }
    printf("%d\n", cnt - 1);
  }

  return 0;
} 