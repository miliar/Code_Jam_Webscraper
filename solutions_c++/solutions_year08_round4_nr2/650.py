#include <cstdio>
#include <cstdlib>

#define forn(i, n) for (int i = 0; i < (int)(n); i++)

int nt, w, h, a;

int main()
{
  freopen("tri.in", "r", stdin);
  freopen("tri.out", "w", stdout);
  scanf("%d", &nt);
  forn (tt, nt)
  {
    printf("Case #%d: ", tt + 1);
    scanf("%d%d%d", &w, &h, &a);
    bool ok = false;
    forn (x1, w + 1)
      forn (y1, h + 1)
        forn (x2, x1 + 1)
          forn (y2, h + 1)
          {
            if (abs(x1 * y2 - x2 * y1) == a)
            {
              printf("%d %d %d %d %d %d\n", 0, 0, x1, y1, x2, y2);
              ok = true;
              y2 = y1 = h + 2;
              x2 = x1 = w + 2;
            }
          }
    if (!ok)
      printf("IMPOSSIBLE\n");
  }
  return 0;
}
