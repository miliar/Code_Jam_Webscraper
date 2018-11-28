#include <cstdio>
#include <algorithm>

using namespace std;

int R;
int a[2][101][101];

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int cs, r = 0;
  scanf("%d", &cs);
  while (cs--) {
    printf("Case #%d: ", ++r);
    scanf("%d", &R);
    for (int i = 1; i <= 100; ++i)
      for (int j = 1; j <= 100; ++j)
        a[0][i][j] = a[1][i][j] = 0;
        
    for (int i = 0; i < R; ++i) {
      int x1, x2, y1, y2;
      scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
      for (int y = y1; y <= y2; ++y)
        for (int x = x1; x <= x2; ++x)
          a[0][y][x] = 1;
    }
    
    int t = 0;
    int v = 0;
    for (;;) {
      int fail = 1;
      for (int i = 1; i <= 100; ++i) {
        for (int j = 1; j <= 100; ++j) {
          if (a[v][i][j]) {
            fail = 0;
            if (a[v][i - 1][j] == 0 && a[v][i][j - 1] == 0)
              a[1 - v][i][j] = 0;
            else a[1 - v][i][j] = 1;
          } else {
            if (a[v][i - 1][j] == 1 && a[v][i][j - 1] == 1)
              a[1 - v][i][j] = 1;
            else a[1 - v][i][j] = 0;
          }
        }
      }
      if (fail) break;
      v = 1 - v;
      t++;          
    }
    printf("%d\n", t);
  }
  return 0;
}