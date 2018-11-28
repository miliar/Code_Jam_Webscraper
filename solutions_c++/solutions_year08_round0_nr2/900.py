#include <cstdio>
#include <cstring>

#define m 1500

int na, tt, nb, n, da[m], db[m], fia[m], fib[m], sta[m], stb[m];

int readt()
{
  int h, mi;
  scanf("%d:%d", &h, &mi);
  return h * 60 + mi;
}

int main()
{
  freopen("b.in", "r", stdin);
  freopen("b.out", "w", stdout);
  scanf("%d", &n);
  for (int i = 0; i < n; i++)
  {
    scanf("%d%d%d", &tt, &na, &nb);
    for (int j = 0; j < na; j++)
      sta[j] = readt(), fia[j] = readt();
    for (int j = 0; j < nb; j++)
      stb[j] = readt(), fib[j] = readt();
    memset(da, 0, sizeof(da));
    memset(db, 0, sizeof(db));
    for (int j = 0; j < na; j++)
      da[sta[j]]--, db[fia[j] + tt]++;
    for (int j = 0; j < nb; j++)
      db[stb[j]]--, da[fib[j] + tt]++;
    int ra = 0, rb = 0, na = 0, nb = 0;
    for (int j = 0; j < m; j++)
    {
      na += da[j];
      while (na < 0)
        na++, ra++;
      nb += db[j];
      while (nb < 0)
        nb++, rb++;
    }
    printf("Case #%d: %d %d\n", i + 1, ra, rb);
  }
  return 0;
}
