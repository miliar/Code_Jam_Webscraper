#include <cstdio>
#include <cstring>

#define forn(i, n) for (int i = 0; i < (int)(n); i++)

const int ml = 505;

char a[ml];
const char b[ml] = "welcome to code jam";
int nt, f[ml][ml];

int main()
{
  scanf("%d", &nt);
  gets(a);
  forn (t, nt)
  {
    gets(a);
    int la = strlen(a), lb = strlen(b);
    forn (i, lb)
      forn (j, la)
        f[i][j] = 0;
    forn (i, la)
      if (a[i] == b[0])
        f[0][i] = 1;
    forn (i, lb - 1)
      forn (j, la)
        for (int k = j + 1; k < la; k++)
          if (a[k] == b[i + 1])
            f[i + 1][k] = (f[i + 1][k] + f[i][j]) % 10000;
    int ans = 0;
    forn (i, la)
      ans = (ans + f[lb - 1][i]) % 10000;
    printf("Case #%d: %04d\n", t + 1, ans);
  }
  return 0;
}
