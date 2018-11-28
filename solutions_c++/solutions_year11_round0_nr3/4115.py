#include<stdio.h>
#define maxi 2147483647

int main(){
    int x,i,xori,mini,sum,casos,n;
    scanf("%d",&casos);
    for(i=1;i<=casos;i++){
        scanf("%d",&n);
        mini=maxi;
        xori=sum=0;
        while(n--){
            scanf("%d",&x);
            xori^=x;
            sum+=x;
            if(x<mini)mini=x;
        }
        printf("Case #%d: ",i);
        if(xori){
            printf("NO\n");
        }else{
            printf("%d\n",sum-mini);
        }
    }
    return 0;
}
