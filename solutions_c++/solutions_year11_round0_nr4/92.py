#include <cstdio>
#include <cstring>

const int N = 1010;

int main() {
    int cas, tt;
    scanf("%d", &tt);
    for (cas = 1; cas <= tt; cas ++) {
        int n, res = 0, x;
        scanf("%d", &n);
        for (int i = 1; i <= n; i ++) {
            scanf("%d", &x);
            if (x != i) res ++;
        }
        printf("Case #%d: %d.000000\n", cas, res);
    }
    return 0;
}

