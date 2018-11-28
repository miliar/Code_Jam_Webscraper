#include<stdio.h>
long long Gcd(long long x,long long y){
    if(y)while((x%=y)&&(y%=x));
    return x+y;
}
main(){
    long long N,g;
    int T,pD,pG,p,q,t=0;
    scanf("%d",&T);
    while(T--){
        t++;
        scanf("%lld%d%d",&N,&pD,&pG);
        printf("Case #%d: ",t);
        p=100;
        q=pD;
        g=Gcd(p,q);
        p/=g;
        q/=g;
        if(p>N)puts("Broken");
        else{
            if(pG==100){
                if(pD!=100){
                    puts("Broken");
                    continue;
                }
            }
            else if(pG==0){
                if(pD!=0){
                    puts("Broken");
                    continue;
                }
            }
            puts("Possible");
        }
    }
}
