#include <stdio.h>
#include <string.h>
#include <math.h>

int G[1000][1000];

int g(int h, int w)
{
  if (h < 0 || w < 0) return 0;

  if (G[h][w] != -1)
    return G[h][w];

  int a = g(h-2,w-1);
  int b = g(h-1,w-2);

  a = (a+b)%10007;
  G[h][w] = a;

  return a;
}

int main()
{
  int cs, N, H, W, R, i ,j;

  scanf("%d", &N);

  for (cs=1; cs<=N; cs++)
  {
    memset(G, -1, sizeof(G));
    scanf("%d %d %d", &H, &W, &R);
    H--; W--;
    G[0][0] = 1;

    for (int t=0;t<R;t++)
    {
      scanf("%d %d", &i, &j);
      i--; j--;
      //printf("removing: %d %d\n", i, j);
      G[H-i][W-j] = 0;
    }
    
    int ans = g(H,W);

    printf("Case #%d: %d\n", cs, ans);
  }

  return 0;
}
