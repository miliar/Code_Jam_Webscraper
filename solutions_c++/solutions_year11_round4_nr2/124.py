#include <algorithm>
#include <iostream>
#include <vector>
#include <map>
#include <cassert>
#define N 601

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned long ul;
typedef unsigned short us;
typedef unsigned char uc;

typedef ll mat[N][N];

ll sum[N][N], xsum[N][N], ysum[N][N];
ll A[N][N]; ll xA[N][N], yA[N][N];

/*ll bslow(mat A,mat sum, int x,int y,int r)
{
  ll t=0;
  for(int i=x;i<=x+r;i++) for(int j=y;j<=y+r;j++)
  { 
    if ( ( i==x||i==x+r) && ( j==y||j==y+r)) continue;
    t += A[i][j];
  }
  return t;
}*/

ll block(mat A, mat sum, int x, int y, int r)
{
  int x1 = x+r+1, x0 = x, y1 = y+r+1, y0 = y;
  ll t = sum[x1][y1] - sum[x0][y1] - sum[x1][y0] + sum[x0][y0];
  t -= A[x+r][y+r] + A[x][y+r] + A[x+r][y] + A[x][y];
//  if(t!=bslow(A,sum,x,y,r)) {printf("%d %d %d\n",x,y,r); }
  return t;
}

int valid(int x, int y, int r)
{
  ll t = block(A,sum,x,y,r), xt = block(xA,xsum,x,y,r), yt = block(yA,ysum,x,y,r);
//  ll t = bslow(A,sum,x,y,r), xt = bslow(xA,xsum,x,y,r), yt = bslow(yA,ysum,x,y,r);
  return (t*(2*x+r) == 2*xt && t*(2*y+r) == 2*yt);
}

main()
{
  int cases;
  cin >> cases;
  for(int loop=1; loop<=cases; loop++)
  {
    int r,c,d;
    cin >> r >> c >> d;
    char str[r+1][c+1];

    for(int i=0;i<r;i++) { scanf("%s",str[i]); for(int j=0;j<c;j++) A[i][j]=str[i][j]-'0'; }

    for(int i=0;i<r;i++) for(int j=0;j<c;j++) xA[i][j] = A[i][j]*i, yA[i][j] = A[i][j]*j;

    for(int i=0;i<=r;i++) for(int j=0;j<=c;j++)
    {
      if (i==0||j==0) { sum[i][j]=xsum[i][j]=ysum[i][j]=0; continue; }

      sum[i][j] = sum[i-1][j] + A[i-1][j-1];
      xsum[i][j] = xsum[i-1][j] + xA[i-1][j-1];
      ysum[i][j] = ysum[i-1][j] + yA[i-1][j-1];
    }

    for(int i=0;i<=r;i++) for(int j=0;j<=c;j++)
    {
      if (i==0 || j==0) { continue; }

      sum[i][j] += sum[i][j-1];
      xsum[i][j] += xsum[i][j-1];
      ysum[i][j] += ysum[i][j-1];
    }

    int m=0;

    for(int rad=2;rad<min(r,c);rad++)
    {
      bool good=false;
      for(int i=0;i<r-rad;i++) for(int j=0;j<c-rad;j++)
      {
        if (valid(i,j,rad)) { good=true; m=rad; break; }
      }
    }

    printf("Case #%d: ",loop);
    if (!m) puts("IMPOSSIBLE"); else printf("%d\n",m+1);
    // puts("");
  }
}
