// For my Garfield
// 27 days to our 3 years
// Round 1A 2010 -- C. Number Game
#include <cstdio>
#include <cstring>
#include <climits>

using namespace std;

int T, D, I, M, N, a[101], f[101][256];

int abs(int x)
{
  return (0 < x)? x: -x;
}

int main()
{
  freopen("B-large.in", "r", stdin);
  freopen("B-large.out", "w", stdout);
  scanf("%d", &T);
  for(int t = 1; t <= T; ++ t)
  {
    scanf("%d%d%d%d", &D, &I, &M, &N);
    for(int i = 1; i <= N; ++ i)
      scanf("%d", &a[i]);
    memset(f[0], 0, sizeof(f[0]));
    for(int i = 1; i <= N; ++ i)
      for(int j = 0; j < 256; ++ j)
      {
        f[i][j] = f[i - 1][j] + D;
        for(int k = 0; k < 256; ++ k)
        {
          int tmp = 0;
          if(abs(j - k) > M)
          {
            if(M == 0)
              tmp = INT_MAX;
            else
            if(abs(j - k) % M == 0)
              tmp = (abs(j - k) / M - 1) * I;
            else
              tmp = (abs(j - k) / M) * I;
          }
          if(tmp == INT_MAX)
            continue;
          tmp += f[i - 1][k] + abs(a[i] - j);
          if(tmp < f[i][j])
           f[i][j] = tmp;
        }        
      }
    int ans = INT_MAX;
    for(int i = 0; i < 256; ++ i)
      if(f[N][i] < ans)
        ans = f[N][i];
    printf("Case #%d: %d\n", t, ans);
  }
  return 0;
}
