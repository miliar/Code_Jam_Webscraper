#include <stdio.h>
#include <new>

int main(void){
    long t, r, k, n;
    long i,j;
    long grupos[1000];
    long long total = 0;
    
    scanf("%d\n",&t);
    for(i = 0;i < t;i++){
        scanf("%d %d %d\n",&r,&k,&n);
        for(j = 0;j < n;j++){
            scanf("%d",&grupos[j]);
            //printf("  %d ",grupos[j]);
        }
        //printf("\n");
        int siguiente = 0;
        int parcial = 0;
        int quedan;
        for(j = 0;j < r;j++){
            quedan = n;
            while((quedan--)&&(parcial + grupos[siguiente])<=k){
                //printf("  %d+",grupos[siguiente]);
                parcial += grupos[siguiente];
                siguiente++;
                if(siguiente == n){
                     siguiente = 0;
                }
            }
            //printf("=  %d\n",parcial);
            total += parcial;
            parcial = 0;
        }
        
        printf("Case #%d: %I64d\n",i+1,total);
        total = 0;
    }
    
    return 0;
}
