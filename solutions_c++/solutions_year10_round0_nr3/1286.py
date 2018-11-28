#include <cstdio>
#include <cstring>

#define N 2005
#define LL long long

LL a[N], s[N];
int v[N], id[N];
bool vis[N];

int main() {
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int t, r, k, n, cnt, ini, i, j, now, nxt, T, cas = 0;
    LL sum, m, sT;
    scanf("%d", &t);
    while (t--) {
        scanf("%d %d %d", &r, &k, &n);
        for (i = 0; i < n; ++i) {
            scanf("%lld", &a[i]);
            a[i + n] = a[i];
        }

        for (i = 0; i < n; ++i) {
            sum = 0;
            for (j = 0; j < n && sum <= k; ++j)
                sum += a[i + j];
            if (sum <= k) {
                s[i] = sum;
                v[i] = i;
            } else {
                --j;
                s[i] = sum - a[i + j];
                v[i] = (i + j) % n;
            }
        }

//        for (i = 0; i < n; ++i)
//            printf(" %lld,%d", s[i], v[i]);
//        puts("");

        if (0 == v[0]) {
            sum = s[0] * r;
            printf("Case #%d: %lld\n", ++cas, sum);
            continue;
        }

        bool over = 0;
        memset(vis, 0, sizeof(vis));
        now = 0; sum = 0; cnt = 0;
        while (1) {
            id[now] = cnt++;
            vis[now] = 1;
            sum += s[now];
            if (cnt == r) {
                over = 1;
                break;
            }
            nxt = v[now];
            if (vis[nxt])
                break;
            now = nxt;
        }

        if (over) {
            printf("Case #%d: %lld\n", ++cas, sum);
            continue;
        }

        T = cnt - id[nxt];
        sT = 0;
        for (i = nxt; v[i] != nxt; i = v[i])
            sT += s[i];
        sT += s[i];
        m = (r - cnt) / T;
        sum += m * sT;
        r = (r - cnt) % T;
//        printf("%d %d %d,%d\n", cnt, m, nxt, r);
        for (i = nxt; r--; i = v[i])
            sum += s[i];
//        printf(" %d %lld\n", T, sT);
        printf("Case #%d: %lld\n", ++cas, sum);
    }
    return 0;
}
