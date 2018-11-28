#include <cstdio>
using namespace std;
int i, ans, x, t, T, N;

int main() {
    freopen("D.in", "r", stdin);
    freopen("D.out", "w", stdout);
    for (scanf("%d", &T), t = 1; t <= T; t ++) {
        scanf("%d", &N);
        for (i = 1, ans = 0; i <= N; i ++) {
            scanf("%d", &x);
            if (x != i) ++ ans;
        }
        printf("Case #%d: %d.000000\n", t, ans);
    }
    return 0;
}
