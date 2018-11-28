#include <algorithm>
#include <cstdio>
#include <cstring>

using namespace std;

typedef long double dbl;

#define forn(i,n) for (int i = 0; i < (int)(n); i++)

#define eps 1e-12

#define maxl 50010
#define maxk 17
#define maxp ((1 << 16) + 20)

int k, len;
char s[maxl];
int d[maxp][maxk][maxk];
int d1[maxk][maxk];

int main()
{
  int nn;
  scanf("%d", &nn);
  forn (tst, nn)
  {
    scanf("%d ", &k);
    gets(s);
    len = strlen(s);
    memset(d, 0x7f, sizeof(d));
    forn (i, k)
      d[1 << i][i][i] = 0;

    forn (i, k) forn (j, k)
    {
      d1[i][j] = 0;
      for (int ii = 0; ii < len; ii += k)
        d1[i][j] += s[ii + i] != s[ii + j];
    }

    forn (p, (1 << k)) forn (i, k) forn (j, k)
    {
/*      if (p % 1000 == 0 && i == 0 && j == 0)
        fprintf(stderr, "p = %d\n", p);*/
      if (p == (1 << k) - 1 || p == 0)
        continue;
      int res = d[p][i][j];
      if (res == 0x7f7f7f7f)
        continue;
      int sz = 0;
      forn (t, k)
        if ((p & (1 << t)) != 0)
          sz++;
      forn (t, k)
        if ((p & (1 << t)) == 0)
        {
          int tmp = res;
          tmp += d1[t][j];
//           for (int ii = 0; ii < len; ii += k)
//             tmp += s[ii + t] != s[ii + j];
          if (sz == k - 1)
            for (int ii = 0; ii + k < len; ii += k)
              tmp += s[ii + k + i] != s[ii + t];
          d[p | (1 << t)][i][t] <?= tmp;
        }
    }

    int ans = 1 << 30;
    if (k == 1)
    {
      ans = 0;
      forn(i, len)
        ans += i > 0 && s[i] != s[i - 1];
    }
    else
      forn (i, k) forn (j, k)
        ans <?= d[(1 << k) - 1][i][j];
    printf("Case #%d: %d\n", tst + 1, ans + 1);
    fprintf(stderr, "test #%d complete!\n", tst);
  }
  return 0;
}

