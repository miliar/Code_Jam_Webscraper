#include<stdio.h>

int main(){

    int T,N,cas=0,count,in;
    scanf("%d",&T);
    while (cas++ <T) {
        count=0;
        scanf("%d ",&N);
        for(int i=0;i<N;i++){
            scanf("%d ",&in);
            if(in != (i+1)) count++;
        }
        printf("Case #%d: %d.000000\n",cas,count);
    }
    return 0;
}
