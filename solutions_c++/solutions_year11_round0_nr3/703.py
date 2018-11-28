#include <cstdio>
#include <algorithm>


int main() {
    int T = 0;
    int N, C[1024];
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d", &N);
        for (int i = 0; i < N; i++)
            scanf("%d", &C[i]);
        std::sort(C, C + N);
        int mask = 0, sum = 0;
        for (int i = 0; i < N; i++) {
            mask ^= C[i];
            sum += C[i];
        }
        if (mask != 0) {
            printf("Case #%d: NO\n", t);
            continue;
        }
        printf("Case #%d: %d\n", t, sum - C[0]);
    }
}
