#include <stdio.h>
#include <string.h>
#define LL long long
#define MaxN 2010

LL a[MaxN], sum[MaxN], tot[MaxN], r, k, t, ans;
int T, n, m, cur, len, id[MaxN], cas;

int main()
{
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    scanf("%d", &T);
    while (T--) {
        memset(id, 0, sizeof(id));
        scanf("%d%lld%d", &m, &k, &n);
        sum[0] = a[0] = tot[0] = 0;
        for (int i = 1; i <= n; ++i) {
            scanf("%lld", a+i);
            sum[i] = sum[i-1] + a[i];
        }
        for (int i = n+1; i <= n+n; ++i) {
            a[i] = a[i-n];
            sum[i] = sum[i-1] + a[i];
        }
        cur = 1; if (k > sum[n]) k = sum[n];
        for (int i = 1; ; ++i) {
            if (id[cur]) {
                len = i-id[cur];
                ans = (m-id[cur]+1)/len*(tot[i-1]-tot[id[cur]-1]) + tot[id[cur]-1+(m-id[cur]+1)%len];
                break;
            }
            id[cur] = i;
            tot[i] = tot[i-1];
            for (int t = k, j = cur; t >= 0; ++j) {
                t -= a[j];
                if (t < 0) {
                    cur = j > n ? j-n : j;
                    break;
                }
                tot[i] += a[j];
            }
        }
        printf("Case #%d: %lld\n", ++cas, ans);
    }
    return 0;
}
