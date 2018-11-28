// For my Garfield
// 27 days to our 3 years
// Round 1A 2010 -- A. Rotate
#include <cstdio>

using namespace std;

int T, N, K;
char map[50][50 + 1];
char now[50][50];

bool check(int x, int y, int dx, int dy, char c)
{
  for(int i = 0; i < K; ++ i)
  {
    if(x < 0 || N <= x || y < 0 || N <= y || now[x][y] != c)
      return false;
    x += dx;
    y += dy;
  }
  return true;
}

int main()
{
  freopen("A-large.in", "r", stdin);
  freopen("A-large.out", "w", stdout);
  scanf("%d", &T);
  for(int t = 1; t <= T; ++ t)
  {
    scanf("%d%d", &N, &K);
    for(int i = 0; i < N; ++ i)
      scanf("%s", &map[i]);
    for(int i = 0; i < N; ++ i)
    {
      for(int j = 0; j < N; ++ j)
        now[i][j] = '.';
      int j = N;
      for(int k = N - 1; 0 <= k; -- k)
        if(map[i][k] != '.')
          now[i][-- j] = map[i][k];
    }
    bool red, blue;
    red = blue = false;
    int dx[8] = {00, 00, +1, -1, +1, +1, -1, -1}, 
        dy[8] = {+1, -1, 00, 00, +1, -1, +1, -1};
    for(int i = 0; i < N; ++ i)
      for(int j = 0; j < N; ++ j)
        for(int k = 0; k < 8; ++ k)          
        {
          red |= check(i, j, dx[k], dy[k], 'R');
          blue |= check(i, j, dx[k], dy[k], 'B');
        }
    printf("Case #%d: ", t);
    if(red && blue)
      printf("Both\n");
    else
    if(red)
      printf("Red\n");
    else
    if(blue)
      printf("Blue\n");
    else
      printf("Neither\n");
  }
  return 0;
}
