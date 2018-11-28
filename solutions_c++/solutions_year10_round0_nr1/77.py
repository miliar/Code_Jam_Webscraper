#include <cstdio>

int main() {
    freopen("A-large.in", "r", stdin);
    int T, n, k, test = 1;
    for(scanf("%d", &T); T; T --) {
        scanf("%d%d", &n, &k);
        printf("Case #%d: ", test ++);
        if(k % (1 << n) == (1 << n) - 1)
            printf("ON\n");
        else
            printf("OFF\n");
    }
    return 0;
}

