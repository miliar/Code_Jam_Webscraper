#include <stdio.h>

int main(){
    
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int N, T, temp, sum, inf, XOR;
    scanf("%d", &N);
    for(int i=1; i<=N; i++){
        scanf("%d", &T);    
        XOR = 0;
        inf = 1000000;
        sum = 0;
        for(int j=0; j<T; j++){
            scanf("%d", &temp);
            sum += temp;    
            if(temp<inf) inf = temp;
            XOR = XOR ^ temp;   
        }
        if(XOR==0) printf("Case #%d: %d\n", i, sum-inf);
        else printf("Case #%d: NO\n", i);    
    }
    return 0;
}
