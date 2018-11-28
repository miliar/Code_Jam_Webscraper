#include <stdio.h>
int it,t,a,b,k;
int main()
{
freopen("A-large.in","r",stdin);
freopen("A-large.out","w",stdout);
scanf("%d",&t);
for(it=1;it<=t;it++)
   {
   printf("Case #%d: ",it);
   scanf("%d %d",&a,&b);
   k=(1<<a)-1;
   if( (b+1) % (1<<a) )
      printf("OFF\n");
   else
      printf("ON\n");
   }
return 0;
}
