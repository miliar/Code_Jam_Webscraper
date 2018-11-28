#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#define max(x,y) ((x)>(y)?(x):(y))
#define min(x,y) ((x)<(y)?(x):(y))

int T, C, r, c, d;
char map[505][505];

bool calc(int i, int j, int k) {
    double midx=i+(k-1)*0.5,midy=j+(k-1)*0.5,xmass=0,ymass=0;
    for (int u=0;u<k;u++)
        for (int v=0;v<k;v++)
            if (u==0 && v==0 || u==0 && v==k-1 || u==k-1 && v==0 || u==k-1 && v==k-1) {
            } else {
                xmass+=(d+map[i+u][j+v]-'0')*(i+u-midx);
            }
    for (int u=0;u<k;u++)
        for (int v=0;v<k;v++)
            if (u==0 && v==0 || u==0 && v==k-1 || u==k-1 && v==0 || u==k-1 && v==k-1) {
            } else {
                ymass+=(d+map[i+u][j+v]-'0')*(j+v-midy);
            }
    return fabs(xmass)<1e-8 && fabs(ymass)<1e-8;
}

int main() {
    freopen("D:\\B-small-attempt0.in","r",stdin);
    freopen("D:\\B-small-attempt0.out","w",stdout);
    int i, j, k, l;
    scanf("%d", &T);
    for (C = 1; C <= T; C++) {
        scanf("%d%d%d", &r, &c, &d);
        for (i = 0; i < r; i++)
            scanf("%s", map[i]);
        int k = min(r, c), ans = -1;
        for (l = 3; l <= k; l++)
            for (i = 0; i + l <= r; i++)
                for (j = 0; j + l <= c; j++) {
                    if (calc(i, j, l))
                        ans = max(ans, l);
                }
        if (~ans)
            printf("Case #%d: %d\n", C, ans);
        else
            printf("Case #%d: IMPOSSIBLE\n", C);
        fflush(stdout);
    }
    return 0;
}