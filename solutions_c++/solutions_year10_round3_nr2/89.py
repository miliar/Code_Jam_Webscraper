#include <stdio.h>
#define LL long long

int T, l, p, c, ans;

LL exp(LL b, int p)
{
    LL ret = 1;
    for (; p; p>>=1, b=b*b)
        if (p&1) ret=ret*b;
    return ret;
}

int main()
{
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas) {
        scanf("%d%d%d", &l, &p, &c);
        for (int i = 0; i < 10; ++i)
            if (l*exp(c, exp(2, i)) >= p) {
                ans = i;
                break;
            }
        printf("Case #%d: %d\n", cas, ans);
    }
    return 0;
}
