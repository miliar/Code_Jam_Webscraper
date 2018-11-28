#include<iostream>
using namespace std ;
#define MAXN 50
int c,n,vis[MAXN] ;
long long ncr[MAXN][MAXN] ;
double memo[MAXN] ;

double solve(int mask)
{
 if(mask == n) return 0 ;
 if(vis[mask]) return memo[mask] ;
 vis[mask] = true ;
 int i ;
 long long sub = ncr[mask][c],total = ncr[n][c] ;
 double ret = 0 ;
 
 for(i=1;i<=c&&mask+i<=n;i++)
  ret += ncr[mask][c-i]*ncr[n-mask][i]*solve(mask+i) ;
 double den = (1 - 1.*sub/total) ;
 double num = 1 + ret/total ;
 return memo[mask] = num/den ; 
}

main()
{
 int i,j,k,runs ;
 
 ncr[0][0] = 1 ;
 for(i=1;i<MAXN;i++)
 {
  ncr[i][0] = ncr[i][i] = 1 ;
  for(j=1;j<i;j++) ncr[i][j] = ncr[i-1][j] + ncr[i-1][j-1] ;
 }
 
 freopen("in.in","r",stdin) ;
 freopen("out.txt","w",stdout) ;
 scanf("%d",&runs) ;
 for(int t=1;t<=runs;t++)
 {
  scanf("%d%d",&n,&c) ;
  double ret ;
  memset(vis,0,sizeof vis) ;
  if(n <= c) ret = 1 ;
  else ret = solve(0) ;
  printf("Case #%d: %.9lf\n",t,ret) ;
 }
// while(1) ;     
}
