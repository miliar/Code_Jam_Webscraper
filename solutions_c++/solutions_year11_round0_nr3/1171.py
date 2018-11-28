#include<stdio.h>

int main(){

    int T,N,cas=0;
    long s,min,v,sum;
    scanf("%d",&T);
    while (cas++ <T) {
        scanf("%d",&N);
        s=sum=0;
        min=9999990;
        for(int i=0;i<N;i++){
            scanf("%ld ",&v);
//            printf("%ld",v);
            s ^=v;
            sum +=v;
            if(v < min) min = v;
        }
        if(s != 0){
            printf("Case #%d: NO\n",cas);
        }
        else {
            printf("Case #%d: %ld\n",cas,sum-min);
        }
    }
    return 0;
}
