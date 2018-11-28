#include <cstdio>
#include <cstdlib>

int main() {
    int t, n, l, h, i, j, a = 1;
    int f[100];
    scanf("%d", &t);
    while (t--) {
          scanf("%d %d %d", &n, &l, &h);
          for (i = 0; i < n; i++)
              scanf("%d", &f[i]);
          for (i = l; i <= h; i++) {
              for (j = 0; j < n && ((f[j] % i == 0) || (i % f[j] == 0)); j++);
              // printf("%d\n", j);
              if (j == n) break;
          }
          
          if (i <= h)
             printf("Case #%d: %d\n", a++, i);
          else printf("Case #%d: NO\n", a++);
    }
    return 0;
}
