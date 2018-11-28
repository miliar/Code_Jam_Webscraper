#include<cstdio>
main() {
  int i, j, n, m, T, C = 1;
  scanf("%d", &T);
  while (T--) {
    scanf("%d %d", &m, &n);
    double p, c = 1, x = n + 2, y;
    for (i = 0; i < m; ++i) {
      scanf("%lf", &p);
      c *= p;
      y = (m-i-1)*2 + (n-m) + 1 + (n+1)*(1-c);
      if (y < x) x = y;
    }
    printf("Case #%d: %.6lf\n", C++, x);
  }
}
