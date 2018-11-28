#include <cstdio>

int T, n, m, a, t;
bool d;

int ok(int a) {
  for (int i = (a - 1)/m + 1; i <= n; ++i)
    if (!(a%i))
      return i;
  return 0;
}

int main() {
  scanf("%d", &T);
  for (int r = 1; r <= T; ++r) {
    printf("Case #%d: ", r);
    scanf("%d%d%d", &n, &m, &a);
    if (t = ok(a))
      printf("0 0 %d 0 0 %d\n", t, a/t);
    else {
      d = 1;
      for (int i = 1; i <= n && d; ++i)
        for (int j = i; j <= m && d; ++j)
          if (t = ok(a + i*j)) {
            printf("0 0 %d %d %d %d\n", t, j, i, (a + i*j)/t);
            d = 0;
          }
      if (d)
        puts("IMPOSSIBLE");
    }
  }
  return 0;
}
