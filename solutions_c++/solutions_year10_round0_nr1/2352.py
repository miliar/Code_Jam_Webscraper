#include <stdio.h>

int main() {
    long i;
    long last;
    long t;
    long long n,k;
    scanf("%ld", &t);

    for (i=1;i<=t;i++) {
        scanf("%lld %lld",&n,&k);
        while (n) {
            if (k%2==0)
                break;
            k /= 2;
            n--;
        }
        if (n!=0)
            printf("Case #%ld: OFF\n",i);
        else
            printf("Case #%ld: ON\n",i);
    }
}
