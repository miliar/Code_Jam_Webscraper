#include<stdio.h>
int main()
{
 int runs,n,a[1002] ;
 scanf("%d",&runs) ;
 for(int t = 1;t <= runs;t++) 
 {
  scanf("%d",&n) ; 
  int ret = n ;
  for(int i = 0;i < n;i++) scanf("%d",&a[i]) ;
  for(int i = 0;i < n;i++) if(a[i] == i + 1) ret-- ;
  printf("Case #%d: %d.000000\n",t,ret) ;
 }
 return 0 ;
}
