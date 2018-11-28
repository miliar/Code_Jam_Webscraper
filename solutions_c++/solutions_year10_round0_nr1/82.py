#include <cstdio>

const char input_file[] = "A-large.in";
const char output_file[] = "a.large.out";

void solve() {
    freopen(input_file, "r", stdin);
    freopen(output_file, "w", stdout);
    
    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; ++i) {
        int n, k;
        scanf("%d%d", &n, &k);
        int m = 1 << n;
        printf("Case #%d: ", i);
        if (k % m + 1 == m) {
            puts("ON");
        } else {
            puts("OFF");
        }
    }
}
int main() {
    solve();
    return 0;
}
