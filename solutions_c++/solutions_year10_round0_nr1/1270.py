#include <stdio.h>
#include <stdlib.h>
int pow2[50];
int t,n,k;
main()
{
 freopen("A-large.in","r",stdin);
 freopen("A-large.out","w",stdout);
  pow2[1]=2;
  for(int i=2;i<=30;i++)
  {
   pow2[i]=pow2[i-1]*2;
  }
  scanf("%d",&t);
  for(int i=1;i<=t;i++)
  {
   scanf("%d%d",&n,&k);
   printf("Case #%d: ",i);
   if(k%pow2[n]==(pow2[n]-1))
   {
    printf("ON\n");
   }
   else
   {
    printf("OFF\n");
   }
  }
 return 0;
}
