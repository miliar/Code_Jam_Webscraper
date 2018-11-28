#include <cstdio>
#include <cstring>

#define forn(i, n) for (int i = 0; i < (int)(n); i++)

typedef unsigned long long ull;

using namespace std;

#define m 50
#define mm 210

int n, l;
char s[m];
ull r[m][mm];

int main()
{
  freopen("ugly.in", "r", stdin);
  freopen("ugly.out", "w", stdout);
  scanf("%d", &n);
  forn (tt, n)
  {
    printf("Case #%d: ", tt + 1);
    scanf("%s", s);
    l = strlen(s);
    memset(r, 0, sizeof(r));
    r[0][0] = 1;
    forn (i, l)
      forn (j, mm)
      {
        int t = 0;
        for (int k = i; k < l; k++)
        {
          t = (t * 10 + s[k] - '0') % mm;
          r[k + 1][(j + t) % mm] += r[i][j];
          if (i > 0)
            r[k + 1][(j + mm - t) % mm] += r[i][j];
        }
      }
    ull ans = 0;
    forn (i, mm)
      if (i % 2 == 0 || i % 3 == 0 || i % 5 == 0 || i % 7 == 0)
        ans += r[l][i];
    printf("%llu\n", ans);
  }
  return 0;
}
