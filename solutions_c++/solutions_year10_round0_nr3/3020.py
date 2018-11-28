#include "stdio.h"
#include "math.h"
#include "string.h"

int main(void){
   freopen("c.in","r",stdin);
   freopen("c.out","w",stdout);
   int t;
   int r,n,k;
   scanf("%d",&t);
   int answer[t];
   for(int i=0;i<t;i++){
      answer[i]=0;
      scanf("%d %d %d",&r,&k,&n);
      int g[n],sumpeople=0;
      for(int j=0;j<n;j++){
         scanf("%d",&g[j]);
         sumpeople+=g[j];
      }

      int z=0;
      for(int j=0;j<r;j++){
         int tmp=k;
         if(sumpeople<k){
            answer[i]+=sumpeople;
         }
         else{
            while(true){
               if(tmp-g[z%n]<0)break;
               else{
                  tmp-=g[z%n];
                  answer[i]+=g[z%n];
                  z++;
               }
            }
         }
      }

   }
   for(int i=0;i<t;i++){
      printf("Case #%d: %d\n",i+1,answer[i]);
   }
   return 0;
}
