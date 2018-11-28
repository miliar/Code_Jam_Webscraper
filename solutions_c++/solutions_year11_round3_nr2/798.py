#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;
long long k, l, t, n, c, a[1010], s[1010], tmp, ans, v;
bool p[1010], gf;
long long calc(int x, int y = -1)
{
  long long v = -1;
  if (2 * s[x - 1] > t)
    v = a[x - 1];
  else if (2 * s[x] > t)
    v = a[x - 1] - (t / 2 - s[x - 1]);
  if (v == -1)
    gf = true;
  if (!gf && y != -1)
    v += a[y - 1];
  return 2 * s[n] - v;
}
int main()
{
  freopen("B.in","r",stdin);
  freopen("output.txt","w",stdout);
  cin >> k;
  for(int q = 0; q < k; q++)
  {
    cin >> l >> t >> n >> c;
    for(int i = 0; i < c; i++)
      cin >> a[i];
    for(int i = c; i < n; i++)
      a[i] = a[i % c];
    for(int i = 1; i <= n; i++)
      s[i] = s[i - 1] + a[i - 1];
    ans = 0;
    for(int i = 0; i < n; i++)
      ans += 2 * a[i];
    if (l == 1)
    {
      for(int i = 1; i <= n; i++)
      {
        gf = false;
        tmp = calc(i);
        if (!gf && ans == -1)
          ans = tmp;
        else if (!gf)
          ans = min(ans, tmp);
      }
    }
    else if (l == 2)
    {
      for(int i = 1; i <= n; i++)
        for(int j = i + 1; j <= n; j++)
        {
          gf = false;
          tmp = calc(i, j);
          if (!gf && ans == -1)
            ans = tmp;
          else if (!gf)
            ans = min(ans, tmp);
        }
    }
    printf("Case #%d: %I64d\n", q + 1, ans);
  }
  return 0;
}
