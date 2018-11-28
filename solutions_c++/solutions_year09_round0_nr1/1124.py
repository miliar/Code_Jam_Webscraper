#include <cstdio>
#include <cstring>
#include <cassert>

#define forn(i, n) for (int i = 0; i < (int)(n); i++)

const int maxn = 5000;
const int mlen = 15;

int L, N, T, is[mlen][26];
char s[maxn][mlen + 1], w[mlen * 28 + 1];

int main()
{
  scanf("%d%d%d", &L, &N, &T);
  forn(i, N)
    scanf("%s", s[i]);

  for (int t = 1; t <= T; t++)
  {
    scanf("%s", w);
    assert(strlen(w) < sizeof(w));
    memset(is, 0, sizeof(is));
    
    int pos = 0;
    forn(i, L)
      if (w[pos] == '(')
      {
        pos++;
        while (w[pos] != ')')
        {
          assert('a' <= w[pos] && w[pos] <= 'z');
          is[i][w[pos++] - 'a'] = 1;
        }
        pos++;
      }
      else
      {
        assert('a' <= w[pos] && w[pos] <= 'z');
        is[i][w[pos++] - 'a'] = 1;
      }

    int cnt = 0;
    forn(i, N)
    {
      int good = 1;
      forn(j, L)
        good &= is[j][s[i][j] - 'a'];
      cnt += good;
    }
    printf("Case #%d: %d\n", t, cnt);
  }
  return 0;
}
