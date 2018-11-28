#include "stdio.h"
#include "math.h"
#include "string.h"

int main(void){
   freopen("al.in","r",stdin);
   freopen("al.out","w",stdout);
   int t;
   int n,k;
   scanf("%d",&t);
   bool answer[t];
   for(int i=0;i<t;i++){
      scanf("%d %d",&n,&k);
      int tmp=1;
      for(int z=0;z<n;z++)tmp*=2;
      if(k%tmp==tmp-1)answer[i]=true;
      else answer[i]=false;
   }
   for(int i=0;i<t;i++){
      if(answer[i]) printf("Case #%d: ON\n",i+1);
      else printf("Case #%d: OFF\n",i+1);
   }
   return 0;
}
