#include <cstdio>
int T,N,x[1005];
int main(){
      scanf("%d",&T);
      for (int cases=1;cases<=T;cases++){
            int xx=0,min,total=0;
            scanf("%d",&N);
            for (int i=0;i<N;i++){ 
               scanf("%d",&x[i]);
               total+=x[i];
               if (min>x[i] || i==0) min=x[i];
               xx^=x[i];
            }
            if (xx) printf("Case #%d: NO\n",cases);
            else printf("Case #%d: %d\n", cases, total-min);
      }
}
