#include <cstdio>
#include <cstring>
#include <algorithm>

const int Max = 1000;

int x[Max], y[Max], n;

void input() {
    scanf("%d", &n);
    for(int i = 0;i < n;i ++) scanf("%d", &x[i]);
    for(int i = 0;i < n;i ++) scanf("%d", &y[i]);
}

void solve() {
    std::sort(x, x+n);
    std::sort(y, y+n);
    long long res = 0;
    for(int i = 0;i < n;i ++) res += (long long)x[i] * (long long)y[n-i-1];
    printf("%I64d\n", res);
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int t;
    scanf("%d", &t);
    for(int cas = 1;cas <= t;cas ++) {
        input();
        printf("Case #%d: ", cas);
        solve();
    }
    getchar(); getchar();
    return 0;
}
