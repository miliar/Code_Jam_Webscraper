#include <algorithm>
#include <cassert>
#include <cstdio>
#include <vector>
#include <cstring>

using namespace std;

typedef pair <double, double> pnt;
#define x first
#define y second

typedef long long ll;

#define maxn 550

int f[maxn][maxn], dp[maxn][maxn], a[maxn][maxn], g[maxn][maxn / 32], nn, n, m;
vector <int> ne[maxn];

int cnt[0xFFFF];

int get (int x, int y, int z) { 
/*  int res = 0;
  for (int i = 0; i < n; i++) {
    res += a[z][i] && !a[x][i] && !a[y][i];
  }

  */
  int res2 = 0;
  for (int i = 0; i < nn; i++) {
    int t = g[z][i] & ~g[x][i] & ~g[y][i];
    res2 += cnt[(t >> 16) & 0xFFFF] + cnt[t & 0xFFFF];
  }
//  assert (res2 == res);
  return res2;

//  return res;
}

int main (void) {

  for (int i = 1; i <= 0xFFFF; i++) {
    cnt[i] = cnt[i & (i - 1)] + 1;
  }
  int tn;
  scanf ("%d", &tn);
  for (int tt = 1; tt <= tn; tt++) {
    printf ("Case #%d: ", tt);
    scanf ("%d%d", &n, &m);

    nn = (n + 31) / 32 + 2;

    memset (a, 0, sizeof (a));
    memset (f, 63, sizeof (f));
    memset (g, 0, sizeof (g));
    for (int i = 0; i < m; i++) {
      int x, y;
      scanf ("%d,%d", &x, &y);
      f[x][y] = f[y][x] = 1;
      a[x][y] = a[y][x] = 1;
      ne[x].push_back(y);
      ne[y].push_back(x);

      g[x][y / 32] |= 1 << (y % 32);
      g[y][x / 32] |= 1 << (x % 32);
    }
    for (int i = 0; i < n; i++) {
      sort (ne[i].begin(), ne[i].end());
      f[i][i] = 0;
      a[i][i] = 1;
      g[i][i / 32] |= 1 << (i % 32);
    }
    for (int i = 0; i < n; i++) {
      for (int s = 0; s < n; s++) {
        for (int t = 0; t < n; t++) {
          f[s][t] = min (f[s][t], f[s][i] + f[i][t]);
        }
      }
    }

    vector <int> v[maxn];
    int d = f[0][1];
    for (int i = 0; i < n; i++) {
      if (f[0][i] + f[i][1] == d) {
        v[f[0][i] + 1].push_back(i);
      }
    }
    v[0].push_back(0);

    memset (dp, 0, sizeof (dp));
    int res = 0;
    dp[0][0] = ne[0].size() + 1;
    if (d == 1) {
      res = dp[0][0];
    }
    for (int i = 0; i < d - 1; i++) {
      for (int tx = 0; tx < (int)v[i].size(); tx++) {
        for (int ty = 0; ty < (int)v[i + 1].size(); ty++) {
          int x = v[i][tx], y = v[i + 1][ty];
          if (a[x][y]) {
//            fprintf (stderr, "i = %d, [%d--%d]\n", i, x, y);
            for (int tz = 0; tz < ne[y].size(); tz++) {
              int z = ne[y][tz];
              if (f[0][z] + f[z][1] == d) {
                int ch = get (x, y, z) + dp[x][y];
                if (i + 1 == d - 1 && res < ch) {
                  res = ch;
                }
                if (dp[y][z] < ch) {
                  dp[y][z] = ch;
  //                fprintf (stderr, "[%d %d] : %d\n", y, z, ch);
                }

              }
            }
          }
        }
      }
    }

    printf ("%d %d\n", d - 1, res - d);

    for (int i = 0; i < n; i++) {
      ne[i].clear();
    }
  }
  return 0;
}