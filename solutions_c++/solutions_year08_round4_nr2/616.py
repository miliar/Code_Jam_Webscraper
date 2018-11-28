#include <cstdio>

int main() {
    int C;
    scanf("%d", &C);
    for (int c = 1; c <= C; c ++) {
        int N, M, A;
        scanf("%d %d %d", &N, &M, &A);
        int x0, y0, x1, y1, x2, y2;
        x0 = 0;
        y0 = 0;
        bool ok = false;
        for (int a = 0; a <= N; a ++) {
            for (int b = 0; b <= M; b ++) {
                for (int c = 0; c <= N; c ++) {
                    for (int d = 0; d <= M; d ++) {
                        if (a * d - b * c == A) {
                            ok = true;
                            x1 = a;
                            y1 = b;
                            x2 = c;
                            y2 = d;
                            goto e;
                        }
                    }
                }
            }
        }
        e:
        if (ok) {
            printf("Case #%d: %d %d %d %d %d %d\n", c, x0, y0, x1, y1, x2, y2);
        } else {
            printf("Case #%d: IMPOSSIBLE\n", c);
        }
    }
    return 0;
}
