#include <algorithm>
#include <cstdio>
#include <cstring>
#include <set>
#include <map>
#include <iostream>

#define inf 1e9

using namespace std;

#define maxn 20010

int type[maxn], can[maxn], dp[maxn][2];

int main( void )
{
  freopen("in.txt", "r", stdin);
  freopen("out.txt", "w", stdout);

  int tn;
  cin >> tn;
  for (int tt = 1; tt <= tn; tt++)
  {
    printf("Case #%d: ", tt);

    int m, v;
    cin >> m >> v;
    memset(dp, 63, sizeof(dp));
    for (int i = 0; i < (m - 1) / 2; i++)
      cin >> type[i] >> can[i];
    for (int i = (m - 1) / 2; i < m; i++)
    {
      int x;
      cin >> x;
      dp[i][x] = 0;
    }
    for (int i = (m - 1) / 2 - 1; i >= 0; i--)
    {
      for (int p1 = 0; p1 < 2; p1++)
        for (int p2 = 0; p2 < 2; p2++)
          if (dp[i * 2 + 1][p1] < inf && dp[i * 2 + 2][p2] < inf)
          {
            if (type[i] || can[i])
              dp[i][p1 & p2] <?= dp[i * 2 + 1][p1] + dp[i * 2 + 2][p2] + (type[i] != 1);
            if (!type[i] || can[i])
              dp[i][p1 | p2] <?= dp[i * 2 + 1][p1] + dp[i * 2 + 2][p2] + (type[i] != 0);
          }
    }
    if (dp[0][v] < inf)
      printf("%d\n", dp[0][v]);
    else
      printf("IMPOSSIBLE\n");
  }



  return 0;
}                          