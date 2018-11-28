#include <stdio.h>

long long gcd(long long a,long long b) {
    if(!a || !b) return a+b;
    while((a%=b) && (b%=a));
    return a+b;
}

int main() {
    int tt,TT;
    long long N,pD,pG;
    scanf("%d",&TT);
    for( tt=0; tt<TT; tt++ ) {
        scanf("%lld %lld %lld",&N,&pD,&pG);
        if(N<100/gcd(100,pD) || (pD!=100 && pG==100) || (pD!=0 && pG==0)) {
            printf("Case #%d: Broken\n",tt+1);
        }else {
            printf("Case #%d: Possible\n",tt+1);
        }
    }
    return 0;
}

