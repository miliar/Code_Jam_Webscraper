#include<stdio.h>
int main()
{
 int runs ;
 scanf("%d",&runs) ;
 for(int t = 1;t <= runs;t++)
 {
  #define MAXN 1002
  int n,a[MAXN] ;
  scanf("%d",&n) ;
  for(int i = 0;i < n;i++) scanf("%d",&a[i]) ;
  int mn = a[0],sum = 0,all = 0 ;
  for(int i = 0;i < n;i++) { if(a[i] < mn) mn = a[i] ; sum += a[i] ; all ^= a[i] ; }
  if(all != 0) printf("Case #%d: NO\n",t) ;
  else printf("Case #%d: %d\n",t,sum - mn) ;
 }
 return 0 ;
}
