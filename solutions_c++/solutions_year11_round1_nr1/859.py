#include <iostream>
#include <cstdio>
using namespace std;
#define LL long long
LL gcd(LL a, LL b)
{
    return b == 0 ? a : gcd(b, a % b);
}
int main()
{
    LL t, n, d, g, a, b, con = 1, gec;
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%lld", &t);
    while(t--) {
        scanf("%lld %lld %lld", &n, &d, &g);
        gec = gcd(d, 100);
        a = d / gec;
        b = 100 / gec;
        printf("Case #%d: ", con++);
        if(b <= n) {
            if(g == 100) {
                if(d == 100)
                    printf("Possible\n");
                else printf("Broken\n");
            } else if(g == 0) {
                if(d == 0)
                    printf("Possible\n");
                else
                    printf("Broken\n");
            } else printf("Possible\n");
        } else printf("Broken\n");
    }
    return 0;
}
