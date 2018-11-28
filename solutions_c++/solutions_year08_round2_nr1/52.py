#include<cstdio>
#include<iostream>
#include<vector>
#include<string>
#include<queue>
#include<map>
#include<stack>
#include<algorithm>
#include<cmath>
#include<sstream>
#include<set>
#include<bitset>

using namespace std ;
#define INF (int)1e9 
typedef pair<int,int> P ;

long long n,X[1000000],Y[1000000] ;

int grp[3][3] ;
long long memo[100005][4][4][4] ;

long long solve()
{
 int i,j,k,taken ; 
 for(i=0;i<3;i++)
  for(j=0;j<3;j++)
   for(k=0;k<3;k++)
    memo[n][i][j][k] = 0 ;
  
  memo[n][0][0][3] = 1 ;
 
 for(i=0;i<n;i++)
  for(j=0;j<3;j++)
   for(k=0;k<3;k++)
   {
    memo[i][j][k][3] = 0 ;              
   }
 
 for(i=0;i<n;i++)
  memo[i][0][0][3] = 1 ;
 
 for(k=n-1;k>=0;k--)
  for(int x=0;x<3;x++)
   for(int y=0;y<3;y++)
    for(taken=0;taken<3;taken++)
    {
     long long ret1 = memo[k+1][x][y][taken] ;
     long long ret2 = memo[k+1][(x+(X[k]%3))%3][(y+(Y[k]%3))%3][taken+1] ;
     memo[k][x][y][taken] = ret1 + ret2 ;                  
    }
 return memo[0][0][0][0] ;
}
main()
{
 int i,j,k,runs ;
 
 freopen("a.in","r",stdin) ;
 freopen("out.txt","w",stdout) ;
 
 cin >> runs ;
 for(int t=1;t<=runs;t++)
 {
  long long A,B,C,D,x0,y0,M ;
  cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M ;
  
  X[0] = x0 ;
  Y[0] = y0 ;
  
  long long xx = x0,yy = y0 ;
  for(i=1;i<n;i++)
  {
   xx = (A*xx + B)%M ;
   yy = (C*yy + D)%M ;
   X[i] = xx%3 ;
   Y[i] = yy%3 ;
  }
  
  memset(memo,0,sizeof memo) ;
  long long ret = solve() ;
  printf("Case #%d: %lld\n",t,ret) ;
 }
 
 
// while(1) ;     
}
