#include <cstdio>

using namespace std;

long long gcd(long long a, long long b)
{
    long long t;

    while (b) {
        t = a % b;
        a = b;
        b = t;
    }
    return a;
}

long long lcm(long long a, long long b)
{
    long long t = gcd(a, b);
    return a / t * b;
}

int main()
{
    int cn, cns;

    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);

    scanf("%d", &cns);
    for (cn = 0; cn < cns; cn++) {
        long long n, x, y;
        scanf("%lld%lld%lld", &n, &x, &y);
        long long t1 = gcd(x, 100);
        //long long t2 = gcd(y, 100);
        //long long t = lcm(100 / t1, 100 / t2);
        printf("Case #%d: ", cn + 1);
        long long a = 100 / t1;
        if (n >= a && (y != 100 || x == 100) && (y != 0 || x == 0)) {
            printf("Possible\n");
        } else {
            printf("Broken\n");
        }

    }
    return 0;
}
