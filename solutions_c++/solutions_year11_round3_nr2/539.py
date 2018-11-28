#include <stdio.h>
#include <string.h>

int main() {
    int T;
    scanf("%d", &T);
    for (int num = 1; num <= T; ++num) {
        int L, t, N, C;
        int a[1000];
        scanf("%d", &L);
        scanf("%d", &t);
        scanf("%d", &N);
        scanf("%d", &C);
        for (int i = 0; i < C; ++i) {
            scanf("%d", &a[i]);
        }
        if (L == 0) {
            int tot = 0;
            for (int i = 0; i < N; ++i) {
                tot += a[i % C];
            }
            printf("Case #%d: %d\n", num, tot * 2);
        }
        if (L == 1) {
            int best = 100000000;
            int b[1000];
            for (int j = 0; j < N; ++j) {
                memset(b, 0, sizeof(b));
                b[j] = 1;
                int tot = 0;
                int now = 0;
                while (now < N) {
                    if (b[now] == 1) {
                        if (tot >= t) {
                            tot += a[now % C];
                        } else {
                            if (a[now % C] * 2 > (t - tot))
                                tot += ((t - tot) >> 1) + a[now % C];
                            else
                                tot += a[now % C] * 2;
                        }
                    } else {
                        tot += a[now % C] * 2;
                    }
                    ++now;
                }
                if (tot < best) best = tot;
            }
            printf("Case #%d: %d\n", num, best);
        }
        if (L == 2) {
            int best = 100000000;
            int b[1000];
            for (int j = 0; j < N; ++j) {
                memset(b, 0, sizeof(b));
                b[j] = 1;
                int tot = 0;
                int now = 0;
                while (now < N) {
                    if (b[now] == 1) {
                        if (tot >= t) {
                            tot += a[now % C];
                        } else {
                            if (a[now % C] * 2 > (t - tot))
                                tot += ((t - tot) >> 1) + a[now % C];
                            else
                                tot += a[now % C] * 2;
                        }
                    } else {
                        tot += a[now % C] * 2;
                    }
                    ++now;
                }
                if (tot < best) best = tot;
            }
            for (int j = 0; j < N; ++j)
            for (int k = j + 1; k < N; ++k) {
                memset(b, 0, sizeof(b));
                b[j] = 1;
                b[k] = 1;
                int tot = 0;
                int now = 0;
                while (now < N) {
                    if (b[now] == 1) {
                        if (tot >= t) {
                            tot += a[now % C];
                        } else {
                            if (a[now % C] * 2 > (t - tot))
                                tot += ((t - tot) >> 1) + a[now % C];
                            else
                                tot += a[now % C] * 2;
                        }
                    } else {
                        tot += a[now % C] * 2;
                    }
                    ++now;
                }
                if (tot < best) best = tot;
            }
            printf("Case #%d: %d\n", num, best);
        }
    }
    return 0;
}
