#include <algorithm>
#include <cstdio>
#include <string>
#include <utility>
#include <vector>

using namespace std;

typedef pair<int, int> pii;

#define mp make_pair
#define pb push_back
#define x first
#define y second

#define forn(i,n) for (int i = 0, limit = (int)(n); i < limit; i++)

#define MOD 10007

int reve( int a )
{
  int p = MOD - 2;
  int res = 1;
  for (; p > 0; p >>= 1)
  {
    if (p & 1)
      res = (res * a) % MOD;
    a = (a * a) % MOD;
  }
  return res;
}

int cnk( int n, int k )
{
  int res = 1;
  for (int i = k + 1; i <= n; i++)
    res = (res * i) % MOD;
  for (int i = 1; i <= n - k; i++)
    res = (res * reve(i)) % MOD;
  return res;
}

int go( int dx, int dy )
{
  int cnt = 1;
  if (dx < 0 || dy < 0 || (dx + dy) % 3 != 0)
    cnt = 0;
  int sum = (dx + dy) / 3;
  dx -= sum, dy -= sum;
  if (dx < 0 || dy < 0)
    cnt = 0;
  else
    cnt = cnt * cnk(sum, dx);
  return cnt % MOD;
}

int main()
{
  int tests;
  scanf("%d", &tests);
  forn (test, tests)
  {
    int n, rx, ry;
    scanf("%d%d%d", &rx, &ry, &n);
    vector <pii> a;
    forn (i, n)
    {
      int x, y;
      scanf("%d%d", &x, &y);
      a.pb(mp(x - 1, y - 1));
    }
    sort(a.begin(), a.end());
    int ans = 0;
    for (int p = 0; p < (1 << n); p++)
    {
      int t = 1, tx = 0, ty = 0, cnt = 0;
      for (int j = 0; j < n; j++)
        if ((p & (1 << j)) != 0)
        {
          cnt++;
          t = (t * go(a[j].x - tx, a[j].y - ty)) % MOD;
          tx = a[j].x, ty = a[j].y;
        }
      t = (t * go(rx - 1 - tx, ry - 1 - ty)) % MOD;
      if (cnt & 1)
        t = (MOD - t) % MOD;
//       fprintf(stderr, "add: %d(%d)\n", t, (MOD - t) % MOD);
      ans = (ans + t) % MOD;
    }
    printf("Case #%d: %d\n", test + 1, ans);
    fprintf(stderr, "Case #%d complete!\n", test);
  }
  return 0;
}
