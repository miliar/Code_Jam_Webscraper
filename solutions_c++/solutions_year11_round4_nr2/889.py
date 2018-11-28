#include <cstdio>
#include <algorithm>
using namespace std;

int T, t, r, c, d, best, lenm, sx, sy, mx, my;
int w[1024][1024];
char buf[1024];

int main() {
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d%d%d", &r, &c, &d);
        for (int i = 0; i < r; i++) {
            scanf("%s", buf);
            for (int j = 0; j < c; j++)
                w[i][j] = buf[j] - '0';
        }

        best = 0;
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                lenm = min(r - i, c - j);
                for (int len = 3; len <= lenm; len++) {
                    sx = 0; sy = 0;
                    mx = len - 1;
                    my = len - 1;
                    for (int p = 0; p < len; p++) {
                        for (int q = 0; q < len; q++) {
                            sx += w[i + p][j + q] * (p * 2 - mx);
                            sy += w[i + p][j + q] * (q * 2 - my);
                        }
                    }
                    sx -= w[i + 0][j + 0] * -mx;
                    sx -= w[i + 0][j + len - 1] * -mx;
                    sx -= w[i + len - 1][j + 0] * mx;
                    sx -= w[i + len - 1][j + len - 1] * mx;
                    sy -= w[i + 0][j + 0] * -mx;
                    sy -= w[i + 0][j + len - 1] * mx;
                    sy -= w[i + len - 1][j + 0] * -mx;
                    sy -= w[i + len - 1][j + len - 1] * mx;

                    //printf("(%d, %d, %d) %d %d\n", i, j, len, sx, sy);
                    if (sx == 0 && sy == 0 && len > best)
                        best = len;
                }
            }
        }
        if (best != 0) {
            printf("Case #%d: %d\n", t, best);
        } else {
            printf("Case #%d: IMPOSSIBLE\n", t);
        }
    }
}
