#include <cstdio>

int T, t, na, nb, x, y, a[100][2], b[100][2], ca, cb;

void z(bool f, int e) {
//      printf("z %d %d\n", f, e);
        int x;
        if (f) {
                for (x = 0; x < nb && b[x][0] < e; ++x);
                if (x == nb)
                        return;
                e = b[x][1] + t;
                --nb;
                for (int i = x; i < nb; ++i) {
                        b[i][0] = b[i + 1][0];
                        b[i][1] = b[i + 1][1];
                }
                z(0, e);
        } else {
                for (x = 0; x < na && a[x][0] < e; ++x);
                if (x == na)
                        return;
                e = a[x][1] + t;
                --na;
                for (int i = x; i < na; ++i) {
                        a[i][0] = a[i + 1][0];
                        a[i][1] = a[i + 1][1];
                }
                z(1, e);
        }
}

int main() {
        scanf("%d", &T);
        for (int r = 1; r <= T; ++r) {
                printf("Case #%d: ", r);
                scanf("%d%d%d", &t, &na, &nb);
                for (int i = 0; i < na; ++i) {
                        scanf("%d:%d", &x, &y);
                        a[i][0] = x*60 + y;
                        scanf("%d:%d", &x, &y);
                        a[i][1] = x*60 + y;
                }
                for (int i = 0; i < na; ++i)
                        for (int j = i + 1; j < na; ++j)
                                if (a[j][0] < a[i][0]) {
                                        a[i][0] ^= a[j][0] ^= a[i][0] ^= a[j][0];
                                        a[i][1] ^= a[j][1] ^= a[i][1] ^= a[j][1];
                                }
                for (int i = 0; i < nb; ++i) {
                        scanf("%d:%d", &x, &y);
                        b[i][0] = x*60 + y;
                        scanf("%d:%d", &x, &y);
                        b[i][1] = x*60 + y;
                }
                for (int i = 0; i < nb; ++i)
                        for (int j = i + 1; j < nb; ++j)
                                if (b[j][0] < b[i][0]) {
                                        b[i][0] ^= b[j][0] ^= b[i][0] ^= b[j][0];
                                        b[i][1] ^= b[j][1] ^= b[i][1] ^= b[j][1];
                                }
                ca = cb = 0;
                while (na && nb) {
                        if (a[0][0] < b[0][0]) {
                                ++ca;
                                z(0, 0);
                        } else {
                                ++cb;
                                z(1, 0);
                        }
                }
                printf("%d %d\n", ca + na, cb + nb);
        }
        return 0;
}
