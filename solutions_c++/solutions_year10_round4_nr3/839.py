#include <cstdio>
#include <iostream>
#include <string>
#include <memory.h>
#include <string.h>
#include <vector>
#include <algorithm>
#include <utility>
#include <cmath>
#include <set>
#include <sstream>
#include <map>
using namespace std;

#define mp make_pair
#define pb push_back
#define sz(a) int((a).size())
#define forn(i, n) for (int i=0; i<(n); ++i)

typedef long long ll;
typedef long double ld;
typedef pair<int,int> pii;

const int maxn = 128;

int a[2][maxn][maxn];


int main()
{
  freopen("c.in", "r", stdin);
  freopen("c.out", "w", stdout);

  int tc;
  scanf("%d", &tc);

  for (int tt=1; tt<=tc; ++tt)
  {
    printf("Case #%d:", tt);

    int r; scanf("%d", &r);

    forn (i, maxn) forn (j, maxn) a[0][i][j] = 0;
    int n = 0, m = 0;

    forn (i, r)
    {
      int x1, y1, x2, y2;
      scanf("%d %d %d %d", &y1, &x1, &y2, &x2);

      for (int x=x1-1; x<x2; ++x)
        for (int y=y1-1; y<y2; ++y)
          a[0][x][y] = 1;
      if (n < x2) n = x2;
      if (m < y2) m = y2;

    }

    int res = 0;
    int z = 0;

    for (;;++res)
    {
      int c = 0;
      forn (i, n) forn (j, m) c+=a[z][i][j];
//      forn (i, n) { forn (j, m) putchar('0'+a[z][i][j]); puts(""); } puts("");
      if (!c) break;
      forn (i, n) forn (j, m) a[z^1][i][j] = 0;

      forn (i, n) forn (j, m)
      {
        int c = 0;
        if (i>0) c += a[z][i-1][j];
        if (j>0) c += a[z][i][j-1];
        if (a[z][i][j])
        {
          if (c==0) a[z^1][i][j] = 0;
          else a[z^1][i][j] = 1;         
        }
        else
        {
          if (c==2) a[z^1][i][j] = 1;
          else a[z^1][i][j] = 0;
        }
      }
      z ^= 1;
    }
    printf(" %d\n", res);

  }

  return 0;
}
