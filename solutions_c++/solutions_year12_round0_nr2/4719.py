#include <cstdio>

int main() {
  int t, n, s, p, a;
  scanf("%d", &t);
  for (int i = 1; i <= t; ++i) {
    int res = 0;
    scanf("%d %d %d", &n, &s, &p);
    while (n--) {
      scanf("%d", &a);
      if (a / 3 >= p) {
        ++res;
      } else if(a % 3 > 0 && (a / 3) + 1 >= p) {
        ++res;
      } else if(a % 3 == 0 && a > 0 && s > 0 && (a / 3) + 1 >= p) {
        ++res;
        --s;
      } else if(a % 3 == 2 && s > 0 && (a / 3) + 2 >= p) {
        ++res;
        --s;
      }
    }
    printf("Case #%d: %d\n", i, res);
  }
  return 0;
}

