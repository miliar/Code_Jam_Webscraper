#include <cstdlib>
#include <iostream>

using namespace std;

int t,n,k;
int tab[32];
int main()
{
   tab[0]=0;
   for(int i=1;i<31;i++) tab[i]=2*tab[i-1]+1;

   scanf("%d",&t);
   for(int p=0;p<t;p++)
   {
      scanf("%d%d",&n,&k);
      if((k+1)%(tab[n]+1)==0)
         printf("Case #%d: ON\n",p+1);
      else
         printf("Case #%d: OFF\n",p+1);
   }

   return 0;
}
