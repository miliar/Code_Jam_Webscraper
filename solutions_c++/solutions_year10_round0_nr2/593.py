#include <cstdio>
#include <algorithm>
using namespace std;

#define LLU unsigned long long
#define N 1005

LLU gcd(LLU a, LLU b) {
    return b ? gcd(b, a % b) : a;
}

int n;
LLU b[N], a[N];

bool check(LLU dis, LLU d) {
    int i;
    for (i = 1; i < n; ++i)
        if ((b[i] + dis) % d)
            return 0;
    return 1;
}

int main() {
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int t, i, cas = 0;
    LLU d, a0, ans;
    scanf("%d", &t);
    while (t--) {
        scanf("%d", &n);
        for (i = 0; i < n; ++i)
            scanf("%llu", &b[i]);
        sort(b, b + n);
        for (i = 0; i < n - 1; ++i)
            a[i] = b[i + 1] - b[i];
        d = a[0];
        for (i = 1; i < n - 1; ++i)
            d = gcd(d, a[i]);
        a0 = b[0] / d;
        if (a0 * d < b[0]) ++a0;
        for (; ; ++a0)
            if (check(a0 * d - b[0], d))
                break;
        ans = a0 * d - b[0];
        printf("Case #%d: %llu\n", ++cas, ans);
    }
    return 0;
}
