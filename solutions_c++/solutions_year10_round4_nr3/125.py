// For my Garfield
// Google Code Jam Round 2 2010
// C. Bacteria
#include <iostream>
#include <algorithm>

using namespace std;

int T, R, pre, now;
bool g[2][101][101];

bool empty()
{
  for(int i = 1; i <= 100; ++ i)
    for(int j = 1; j <= 100; ++ j)
      if(g[now][i][j])
        return false;
  return true;
}

int solve()
{
  int ans = 0;
  pre = 1;
  now = 0;
  while(!empty())
  {
    ans ++;
    pre = 1 - pre;
    now = 1 - now;
    for(int i = 1; i <= 100; ++ i)
      for(int j = 1; j <= 100; ++ j)
        if(g[pre][i][j])
          g[now][i][j] = g[pre][i - 1][j] || g[pre][i][j - 1];
        else
          g[now][i][j] = g[pre][i - 1][j] && g[pre][i][j - 1];
  }
  return ans;
}

int main()
{
  freopen("C-small-attempt1.in", "r", stdin);
  freopen("C-small-attempt1.out", "w", stdout);
  cin >> T;
  for(int t = 1; t <= T; ++ t)
  {
    memset(g, 0, sizeof(g));
    cin >> R;
    for(int i = 1; i <= R; ++ i)
    {
      int x1, y1, x2, y2;
      cin >> x1 >> y1 >> x2 >> y2;
      for(int x = x1; x <= x2; ++ x)
        for(int y = y1; y <= y2; ++ y)
          g[0][x][y] = 1;
    }
    cout << "Case #" << t << ": " << solve() << endl;
  }
  return 0;
}
