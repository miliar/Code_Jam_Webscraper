#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>

#define ZERO(x) (fabs(x) < eps)
#define MAX 3010

using namespace std;

typedef long long i64;

const double eps = 1e-8;

i64 extEuclid(const i64 a, const i64 b, i64 &x, i64 &y) {
    i64 r, t;

    if (!b) {
        x = 1;
        y = 0;
        return a;
    }
    r = extEuclid(b, a % b, x, y);
    t = x;
    x = y;
    y = t - a / b * y;

    return r;
}

//求解 ax = b mod n, ans = -1代表无解
i64 modEquation(i64 a, i64 b, i64 n) {
    i64 d, x, y, ans = -1;

    ans = -1;
    d = extEuclid(a, n, x, y);
    if (b % d) return -1;
    x = x * (b / d);
    ans = (x % (n / d) + (n / d)) % (n / d);

    return ans;
}

bool check(const i64 n, const i64 d, const i64 g, i64 &i, i64 &j) {
    i64 t;

    for (i = 1; i <= n; i++) {
        if (i * 100 % d) continue;
        j = i * 100 / d;

//        printf("i = %lld, j = %lld\n", i, j);

        if (j >= i && j <= n) return true;
    }

    return false;
}

bool solve(const i64 n, const i64 d, const i64 g) {
    i64 i = 0, j = 0, x, y, t, a, b;

    if (!d && !g) return true;
    if (d < 100 && g == 100) return false;
    if (d && !g) return false;
    if (d) {
        if (!check(n, d, g, i, j)) return false;
    }

    for (b = g * j - 100 * i; b < 0; b += g);
    a = 100;
    x = modEquation(a, b, g);


//    printf("a = %lld, b = %lld, x = %lld\n", a, b, x);

    if (x == -1) return false;

    return true;
}

int main() {
    int i, t, cnt = 1;
    i64 n, d, g;
    double pd, pg, k;

//    freopen("A-large.in", "r", stdin);
//    freopen("A-large.out", "w", stdout);

    scanf("%d", &t);
    while (t--) {
        scanf("%lld %lld %lld", &n, &d, &g);
        pd = (double)d;
        pg = (double)g;
        k = n * pd / 100 / (pg / 100);
        printf("Case #%d: ", cnt++);
        if (solve(n, d, g)) printf("Possible\n");
        else printf("Broken\n");
    }

    return 0;
}
