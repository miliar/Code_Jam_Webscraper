#include <cstdio>
#include <cassert>
#include <cstring>

int tmp[200][200];

int gcd(int a, int b) {
    return (a == 0) ? b : gcd(b % a, a);
}

int gao2(int a, int b) {
    if (a > b) {
        int t = a;
        a = b;
        b = t;
    }
    if (a == b)
        return 0;
    if (a <= 0 || b <= 0)
        return 1;
    if (b >= a * 2)
        return 1;

    return 1 - gao2(b - a, a);
        
}

int gao(int a, int b) {
    if (a == b)
        return 0;
    if (a <= 0 || b <= 0)
        return 1;
    if (tmp[a][b] != -1)
        return tmp[a][b];

    int ret = 0;
    for (int na = a - b; ; na -= b) {
        int xx = gao(b, na);
        if (xx == 0) {
            ret = 1;
            goto end;
        }
        if (na < 0)
            break;
    }
    for (int nb = b - a; ; nb -= a) {
        int xx = gao(nb, a);
        if (xx == 0) {
            ret = 1;
            goto end;
        }
        if (nb < 0)
            break;
    }
end:
    return tmp[a][b] = ret;
}

int main1() {
    memset(tmp, -1, sizeof(tmp));
    for (int i = 1; i <= 20; i++) {
        int cnt = 0;
        for (int j = 1; j <= 100; j++) {
            int k = gcd(i, j);
            if (k != 1) {
                assert(gao(i, j) == gao(i / k, j / k));
                continue;
            }
            assert(gao(i, j) == gao2(i, j));
            if (gao(i, j) == 2) {
                printf("(%2d %2d)", i, j);
                cnt++;
            }
        }
        //printf(" %d\n", cnt);
        printf("\n");
    }
    printf("%d %d\n", gao(5, 8), gao(11, 2));
    // (a, a) -> (a, ka)
    //        -> (a + ka, 
    return 0;
}
int T, t, a1, a2, b1, b2, i, j;
int main() {
    scanf("%d", &T);
    for (t = 1; t <= T; t++) {
        scanf("%d%d%d%d", &a1, &a2, &b1, &b2);
        int cnt = 0;
        for (i = a1; i <= a2; i++)
            for (j = b1; j <= b2; j++) {
                cnt += gao2(i, j);
            }
        printf("Case #%d: %d\n", t, cnt);
    }
}
