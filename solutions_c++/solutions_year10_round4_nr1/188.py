#include <cmath>
#include <algorithm>
#include <cstdio>

using namespace std;

int T, n;
int d[200][200];

bool check(int x, int y)
{
  if(1 <= x && x <= 2 * n - 1 && 1 + abs(x - n) <= y && y <= 2 * n - 1 - abs(x - n))    
    return true;
  return false;
}

int solve(int x, int y)
{
  int ans = 0;    
  for(int i = 1; i <= 2 * n - 1; ++ i)
    for(int j = 1 + abs(i - n); j <= 2 * n - 1 - abs(i - n); ++ j)
    {
      ans = max(ans, abs(i - x) + abs(j - y) + 1);
      if(check(i, y + y - j) && d[i][j] != d[i][y + y - j])
        return 1000000000;      
      if(check(x + x - i, j) && d[i][j] != d[x + x - i][j])
        return 1000000000;
    }
  return ans;
}

int main()
{
  freopen("A-large.in", "r", stdin);
  freopen("A2.out", "w", stdout);  
  scanf("%d", &T);
  for(int t = 1; t <= T; ++ t)
  {
    scanf("%d", &n);
    memset(d, -1, sizeof(d));
    for(int i = 1; i <= 2 * n - 1; ++ i)
      for(int j = 1 + abs(i - n); j <= 2 * n - 1 - abs(i - n); ++ j, ++ j)
        scanf("%d", &d[i][j]);
    int m = 1000000000;
    for(int i = 1; i <= 2 * n - 1; ++ i)
      for(int j = 1; j <= 2 * n - 1; ++ j)
        m = min(m, solve(i, j));
    printf("Case #%d: %d\n", t, m*m - n*n);
  }
  return 0;
}
