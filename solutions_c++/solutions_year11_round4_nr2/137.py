#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>

using namespace std;

const int N = 520;
int R, C, D;
int a[N][N], sa[N][N], ar[N][N], sr[N][N], ac[N][N], sc[N][N];

int sum(int a[N][N], int s[N][N], int x1, int y1, int x2, int y2) {
    int res = s[x2][y2] + s[x1][y1] -s[x1][y2] - s[x2][y1];
    res = res - a[x1 + 1][y1 + 1] - a[x1 + 1][y2] - a[x2][y1 + 1] - a[x2][y2];
    return res;
}

void make(int a[N][N], int sa[N][N]) {
    memset(sa, 0, N * N * sizeof(int));
    for (int i = 1; i <= R; i ++)
        for (int j = 1; j <= C; j ++)
            sa[i][j] = a[i][j] + sa[i-1][j];
    for (int i = 1; i <= R; i ++)
        for (int j = 1; j <= C; j ++)
            sa[i][j] = sa[i][j] + sa[i][j-1];
}

int main() {
    int tt, cas;
    scanf("%d", &tt);
    for (cas = 1; cas <= tt; cas ++) {
        scanf("%d%d%d", &R, &C, &D);
        char ch;
        for (int i = 1; i <= R; i ++)
            for (int j = 1; j <= C; j ++) {
                do {
                    scanf("%c", &ch);
                } while (!isdigit(ch));
                a[i][j] = (ch - '0');
                ar[i][j] = a[i][j] * i;
                ac[i][j] = a[i][j] * j;
            }
        make(a , sa);
        make(ar, sr);
        make(ac, sc);
/*        for (int i = 1; i <= R; i ++) {
            for (int j = 1; j <= C; j ++) 
                printf("%4d", sa[i][j]);
            printf("\n");
        } */
        int ans = -1;
        for (int K = min(R, C); K >= 3 && ans == -1; K --) {
            for (int i = 0; i + K <= R; i ++)
                for (int j = 0; j + K <= C; j ++) {
                    int s1 = sum(a , sa, i, j, i+K, j+K);
                    int s2 = sum(ar, sr, i, j, i+K, j+K);
                    int s3 = sum(ac, sc, i, j, i+K, j+K);
//                    printf("%d %d %d : %d %d %d\n", i, j, K, s1, s2, s3);
                    if (s1*(i+1+i+K) == s2*2 && s1*(j+1+j+K) == s3*2)
                        ans = K;
               }
        }
        printf("Case #%d: ", cas);
        if (ans == -1)
            puts("IMPOSSIBLE");
        else printf("%d\n", ans);
    }
    return 0;
}

