#include <cstdio>
#include <string>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAXN = 512;
char buf[MAXN];
int hsum[MAXN][MAXN], ssum[MAXN][MAXN];
int sum[MAXN][MAXN];
int flg1[MAXN][MAXN], flg2[MAXN][MAXN];
int a[MAXN][MAXN];
int R, C;

inline int rect(int x1, int y1, int x2, int y2) {
    return sum[x2][y2] - sum[x1-1][y2] - sum[x2][y1-1] + sum[x1-1][y1-1];
}

int check(int sx, int sy, int K) {
    int i, j;
    if (K % 2 == 1) {
        int mx = sx + K / 2, my = sy + K / 2;
        int v1 = 0, v2 = 0;
        for (i = sx ; i < sx + K ; i++)
            for (j = sy ; j < sy + K ; j++) {
                if (i == sx && j == sy ||
                    i == sx + K - 1 && j == sy ||
                    i == sx && j == sy + K - 1 ||
                    i == sx + K - 1 && j == sy + K -1) continue;
                v1 += (i - mx) * a[i][j];
                v2 += (j - my) * a[i][j];
            }
        if (v1 == 0 && v2 == 0) return 1;
    } else {
        int v1 = 0, v2 = 0;
        int mx = sx * 2 + K - 1, my = sy * 2 + K - 1;
        for (i = sx * 2 ; i < (sx + K) * 2 ; i += 2)
            for (j = sy * 2 ; j < (sy + K) * 2 ; j += 2) {
                if (i / 2 == sx && j / 2 == sy ||
                    i / 2 == sx + K - 1 && j / 2 == sy ||
                    i / 2 == sx && j / 2 == sy + K - 1 ||
                    i / 2 == sx + K - 1 && j / 2 == sy + K -1) continue;
                v1 += (i - mx) * a[i/2][j/2];
                v2 += (j - my) * a[i/2][j/2];
            }
        if (v1 == 0 && v2 == 0) return 1;
    }
    return 0;
}

int main() {
    freopen("b-small-attempt1.in","r",stdin);
    freopen("b-small-attempt1.out","w",stdout);
    int T, ca, i, j, ttt;
    scanf("%d",&T);
    for (ca = 1 ; ca <= T ; ++ca) {
        scanf("%d%d%d",&R,&C,&ttt);
        for (i = 1 ; i <= R ; i++) {
            scanf("%s",buf+1);
            for (j = 1 ; j <= C ; j++) {
                a[i][j] = buf[j] - '0';
            }
        }
        for (i = 1 ; i <= R ; i++) {
            for (j = 1 ; j <= C ; j++) {
                hsum[i][j] = hsum[i][j-1] + a[i][j];
                sum[i][j] = sum[i-1][j] + hsum[i][j];
            }
        }
        for (j = 1 ; j <= C ; j++) {
            for (i = 1 ; i <= R ; i++)
                ssum[i][j] = ssum[i-1][j] + a[i][j];
        }
        int k, sx, sy;
        for (k = min(R,C) ; k >= 3 ; --k) {
            for (sx = 1 ; sx + k <= R + 1 ; sx++) {
                for (sy = 1 ; sy + k <= C + 1 ; sy++) {
                    if (check(sx,sy,k)) {
                        goto out;
                    }
                }
            }
        }
out:
        printf("Case #%d: ",ca);
        if (k < 3) printf("IMPOSSIBLE\n");
        else printf("%d\n",k);
    }
    return 0;
}
