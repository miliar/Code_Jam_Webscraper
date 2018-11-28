#include <cstdio>

int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a%b);
}

void solve(int CASE) {
    printf("Case #%d: ", CASE);
    long long n;
    int pd, pg;
    scanf("%lld %d %d", &n, &pd, &pg);

    int gpd = gcd(pd, 100);
    if (gpd == 0) gpd = 1;

    if (pd / gpd > n || (pg == 100 && pd != 100) || (pd != 0 && pg == 0)) {
        printf("Broken\n");
        return;
    }

    int req = 1;
    if (pd % 4 == 0) {
    } else if (pd % 2 == 0) {
        req *= 2;
    } else {
        req *= 4;
    }

    if (pd % 25 == 0) {
    } else if (pd % 5 == 0) {
        req *= 5;
    } else {
        req *= 25;
    }

    if (req > n) {
        printf("Broken\n");
    } else {
        printf("Possible\n");
    }
}

int main() {
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        solve(i+1);
    }

    return 0;
}
