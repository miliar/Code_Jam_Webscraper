#include<iostream>
#include<cmath>
using namespace std ;
int n,x[100],y[100],r[100] ;

double solve(int a,int b)
{
 double ret = (x[a] - x[b])*(x[a] - x[b]) ;
 ret += (y[a] - y[b])*(y[a] - y[b]) ;
 return sqrt(ret) ;
}

main()
{
 int i,j,k,runs ;
 freopen("in.txt","r",stdin) ;
 freopen("out.txt","w",stdout) ;
 scanf("%d",&runs) ;
 for(int t=1;t<=runs;t++)
 {
  printf("Case #%d: ",t) ;
  scanf("%d",&n) ;
  for(i=0;i<n;i++) scanf("%d%d%d",&x[i],&y[i],&r[i]) ;
  double mxr = 0 ;
  for(i=0;i<n;i++) mxr = max(mxr,(double)r[i]) ;
  if(n < 3) { printf("%.9lf\n",(double)r[0]) ; continue ; }
  double dist = solve(0,1) + r[0] + r[1] ;
  double ret = max(dist/2,mxr) ;

  dist = solve(0,2) + r[0] + r[2] ;
  ret = min(ret,max(dist/2,mxr)) ;

  dist = solve(1,2) + r[1] + r[2] ;
  ret = min(ret,max(dist/2,mxr)) ;
   
  printf("%.9lf\n",ret) ;
 }
// while(1) ;
}
