#include <cstdio>

int f(int n) {
        int a = 6, b = -4, c = 1, d = 0, za = 1, zb = 0, zc = 0, zd = 1, ta, tb, tc, td;
        while (n) {
                if (n&1) {
                        ta = za*a + zb*c;
                        tb = za*b + zb*d;
                        tc = zc*a + zd*c;
                        td = zc*b + zd*d;
                        za = ta%1000, zb = tb%1000, zc = tc%1000, zd = td%1000;
                }
                n >>= 1;
                ta = a*a + b*c;
                tb = a*b + b*d;
                tc = c*a + d*c;
                td = c*b + d*d;
                a = ta%1000, b = tb%1000, c = tc%1000, d = td%1000;
        }
        return ((zc*6 + zd*2)%1000 + 1000)%1000;
}

int T, n;

int main() {
        scanf("%d", &T);
        for (int r = 1; r <= T; ++r) {
                scanf("%d", &n);
                printf("Case #%d: %03d\n", r, f(n) - 1);
        }
        return 0;
}
