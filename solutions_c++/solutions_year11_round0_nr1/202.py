#include<stdio.h>
#include<string.h>
#include<math.h>
#include<iostream>
#include<algorithm>
using namespace std;
#define maxn 110
int t[maxn][maxn][maxn];
int q[maxn*maxn*maxn][3];
int ord[maxn*2][2];
int tt,cas=1;
int N,ans;
int main() {
    int i,j,a,b,cost;
    int aa,bb,L,R;
    char str[10];
    freopen("A-large.in","r",stdin);
    freopen("1.out","w",stdout);
    scanf("%d", &tt);
    while (tt--) {
        scanf("%d", &N);
        for (i = 0; i < N; i++) {
            scanf("%s%d", str, &a);
            ord[i][0] = (str[0] == 'O' ? 0 : 1);
            ord[i][1] = a;
        }
        L = 0, R = 1;
        q[0][0] = 1, q[0][1] = 1, q[0][2] = 0;
        memset(t, -1, sizeof (t));
        ans = 1000000000;
        t[1][1][0] = 0;
        while (L < R) {
            a = q[L][0], b = q[L][1], cost = q[L][2];
            L++;
            if (cost == N) {
                ans = min(ans, t[a][b][cost]);
                continue;
            }
            for (i = -1; i <= 1; i++)
                for (j = -1; j <= 1; j++) {
                    aa = a, bb = b;
                    aa += i, bb += j;
                    if (aa >= 1 && aa <= 100 && bb >= 1 && bb <= 100) {
                        if (t[aa][bb][cost] < 0) {
                            t[aa][bb][cost] = t[a][b][cost] + 1;
                            q[R][0] = aa, q[R][1] = bb, q[R][2] = cost;
                            R++;
                        }
                        if (ord[cost][0] == 0) {
                            if (i == 0 && aa == ord[cost][1]) {
                                if (t[aa][bb][cost + 1] < 0) {
                                    t[aa][bb][cost + 1] = t[a][b][cost] + 1;
                                    q[R][0] = aa, q[R][1] = bb, q[R][2] = cost + 1;
                                    R++;
                                }
                            }
                        } else {
                            if (j == 0 && bb == ord[cost][1]) {
                                if (t[aa][bb][cost + 1] < 0) {
                                    t[aa][bb][cost + 1] = t[a][b][cost] + 1;
                                    q[R][0] = aa, q[R][1] = bb, q[R][2] = cost + 1;
                                    R++;
                                }
                            }
                        }
                    }
                }

        }
        printf("Case #%d: ", cas);
        printf("%d\n", ans);
        cas++;
    }
    return 0;
}

