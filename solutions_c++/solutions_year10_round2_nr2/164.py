#include<iostream>
#include<stdio.h>
#include<vector>
#include<string.h>
#include<sstream>
#include<algorithm>
using namespace std ;
#define MAXN 55
int n,K,B,T,x[MAXN],v[MAXN] ;

main()
{
 int i,j,k,runs ;
 cin >> runs ;
 for(int t=1;t<=runs;t++)
 {
  cin >> n >> K >> B >> T ;
  for(i=0;i<n;i++) cin >> x[i] ;
  for(i=0;i<n;i++) cin >> v[i] ;
  int ret = 0 ;
  for(i=n-1;K > 0 && i >= 0;i--) if(x[i] + v[i]*T < B) ret += K ;
  else K -- ;
  if(K > 0) printf("Case #%d: IMPOSSIBLE\n",t) ;
  else printf("Case #%d: %d\n",t,ret) ;
 }
}
