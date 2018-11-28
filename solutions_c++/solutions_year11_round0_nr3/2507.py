#include <stdio.h>
int i,j,n,t,mn,k,jami,a;
int main()
{
freopen("C-large.in","r",stdin);
freopen("C-large.out","w",stdout);
scanf("%d",&t);
for(i=1;i<=t;i++)
   {
   printf("Case #%d: ",i);
   n = 0;
   jami = 0;
   scanf("%d",&k);
   mn = 1000000000;
   for(j=0;j<k;j++)
      {
      scanf("%d",&a);
      n ^= a;
      jami += a;
      if(a < mn) mn = a;
      }
   if(!n)
      printf("%d\n",jami-mn);
   else
      printf("NO\n");
   }
return 0;
}
