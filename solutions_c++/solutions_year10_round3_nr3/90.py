#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
#define MaxN 520

int T, n, m, t, ans, a[MaxN][MaxN], r[MaxN][MaxN], d[MaxN][MaxN], f[MaxN][MaxN], tot[MaxN], best, px, py, cnt;
char s[MaxN];
bool vst[MaxN][MaxN];

int main()
{
    //freopen("test.txt", "r", stdin);
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas) {
        memset(tot, 0, sizeof(tot));
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; ++i) {
            scanf("%s", s);
            for (int j = 0; j < m/4; ++j) {
                t = s[j] <= '9' ? s[j]-'0' : s[j]-'A'+10;
                for (int k = 3; k >= 0; --k, t>>=1)
                    a[i][j*4+k] = t&1;
            }
        }
        for (int i = 0; i <= n; ++i)
            a[i][m] = a[i][m-1];
        for (int j = 0; j <= m; ++j)
            a[n][j] = a[n-1][j];
        a[n][m] = a[n-1][m-1];
        memset(vst, 0, sizeof(vst));

        for (int iter = 0; iter < n*m; ++iter) {
            best = -1;
            for (int i = n-1; i >= 0; --i)
                for (int j = m-1; j >= 0; --j) {
                    r[i][j] = vst[i][j] ? 0 : a[i][j] == a[i][j+1] ? 1 : r[i][j+1]+1;
                    d[i][j] = vst[i][j] ? 0 : a[i][j] == a[i+1][j] ? 1 : d[i+1][j]+1;
                }
            for (int i = n-1; i >= 0; --i)
                for (int j = m-1; j >= 0; --j) {
                    f[i][j] = vst[i][j] ? 0 : a[i][j] != a[i+1][j+1] ? 1 : min(f[i+1][j+1]+1, min(r[i][j], d[i][j]));
                    if (f[i][j] >= best) {
                        px = i, py = j;
                        best = f[i][j];
                    }
                }
            if (best == 1) break;
            ++tot[best];
            for (int i = 0; i < best; ++i)
                for (int j = 0; j < best; ++j)
                    vst[px+i][py+j] = 1;
        }
//        for (int i = 0; i < n; ++i)
//            for (int j = 0; j < m; ++j)
//                if (!vst[i][j] && (!i || !j || f[i-1][j-1] != f[i][j] +1)) {
//                    t = f[i][j];
//                    ++tot[t];
//                    for (int x = 0; x < t; ++x)
//                        for (int y = 0; y < t; ++y)
//                            vst[i+x][j+y] = 1;
//                }
        //
//        puts("show array a");
//        for (int i = 0; i < n; ++i) {
//            for (int j = 0; j < m; ++j)
//                printf("%d", a[i][j]);
//            puts("");
//        }
//        puts("show array r");
//        for (int i = 0; i < n; ++i) {
//            for (int j = 0; j < m; ++j)
//                printf("%4d", r[i][j]);
//            puts("");
//        }
//        puts("show array d");
//        for (int i = 0; i < n; ++i) {
//            for (int j = 0; j < m; ++j)
//                printf("%4d", d[i][j]);
//            puts("");
//        }
//        puts("show array f");
//        for (int i = 0; i < n; ++i) {
//            for (int j = 0; j < m; ++j)
//                printf("%3d", f[i][j]);
//            puts("");
//        }
        //
        ans = 0; cnt = n*m;
        for (int i = max(n, m); i > 1; --i)
            if (tot[i] > 0) {
                ++ans;
                cnt -= i*tot[i]*i;
            }
        if (cnt > 0) ++ans;
        printf("Case #%d: %d\n", cas, ans);
        for (int i = max(n, m); i > 1; --i)
            if (tot[i] > 0) printf("%d %d\n", i, tot[i]);
        if (cnt > 0) printf("%d %d\n", 1, cnt);
    }
    return 0;
}
