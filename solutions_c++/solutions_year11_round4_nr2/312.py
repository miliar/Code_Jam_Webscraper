#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;
long long c[510][510], sum[510][510];
long long dpx[510][510];
long long dpy[510][510];
char s[510];
long long fx(int x, int y){
    return c[x][y] * (2 * x + 1);
}
long long fy(int x, int y){
    return c[x][y] * (2 * y + 1);
}
long long sumx(int x, int y, int k){
    long long t;
    t = dpx[x + k - 1][y + k - 1] - dpx[x - 1][y + k - 1] - dpx[x + k - 1][y - 1] + dpx[x - 1][y - 1];
    t -= fx(x, y) + fx(x + k - 1, y) + fx(x, y + k - 1) + fx(x + k - 1, y + k - 1);
    return t;
}
long long sumy(int x, int y, int k){
    long long t;
    t = dpy[x + k - 1][y + k - 1] - dpy[x - 1][y + k - 1] - dpy[x + k - 1][y - 1] + dpy[x - 1][y - 1];
    t -= fy(x, y) + fy(x + k - 1, y) + fy(x, y + k - 1) + fy(x + k - 1, y + k - 1);
    return t;
}
long long ss(int x, int y, int k){
    long long t;
    t = sum[x + k - 1][y + k - 1] - sum[x - 1][y + k - 1] - sum[x + k - 1][y - 1] + sum[x - 1][y - 1];
    t -= c[x][y] + c[x + k - 1][y] + c[x][y + k - 1] + c[x + k - 1][y + k - 1];
    return t;
}
int main(){
    int T, ri = 1, n, m, d, i, j, k, p, q, dx, dy;
    freopen("B-large (2).in", "r", stdin);
    freopen("out.txt", "w", stdout);
    scanf("%d", &T);
    while (T--){
        scanf("%d%d%d", &n, &m, &d);
        for (i = 1; i <= n; i++){
            scanf("%s", s);
            for (j = 0; j < m; j++){
                c[i][j + 1] = s[j] - '0' + d;
            }
        }
        memset(sum, 0, sizeof(sum));
        memset(dpx, 0, sizeof(dpx));
        memset(dpy, 0, sizeof(dpy));
        for (i = 1; i <= n; i++){
            dpx[i][1] = c[i][1] * (2 * i + 1);
            dpy[i][1] = c[i][1];
            sum[i][1] = c[i][1];
            for (j = 1; j <= m; j++){
                dpx[i][j] = c[i][j] * (2 * i + 1) + dpx[i][j - 1];
                dpy[i][j] = c[i][j] * (2 * j + 1) + dpy[i][j - 1];
                sum[i][j] = c[i][j] + sum[i][j - 1];
            }
        }
        for (i = 2; i <= n; i++){
            for (j = 1; j <= m; j++){
                dpx[i][j] += dpx[i - 1][j];
                dpy[i][j] += dpy[i - 1][j];
                sum[i][j] += sum[i - 1][j];
            }
        }
        for (k = min(m, n); k > 2; k--){
            for (i = 1; i + k <= n + 1; i++){
                for (j = 1; j + k <= m + 1; j++){
                    p = i + i + k;
                    q = j + j + k;
                    dx = dy = 0;
                    dx = sumx(i, j, k) - p * ss(i, j, k);
                    dy = sumy(i, j, k) - q * ss(i, j, k);
                    if (0 == dx && 0 == dy){
                        printf("Case #%d: ", ri++);
                        goto l;
                    }
                }
            }
        }
        printf("Case #%d: ", ri++);
        if (0){
l:          printf("%d\n", k);
        }
        else{
            printf("IMPOSSIBLE\n");
        }
    }
    return 0;
}
