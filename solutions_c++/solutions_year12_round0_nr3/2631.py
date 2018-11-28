#include <stdio.h>
#include <string.h>

#define MAX 2000001

bool flag[MAX];

int main() {
  int n, res, a, b;
  scanf("%d", &n);
  for (int i = 1; i <=n; ++i) {
    scanf("%d %d", &a, &b);
    memset(flag, 0, sizeof(flag));
    res = 0;
    for (int j = a;j < b; ++j) {
      if (flag[j]) continue;

      flag[j] = true;
      int k = j/10;
      int n = 0, m = 1;
      while (k != 0) {
        k /= 10;
        ++n;
        m *= 10;
      }
      k = j;
      int tmp = 0;
      for (int p = 0;p < n; ++p) {
        k = k/10 + k %10 *m;
        if (k >= a&&k <= b&& !flag[k]) {
          flag[k] = true;
          ++tmp;
        }
      }
      res += (tmp+1) * tmp /2;
    }
    printf("Case #%d: %d\n", i, res);
  }
}

