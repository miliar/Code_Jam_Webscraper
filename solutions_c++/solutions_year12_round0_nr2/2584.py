#include <stdio.h>
#include <string.h>

int main() {
  int n, sum, res, t, s, p;
  scanf("%d", &n);
  for (int i = 1; i <=n; ++i) {
    scanf("%d %d %d", &t, &s, &p);
    res = 0;
    for (int j = 0;j < t; ++j) {
      scanf("%d", &sum);
      if (sum == 0 ) {
        if (p == 0) {
          ++res;
        }
        continue;
      }
      if ((sum+2)/3 >= p) {
        ++res;
        continue;
      }
      if (s > 0 && sum/3+1 >= p) {
        ++res;
        --s;
        continue;
      }
      if (s > 0 && sum % 3 == 2 && (sum+4)/3 >= p) {
        ++res;
        --s;
        continue;
      }
    }
    printf("Case #%d: %d\n", i, res);
  }
}
