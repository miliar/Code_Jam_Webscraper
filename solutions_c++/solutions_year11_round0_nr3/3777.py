#include<stdio.h>

int candy[1001];

int main(){
    int T,N,cnt,min,sum,test;
    scanf("%d",&T);
    cnt = 0;
    while(T--){
        cnt++;
        scanf("%d",&N);
        for(int i=0;i<N;i++)
            scanf("%d",&candy[i]);
        min = 1000001;
        sum = test = 0;
        for(int i=0;i<N;i++){
            if(candy[i] < min) min = candy[i];
            sum += candy[i];
            test = test ^ candy[i];
        }
        
        if(test) printf("Case #%d: NO\n",cnt);
        else printf("Case #%d: %d\n",cnt,sum - min);
    }
    return 0;
}
