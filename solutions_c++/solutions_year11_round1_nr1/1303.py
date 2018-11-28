#include <stdio.h>
#include <string>
#include <algorithm>
#include <vector>
#include <string>
using namespace std;
int main(){
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
   long n,i,j;
   long test,order,pd,pg;
   scanf("%ld",&test);
   for(order=1;order<=test;order++){
       scanf("%ld%ld%ld",&n,&pd,&pg);
       printf("Case #%ld: ",order);
       if((pd<100&&pg==100)||(pd>0&&pg==0)){
           printf("Broken\n");
           continue;
       }
       for(i=1;i<=n;i++){           //the zero must be processd
           for(j=1;j<=i;j++)
               if(j*100.0/i==pd)
                   break;
           if(j<=i)
               break;
       }
       if(i<=n||pd==0)
           printf("Possible\n");
       else
           printf("Broken\n");
   }
   return 0;
}
