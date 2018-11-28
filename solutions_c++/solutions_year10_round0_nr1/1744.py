#include <cstdio>

int main() {
    freopen("date.in", "r", stdin);
    freopen("date.out", "w", stdout);

    int t, n, k;

    scanf("%d", &t);
    for (int test = 1; test <= t; ++test) {
        scanf("%d %d", &n, &k);

        int ok = 1;
        for (int i = 0; i < n; ++i)
            ok &= (k >> i);

        printf("Case #%d: %s\n", test, ok ? "ON" : "OFF");
    }
}
