#include <cstdio>
#include <cstring>

#define forn(i,n) for (int i = 0; i < (int)(n); i++)

#define OR 0
#define AND 1

#define maxn 30010

int g[maxn], c[maxn], v[maxn], d[maxn][2];

int op( int a, int b, int opr )
{
  switch (opr)
  {
    case OR: return a | b;
    case AND: return a & b;
  }
  return -1;
}

int main()
{
  int n;
  scanf("%d", &n);
  forn (test, n)
  {
    int m, val;
    scanf("%d%d", &m, &val);
    forn (i, (m - 1) / 2)
      scanf("%d%d", &g[i + 1], &c[i + 1]);
    forn (i, (m + 1) / 2)
      scanf("%d", &v[i + (m - 1) / 2 + 1]);
    memset(d, 0x7f, sizeof(d));
    forn (i, (m + 1) / 2)
      d[i + (m - 1) / 2 + 1][v[i + (m - 1) / 2 + 1]] = 0;

    for (int i = (m - 1) / 2; i > 0; i--)
      forn (v1, 2) forn (v2, 2)
        if (d[i * 2][v1] != 0x7f7f7f7f && d[i * 2 + 1][v2] != 0x7f7f7f7f)
        {
          d[i][op(v1, v2, g[i])] <?= d[i * 2][v1] + d[i * 2 + 1][v2];
          if (c[i])
            d[i][op(v1, v2, 1 - g[i])] <?= d[i * 2][v1] + d[i * 2 + 1][v2] + 1;
        }
    if (d[1][val] == 0x7f7f7f7f)
      printf("Case #%d: IMPOSSIBLE\n", test + 1);
    else
      printf("Case #%d: %d\n", test + 1, d[1][val]);
  }
  return 0;
}

