#include <cstdio>

int gcd(int a, int b) {
    return (a == 0) ? b : gcd(b % a, a);
}

int main() {
    int T;
    long long n;
    int pd, pg;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%lld%d%d", &n, &pd, &pg);
        if (pg == 100 && pd != 100)
            goto broken;
        if (pg == 0 && pd != 0)
            goto broken;
        if (n <= 100 && pd != 0) {
            int x = 100 / gcd(pd, 100);
            if (n < x)
                goto broken;
        }
        printf("Case #%d: Possible\n", t);
        continue;
broken:
        printf("Case #%d: Broken\n", t);
    }
}
