#include <cmath>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>

#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>
#include <functional>
#include <map>
#include <set>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define forit(i, a) for (__typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)
#define sz(a) (int)(a).size()
#define all(a) (a).begin(), (a).end()
#define zero(a) memset(a, 0, sizeof(a))
#define pb push_back
#define mp make_pair

typedef long long ll;
typedef vector <int> vi;
typedef pair <int, int> pii;

const int maxn = 303;

int n, cc, u[maxn][maxn];
int an[maxn], ast[maxn], a[maxn][maxn];
int bn[maxn], bst[maxn], b[maxn][maxn];

inline int Try( int x, int y, int d )
{
  if (b[y][x] != d && u[y][x] == cc)
    return 0;
  u[y][x] = cc, b[y][x] = d;
  return 1;
}

int main()
{
  int tn;
  scanf("%d", &tn);
  for (int tt = 1; tt <= tn; tt++)
  {
    fprintf(stderr, "%d\n", tt);
    scanf("%d", &n);

    int len = 0, st = 0;
    forn(i, 2 * n - 1)
    {
      if (i < n)
        len++;
      else
        st++, len--;
      forn(j, len)
        scanf("%d", &a[i][j]);
      ast[i] = st, an[i] = len;
    }

    int bad = 1, size;
    for (size = n; bad; size++)
    {
      fprintf(stderr, "size=%d\n", size);

      int len = 0, st = 0;
      forn(i, 2 * size - 1)
      {
        if (i < size)
          len++;
        else
          st++, len--;
        bn[i] = len, bst[i] = st;
      }
      forn(dx, size - n + 1)
        forn(dy, size - n + 1)
        {
          if (dx != 0 && dy != 0 && dx != size - n && dy != size - n)
            continue;

          int flag = 1;
          cc++;
          forn(i, 2 * n - 1)
            forn(j, an[i])
            {
              int y = i + dx + dy;
              int x = j + ast[i] + dx - bst[y];

              flag &= Try(x, y, a[i][j]);
              flag &= Try(x, 2 * size - y - 2, a[i][j]);
              flag &= Try(bn[y] - x - 1, y, a[i][j]);

              if (!flag)
                i = j = 2 * n;
            }
          if (flag)
            bad = 0, dx = dy = size + 1;
        }
    }

    #define F(n) ((n) * (n))
    printf("Case #%d: %d\n", tt, F(size - 1) - F(n));
  }
  return 0;
}
