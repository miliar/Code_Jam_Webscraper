#include <cstdio>

typedef long long i64;

int main() {
    int t, c = 0;
    i64 n, k;

    for (scanf("%d", &t); t-- > 0; ) {
        scanf("%lld %lld", &n, &k);
        printf("Case #%d: %s\n", 
                ++c, (k==0 || (k%(1ll<<n) != (1ll<<n)-1) ) ? "OFF" : "ON");
    }

    return 0;
}
