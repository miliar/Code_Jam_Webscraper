#include <stdio.h>

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T, n, k, mod;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas) {
        printf("Case #%d: ", cas);
        scanf("%d%d", &n, &k);
        mod = 1<<n;
        k %= mod;
        for (mod >>= 1; mod; mod >>= 1) if (!(mod&k)) break;
        if (mod) puts("OFF");
        else puts("ON");
    }
    return 0;
}
