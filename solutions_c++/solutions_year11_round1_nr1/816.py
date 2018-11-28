#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int gcd(int a, int b) {
    int t;
    while ( a > 0 ) {
        b %= a;
        t = a;
        a = b;
        b = t;
    }
    return b;
}

int main()
{
    long long n;
    int pd, pg;
    int aa, nn, c;
    scanf("%d",&nn);
    for ( aa = 1; aa <= nn; ++aa ) {
        scanf("%lld %d %d",&n,&pd,&pg);
        printf("Case #%d: ",aa);
        if ( pd < 100 && pg == 100 ) {
            printf("Broken\n");
            continue;
        }
        if ( pd > 0 && pg == 0 ) {
            printf("Broken\n");
            continue;
        }
        c = gcd(pd,100);
        if ( 100/c > n ) printf("Broken\n");
        else printf("Possible\n");
    }
    return 0;
}
