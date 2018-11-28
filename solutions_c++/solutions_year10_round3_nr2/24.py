#include <cstdio>
#include <cmath>

int solve(long long a, long long b, long long c) {
    int sol = 0;
    while (a * c < b) {
        c = c * c;
        ++sol;
    }
    return sol;
}

int main() {
    freopen("date.in", "r", stdin);
    freopen("date.out", "w", stdout);

    int t; scanf("%d", &t);
    for (int test = 1; test <= t; ++test) {
        int a, b, c;
        scanf("%d %d %d", &a, &b, &c);
        printf("Case #%d: %d\n", test, solve(a, b, c));
    }
}
