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

const int maxn = 10;
const int inf = (int)1e9;

int n;
int a[maxn + 1][1 << maxn];
int f[maxn + 1][maxn + 1][1 << maxn];

int main()
{
  int tn;
  scanf("%d", &tn);
  for (int tt = 1; tt <= tn; tt++)
  {
    fprintf(stderr, "%d\n", tt);
    scanf("%d", &n);
    for (int k = n; k >= 0; k--)
      forn(i, 1 << k)
        scanf("%d", &a[k][i]);
    
    for (int h = n - 1; h >= 0; h--)
      for (int up = 0; up <= h; up++)
        for (int game = 0; game < (1 << h); game++)
        {
          int &res = f[h][up][game];
          if (h == n - 1)
          {
            int x = min(a[n][2 * game], a[n][2 * game + 1]);
            if (up + 1 + x < n)
              res = inf;
            else if (up + x >= n)
              res = 0;
            else
              res = a[h][game];
          }
          else
          {
            int f1 = f[h + 1][up][game * 2] + f[h + 1][up][game * 2 + 1];
            int f2 = f[h + 1][up + 1][game * 2] + f[h + 1][up + 1][game * 2 + 1] + a[h][game];
            res = min(inf, min(f1, f2));
          }
        }
    printf("Case #%d: %d\n", tt, f[0][0][0]);
  }
  return 0;
}
