#include <cstdio>

int f[100];

int main() {
    //freopen("A-large.in", "r", stdin);
    //freopen("out.txt", "w", stdout);
    int T, n, k, ison;
    int i;
    f[0] = 0;
    for (i = 1; i <= 32; i++) f[i] = f[i - 1]*2 + 1;
    scanf("%d", &T);
    int tt;
    for (tt = 1; tt <= T; tt++) {
        scanf("%d%d", &n, &k);
        if ((k + 1) % (f[n] + 1) == 0) ison = 1;
        else ison = 0;
        printf("Case #%d: %s\n", tt, ison ? "ON" : "OFF");
    }
    return 0;
}
