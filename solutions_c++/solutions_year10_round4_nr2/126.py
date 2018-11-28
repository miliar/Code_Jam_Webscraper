// For my Garfield
// Google Code Jam Round 2 2010
// B.World Cup 2010
#include <iostream>
#include <algorithm>

using namespace std;

int T, P, M[1024], C[1024], f[1024][11];

void solve(int N, int L, int R)
{
  if(R - L <= 1)
  {
    for(int i = 0; i <= P; ++ i)
    {      
      f[N][i] = 1000000000;
      if(i + 1 <= M[L] && i + 1 <= M[R])
        f[N][i] = min(0, f[N][i]);
      if(i <= M[L] && i <= M[R])
        f[N][i] = min(C[N], f[N][i]);
    }
  }
  else
  {
    solve(N + N, L, (L + R) >> 1);
    solve(N + N + 1, ((L + R) >> 1) + 1, R);
    for(int i = 0; i <= P; ++ i)
    {
      f[N][i] = 1000000000;
      f[N][i] = min(f[N + N][i + 1] + f[N + N + 1][i + 1], f[N][i]);
      f[N][i] = min(f[N + N][i] + f[N + N + 1][i] + C[N], f[N][i]);
    }
  }
}

int main()
{
  freopen("B-large.in", "r", stdin);
  freopen("B-large.out", "w", stdout);  
  scanf("%d", &T);
  for(int t = 1; t <= T; ++ t)
  {    
    scanf("%d", &P);
    for(int i = 0; i < (1 << P); ++ i)
      scanf("%d", &M[i]);
    for(int i = P - 1; 0 <= i; -- i)
      for(int j = 0; j < (1 << i); ++ j)
        scanf("%d", &C[(1 << i) + j]);
    solve(1, 0, (1 << P) - 1);
    printf("Case #%d: %d\n", t, f[1][0]);
  }
  return 0;
}
