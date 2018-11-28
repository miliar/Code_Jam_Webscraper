#include <cstdio>

int main() {
    long long T, a, b, c, i;
    scanf("%lld", &T);
    bool broken;

    int t;
    for (t = 1; t <= T; t++) {
        broken = false;
        scanf("%lld %lld %lld", &a, &b, &c);
        if (c == 100 && b < 100) broken = true;
        if (c == 0) {
            broken = (b != 0);
        } else {
            long long d = 100;
            for (i = b; i >= 1; i--) {
                if (b % i == 0 && d % i == 0) {
                    b /= i;
                    d /= i;
                }
            }
            if (d > a) broken = true;
        }
        printf("Case #%d: %s\n", t, broken ? "Broken" : "Possible");
    }
    return 0;
}

