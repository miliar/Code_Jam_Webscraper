#include <cstdio>
#include <cstdlib>

long long GCD(long long a, long long b) {
    while(b != 0) {
        long long tmp=b;
        b = a % b;
        a = tmp;
    }
    return a;
}

int main() {
    int C,i,cas=1,N;
    long long t,t2,gcd;

    scanf("%d", &C);
    while(C--) {
        scanf("%d", &N);
        for(i=0; i<N; i++) {
            scanf("%lld", &t2);
            if(i == 1)
                gcd = abs(t2-t);
            else if(i >= 2)
                gcd = GCD(gcd, abs(t2-t));
            t = t2;
        }
        printf("Case #%d: %lld\n", cas++, (gcd-(t2%gcd))%gcd);
    }
    return 0;
}


