#define MAXN 1010

#include <cstdio>
#include <cstring>

long long a[MAXN];
bool vis[MAXN];

int main() {
    int tec, cas, l, n, c, i, j, tag;
    long long t, ret, tot, tmp, m;

//    freopen("B-small-attempt1.in", "r", stdin);
//    freopen("B-small-attempt1.out", "w", stdout);

    scanf("%d", &tec);
    for (cas = 1; cas <= tec; cas++) {
        scanf("%d%lld%d%d", &l, &t, &n, &c);
        for (i = 0; i < c; i++) {
            scanf("%lld", &a[i]);
        }

        ret = 0;
        tag = -1;
        for (i = 0; i < n; i++) {
            ret += a[i % c] * 2;
            if (tag == -1 && ret >= t) {
                tag = i;
                tot = ret;
            }
        }

        tmp = (tot - t) / 2;
        memset(vis, 0, sizeof(vis));
        while (l--) {
            if (vis[tag]) {
                m = -1;
            }
            else {
                m = tmp;
                j = tag;
            }
            for (i = tag + 1; i < n; i++) {
                if (!vis[i] && (a[i % c] > m || m == -1)) {
                    m = a[i % c];
                    j = i;
                }
            }
            vis[j] = true;
            ret -= m;
        }

        printf("Case #%d: %lld\n", cas, ret);
    }

    return 0;
}
