#include<cstdio>
#include<algorithm>
using namespace std;
const int N = 1111;
int x[N], y[N];
main() {
  char a[9];
  int i, j, k, n, m, c, T, C = 1;
  scanf("%d", &T);
  while (T--) {
    scanf("%d", &n);
    for (i = 0; i < n; ++i)
      scanf("%d %d", x+i, y+i);
    for (c = k = 0, m = 2*n; m > 0; ++c) {
      for (i = 0, j = -1; i < n; ++i) {
        if (k < x[i] || x[i] < 0) continue;
        if (y[i] >= 0 && k >= y[i]) {
          j = i;
          --m, ++k;
          x[i] = y[i], y[i] = -1;
          break;
        }
        if (y[i] < 0) {
          j = i;
          break;
        }
        if (j < 0 || y[i] < 0 || (y[i] > y[j])) j = i;
      }
      if (j < 0 || k < x[j]) break;
      --m, ++k;
      x[j] = y[j], y[j] = -1;
    }
    printf("Case #%d: ", C++);
    if (m > 0) puts("Too Bad");
    else printf("%d\n", c);
  }
}

