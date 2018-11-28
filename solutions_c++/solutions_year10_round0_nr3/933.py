// For my Garfield
// 41 days to our 3 years
// C. Theme Park
// Google Code Jam Qualification Round 2010
#include <cstdio>
using namespace std;
int T, R, k, N, g[1000], p[1000];
long long s[1000];
int main()
{
  freopen("C-large.in", "r", stdin);
  freopen("C-large.out", "w", stdout);
  scanf("%d", &T);
  for(int t = 1; t <= T; ++ t)
  {
    scanf("%d%d%d", &R, &k, &N);
    long long sum = 0;
    for(int i = 0; i < N; ++ i)
    {
      scanf("%d", &g[i]);
      sum += g[i];
    }
    if(sum <= k)
      printf("Case #%d: %lld\n", t, sum * R);
    else
    {
      for(int i = 0; i < N; ++ i)
      {
        s[i] = 0;
        p[i] = i;
        while(s[i] + g[p[i]] <= k)
        {
          s[i] += g[p[i]];
          p[i] = (p[i] + 1) % N;
        }
      }
      int now = 0;
      long long ans = 0;
      for(int i = 0; i < R; ++ i)
      {
        ans += s[now];
        now = p[now];
      }
      printf("Case #%d: %lld\n", t, ans);
    }
  }
  return 0;
}
