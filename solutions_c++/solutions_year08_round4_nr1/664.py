#include <cstdio>

#define m 100000

#define forn(i, n) for (int i = 0; i < (int)(n); i++)

int nt, n, g[m], c[m], r[m][2], v;

int main()
{
  freopen("bool.in", "r", stdin);
  freopen("bool.out", "w", stdout);
  scanf("%d", &nt);
  forn (tt, nt)
  {
    printf("Case #%d: ", tt + 1);
    scanf("%d%d", &n, &v);
    forn (i, (n - 1) / 2)
      scanf("%d%d", &g[i], &c[i]);
    forn (i, (n + 1) / 2)
      scanf("%d", &c[(n - 1) / 2 + i]), g[(n - 1) / 2 + i] = 2;
    for (int i = n - 1; i >= 0; i--)
    {
      if (g[i] == 2)
        r[i][c[i]] = 0, r[i][1 - c[i]] = -1;
      else
      {
        r[i][0] = r[i][1] = -1;
        int nl = i * 2 + 1, nr = nl + 1;
        forn (t, 2) forn (vl, 2) forn (vr, 2)
        {
          int s = 0;
          if (t != g[i])
            if (c[i] == 0)
              continue;
            else
              s++;
          if (r[nl][vl] == -1 || r[nr][vr] == -1)
            continue;
          s += r[nl][vl] + r[nr][vr];
          int q;
          if (t == 0)
            q = vl || vr;
          else
            q = vl && vr;
          if (r[i][q] == -1 || r[i][q] > s)
            r[i][q] = s;
        }
      }
    }
    if (r[0][v] == -1)
      printf("IMPOSSIBLE\n");
    else
      printf("%d\n", r[0][v]);
  }
  return 0;
}
