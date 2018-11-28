#include<cstdio>
main() {
  int i, j, k, n, m, a, T, C = 1;
  scanf("%d", &T);
  while (T--) {
    scanf("%d %d %d" , &n, &m, &k);
    for (i = a = 0; i < n; ++i) {
      scanf("%d", &j);
      if ((j+2)/3 >= k) {
        ++a;
        continue;
      }
      if (j < 2 || j > 28) continue;
      if (m > 0 && (j+2)/3 + 1 >= k && j%3 != 1)
        --m, ++a;
    }
    printf("Case #%d: %d\n", C++, a);
  }
}
