#include <cstdio>
#include <cstring>
#include <cassert>

#include <vector>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)

const int maxn = 503;

char s[maxn], *w = "welcome to code jam";
int T, f[25][maxn];

void add( int &a, int b )
{
  static int M = 10000;

  a += b;
  if (a >= M)
    a -= M;
}

int main()
{
  scanf("%d", &T);
  gets(s);
  for (int t = 1; t <= T; t++)
  {
    gets(s);
    int N = strlen(s);
    int K = strlen(w);
    memset(f, 0, sizeof(f));
    f[0][0] = 1;
    forn(i, K + 1)
      forn(j, N + 1)
        if (f[i][j])
        {
          add(f[i][j + 1], f[i][j]);
          if (w[i] == s[j])
            add(f[i + 1][j + 1], f[i][j]);
        }

    printf("Case #%d: %04d\n", t, f[K][N]);
  }
  return 0;
}
