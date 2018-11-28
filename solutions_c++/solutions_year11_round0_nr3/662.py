#include<stdio.h>
#include<stdlib.h>
int num[10000];
int main (){
    int MIN,T,sum,xorsum,ca=0,n,i;
    scanf("%d",&T);
    while(T--){
        scanf("%d",&n);
        sum = 0;
        xorsum = 0;
        MIN = 100000000;
        for(i=0;i<n;i++){
            scanf("%d",&num[i]);
            if(num[i] < MIN)
                MIN = num[i];
            sum += num[i];
            xorsum = (xorsum ^ num[i]);
        }
        ca++;
        if(xorsum == 0)
            printf("Case #%d: %d\n",ca,sum - MIN);
        else
            printf("Case #%d: NO\n",ca);

    }
    return 0;
}
/*
2
5
1 2 3 4 5
3
3 5 6
*/
