#include<iostream>
#include<vector>
#include<map>
using namespace std ;
typedef pair<int,int> P ;
#define x first
#define y second

inline bool check(P p,P r1,P r2)
{
 if(p.x >= r1.x && p.x <= r2.x && p.y >= r1.y && p.y <= r2.y) 
  return true ;
 return false ;
}

long long det(P A, P B) { return 1LL*A.x*B.y - 1LL*A.y*B.x ; }
long long area(P A, P B, P C) { return det(P(B.x-A.x,B.y-A.y),P(C.x-A.x,C.y-A.y)) ; }
bool cut(P p1,P p2,P q1,P q2)
{
 if(max(p1.x, p2.x) < min(q1.x, q2.x)) return false ;
 if(max(p1.y, p2.y) < min(q1.y, q2.y)) return false ;
 if(min(p1.x, p2.x) > max(q1.x, q2.x)) return false ;
 if(min(p1.y, p2.y) > max(q1.y, q2.y)) return false ;
 long long a1 = area(p1, p2, q1) ;
 long long a2 = area(p1, p2, q2) ;
 long long b1 = area(q1, q2, p1) ;
 long long b2 = area(q1, q2, p2) ;
 if( a1 > 0 && a2 > 0 ) return false ;
 if( a1 < 0 && a2 < 0 ) return false ;
 if( b1 > 0 && b2 > 0 ) return false ;
 if( b1 < 0 && b2 < 0 ) return false ;
 return true ;
}


#define MAXN 502
int n,k,m ;
P lineS[MAXN][MAXN],lineE[MAXN][MAXN] ;
int g[MAXN][MAXN] ;

int valid[1<<16],memo[1<<16] ;

int solve(int mask)
{
 if(mask == 0) return 0 ;
 if(memo[mask] != -1) return memo[mask] ;
 int i,j,ret = 100 ;
 for(i=mask;i;i=(i-1)&mask) if(valid[i])
  ret = min(ret,1 + solve(mask^i)) ;
 return memo[mask] = ret ;
}

main()
{
 int i,j,k,runs ;

 freopen("in.txt","r",stdin) ;
 freopen("out.txt","w",stdout) ;
 scanf("%d",&runs) ;
 for(int t=1;t<=runs;t++)
 {
  scanf("%d%d",&n,&k) ;
  for(i=0;i<n;i++)
   for(j=0;j<k;j++)
   {
    lineS[i][j].x = j ;
    scanf("%d",&lineS[i][j].y) ;
    if(j > 0) lineE[i][j-1] = lineS[i][j]; 
   }
/*
 for(i=0;i<n;i++,cout << endl)
  for(j=0;j+1<k;j++)
   cout << lineS[i][j].x << " " << lineS[i][j].y << "  " << lineE[i][j].x << " " << lineE[i][j].y << endl ;
*/
  memset(g,0,sizeof g) ;
  for(i=0;i<n;i++)
   for(j=0;j<n;j++)
    for(int ii=0;ii+1<k;ii++)
     for(int jj=0;jj+1<k;jj++)
      if(cut(lineS[i][ii],lineE[i][ii],lineS[j][jj],lineE[j][jj]))
       g[i][j] = 1 ;
/*  
  for(i=0;i<n;i++,cout << endl)
   for(j=0;j<n;j++)
    cout << g[i][j] << " " ;
*/
  valid[0] = 1 ;
  for(i=1;i<1<<n;i++)
  {
   bool val = true ;
   for(j=0;j<n;j++) if(i&1<<j)
    for(k=j+1;k<n;k++) if(i&1<<k)
     if(g[j][k]) val = false ;
   if(val) valid[i] = 1 ;
   else valid[i] = 0 ;
  }
  memset(memo,255,sizeof memo) ;
  int ret = solve((1<<n)-1) ;
  printf("Case #%d: %d\n",t,ret) ;
 }
// while(1) ;
}
