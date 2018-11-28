#include <stdio.h>
#include <stdlib.h>
int A[1001];
int mins;
int sums;
int xo;
int t,n;
main()
{
 freopen("C-large.in","r",stdin);
 freopen("C-large.out","w",stdout);
 scanf("%d",&t);
 for(int i=1;i<=t;i++)
 {
  scanf("%d",&n);
  xo=0;
  sums=0;
  mins=2000000000;
  for(int j=1;j<=n;j++)
  {
   scanf("%d",&A[i]);
   sums+=A[i];
   xo=(xo^A[i]);
   if(A[i]<mins){mins=A[i];}
  }
  printf("Case #%d: ",i);
  if(xo!=0){printf("NO\n");}
  else{printf("%d\n",sums-mins);}
 }
 return 0;
}
