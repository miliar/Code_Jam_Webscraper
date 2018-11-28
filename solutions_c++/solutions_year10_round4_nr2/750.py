#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

#define N 100005

int a[N], b[N], c[N], f[N];

bool cmp(int l, int r) {
    return a[l] > a[r];
}

int main() {
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-attempt0.out", "w", stdout);
    int t, i, p, n, cn, cnt, ans, cas = 0, j, x;
    scanf("%d", &t);
    while (t--) {
        scanf("%d", &p);
        n = 1 << p;
        for (i = 0; i < n; ++i) {
            scanf("%d", &a[i]);
            a[i] = max(0, p - a[i]);
        }
        for (i = 0; i < n - 1; ++i)
            scanf("%d", &x);
        for (i = 0; i < n; ++i)
            b[i] = i;
        sort(b, b + n, cmp);
        memset(f, 0, sizeof(f));
        ans = 0;
        for (i = 0; i < n; ++i) {
            cn = 0; cnt = 0;
            for (j = b[i] + n; j; j /= 2) {
                c[cn++] = j;
                if (f[j]) ++cnt;
            }
            if (cnt >= a[ b[i] ]) continue;
            for (j = cn - 1; j >= 0; --j)
                if (!f[x = c[j]]) {
                    f[x] = 1;
                    ++cnt;
                    ++ans;
                    if (cnt >= a[ b[i] ]) break;
                }
        }
        printf("Case #%d: %d\n", ++cas, ans);
    }
    return 0;
}
