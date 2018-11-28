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

const int maxn = 103;

int n, k[maxn];
int is[maxn][maxn];

int main()
{
  int tn;
  scanf("%d", &tn);
  for (int tt = 1; tt <= tn; tt++)
  {
    fprintf(stderr, "%d\n", tt);
    scanf("%d", &n);
    memset(is, 0, sizeof(is));
    forn(i, n)
    {
      int x1, y1, x2, y2;
      scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
      for (int y = y1; y <= y2; y++)
        for (int x = x1; x <= x2; x++)
          is[y][x] = 1;
    }

    int res = 0;
    while (1)
    {
/*
      forn(i, maxn)
      {
        forn(j, maxn)
          printf("%d", is[i][j]);
        puts("");
      }
      puts("");
*/

      int good = 0;
      forn(i, maxn)
        forn(j, maxn)
          good |= is[i][j];
      if (!good)
        break;
      res++;
      for (int i = maxn - 1; i >= 0; i--)
        for (int j = maxn - 1; j >= 0; j--)
        {
          int f1 = (i && is[i - 1][j]);
          int f2 = (j && is[i][j - 1]);
          if (f1 && f2)
            is[i][j] = 1;
          else if (!f1 && !f2)
            is[i][j] = 0;
        }
    }
    printf("Case #%d: %d\n", tt, res);
  }
  return 0;
}
