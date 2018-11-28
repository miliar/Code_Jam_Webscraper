#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;

const int maxn = 2000005;
int pow[10];
int mexp[maxn], sum[maxn];
long long ans;

void prepare(int n) {
    int i, j, t, l;
    for (i = 1, pow[0] = 1; i < 10; ++i) pow[i] = pow[i - 1] * 10;
    for (i = 1; i <= n; ++i) {
        mexp[i] = i;
        for (t = i, l = 0; t > 0; t /= 10, ++l);
        for (j = 1; j < l; ++j) {
            t = i / pow[j] + (i % pow[j]) * pow[l - j];
            if (t < mexp[i]) mexp[i] = t;
        }
    }
}

int main() {
    freopen("C-large.in", "r", stdin);
    freopen("b-large.out", "w", stdout);
    int testi, test, i, a, b;
    prepare(2000000);
    scanf("%d", &test);
    for (testi = 1; testi <= test; ++testi) {
        scanf("%d%d", &a, &b);
        memset(sum, 0, sizeof sum);
        for (i = a; i <= b; ++i)
            ++sum[mexp[i]];
        ans = 0;
        printf("Case #%d: ", testi);
        for (i = 1; i <= b; ++i)
            ans += (long long)sum[i] * (sum[i] - 1) / 2;
        printf("%I64d\n", ans);
    }
    fclose(stdout);
    return 0;
}
    
    
