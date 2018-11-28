#include <cstdio>

#define min(a, b) ((a) < (b) ? (a) : (b))

int main() {
    int t, n, sx, s, m, a = 1, i, c;
    scanf("%d", &t);
    while (t--) {
          s = sx = 0; m = 1 << 30;
          scanf("%d", &n);
          for (i = 0; i < n; i++) scanf("%d", &c), sx ^= c, s += c, m = min(m, c);
          
          if (sx) printf("Case #%d: NO\n", a++);
          else printf("Case #%d: %d\n", a++, s - m);
    }
    return 0;
}
