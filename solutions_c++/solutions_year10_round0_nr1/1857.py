#include <cstdio>

using namespace std;

int t, n, k;

void solve();

int main() {
    freopen("out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int i = 0; i < t; ++i)
        solve();
    return 0;
}

void solve() {
    scanf("%d%d", &n, &k);
    printf("Case #%d: %s\n", ++t, k % (1 << n) == (1 << n) - 1 ? "ON" : "OFF");
}
