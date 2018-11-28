#include <cstdio>
#include <cstring>

//y,x!!
const int MOVE[][2] = { {-2,-1}, {-1,-2} };
const int MAXN=105;
const int MOD=10007;

bool rock[MAXN][MAXN];
int dp[MAXN][MAXN];

int main()
{
  int tt;
  scanf("%d", &tt);
  for(int t=1;t<=tt;t++) {
    int n,m,r;
    scanf("%d%d%d", &n, &m, &r);
    memset(rock,0,sizeof(rock));
    memset(dp,0,sizeof(dp));
    for(int i=0;i<r;i++) {
      int r,c;
      scanf("%d%d", &r, &c);
      rock[r-1][c-1]=1;
    }
    
    dp[0][0]=1;
    for(int x=1;x<m;x++)
      for(int y=0;y<n;y++) {
	for(int i=0;i<2;i++) {
	  int py=y+MOVE[i][0], px=x+MOVE[i][1];
	  if(py<0 || px<0) continue;
	  if(rock[py][px]) continue;
	  dp[y][x] = (dp[y][x]+dp[py][px])%MOD;
	}
      }
    printf("Case #%d: ", t);
    printf("%d\n", dp[n-1][m-1]);
  }
  return 0;
}
