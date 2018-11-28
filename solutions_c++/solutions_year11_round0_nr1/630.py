#include <stdio.h>
#define abs(x) ((x) < 0 ? (-(x)) : (x))

int main() {
    int T;
    scanf("%d\n", &T);
    for (int num = 1; num <= T; ++num) {
        int N;
        scanf("%d", &N);
        int t0 = 0, t1 = 0;
        int p0 = 1, p1 = 1;
        for (int i = 0; i < N; ++i) {
            char r;
            int p;
            scanf(" %c %d", &r, &p);
            if (r == 'O') {
                t0 += abs(p - p0) + 1;
                p0 = p;
                if (t1 != 0 && t0 <= t1) t0 = t1 + 1;
            } else {
                t1 += abs(p - p1) + 1;
                p1 = p;
                if (t0 != 0 && t1 <= t0) t1 = t0 + 1;
            }
        }
        if (t0 > t1)
            printf("Case #%d: %d\n", num, t0);
        else
            printf("Case #%d: %d\n", num, t1);
    }
    return 0;
}
