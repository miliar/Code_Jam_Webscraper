#include <stdio.h>

int main() {
    int T;
    scanf("%d\n", &T);
    for (int num = 1; num <= T; ++num) {
        int N;
        int a[1000];
        scanf("%d\n", &N);
        for (int i = 0; i < N; ++i) {
            scanf("%d", &a[i]);
        }
        int tot = 0;
        for (int i = 0; i < N; ++i)
            if (a[i] != i + 1)
                ++tot;
        printf("Case #%d: %d.000000\n", num, tot);
    }
    return 0;
}
