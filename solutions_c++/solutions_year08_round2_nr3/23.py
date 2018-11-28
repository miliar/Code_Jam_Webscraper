#include <cstdio>

int res(int k, int d, int x) {
    while (d % k != x % k) {
        x -= d % k;
        if (x <= 0) {
            x += k;
        }
        k -= 1;
        d += 1;
    }
    return d;
}

int main() {
    int T;
    scanf("%d", &T);
    for (int c = 1; c <= T; c ++) {
        printf("Case #%d:", c);
        int K, n;
        scanf("%d %d", &K, &n);
        for (int i = 0; i < n; i ++) {
            int k;
            scanf("%d", &k);
            printf(" %d", res(K, 1, k));
        }
        printf("\n");
    }
}
