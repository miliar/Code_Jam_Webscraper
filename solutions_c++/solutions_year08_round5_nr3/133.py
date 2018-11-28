#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

int n,m;
int dp[11][1<<11];
char grid[11][11];

bool canSeat(int row, int st)
{
  for(int i=0;i<m;i++)
    if(grid[row][i]=='x' && (st>>i)&1) return 0;
  return 1;
}

bool canAfter(int first, int second)
{
  for(int i=0;i<m;i++)
    if((second>>i)&1) {
      int p=i-1;
      if(p>=0 && (first>>p)&1) return 0;
      if(p>=0 && (second>>p)&1) return 0;
      p=i+1;
      if(p<m && (first>>p)&1) return 0;
      if(p<m && (second>>p)&1) return 0;
    }
  return 1;
}

bool nei(int st)
{
  for(int i=0;i<m;i++) 
    if((st>>i)&1) {
      int p=i-1;
      if(p>=0 && (st>>p)&1) return 1;
      p=i+1;
      if(p<m && (st>>p)&1) return 1;
    }
  return 0;
}

int bits(int st)
{
  return __builtin_popcount(st);
}

int main()
{
  int tt;
  scanf("%d", &tt);
  for(int t=1;t<=tt;t++) {
    memset(dp,0,sizeof(dp));
    scanf("%d%d", &n, &m);
    for(int i=0;i<n;i++) scanf("%s", grid[i]);
    
    for(int i=0;i<(1<<m);i++)
      if(canSeat(0,i) && !nei(i))
	dp[0][i] = bits(i);
    
    for(int i=1;i<n;i++)
      for(int st=0;st<(1<<m);st++)
	if(canSeat(i,st))
	  for(int prev=0;prev<(1<<m);prev++)
	    if(canSeat(i-1,prev) && canAfter(prev,st)) {//can st be after prev?
	      dp[i][st] = max(dp[i][st], dp[i-1][prev]+bits(st));
	    }
    int res=0;
    for(int st=0;st<(1<<m);st++)
      if(canSeat(n-1,st))
	res=max(res,dp[n-1][st]);

    printf("Case #%d: ", t);
    printf("%d\n", res);    
  }

  return 0;
}
