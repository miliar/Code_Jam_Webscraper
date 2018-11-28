#include <cstdio>

int T, A1, A2, B1, B2;

int check(int a, int b) {
    if (a == b) return -1;
    if (a % b == 0 || b % a == 0) return 1;
    int x, y;
    if (a > b) {
        if (a > 2 * b) {
            x = check(a % b, b);
            y = check(a % b + b, b);
            if (x == -1 || y == -1) return 1;
            else return -1;
        } else return -check(a % b, b);
    } else {
        if (b > 2 * a) {
            x = check(a, b % a);
            y = check(a, b % a + a);
            if (x == -1 || y == -1) return 1;
            else return -1;
        } else return -check(a, b % a);
    }
}

int main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-out.txt", "w", stdout);
    int tc, i, j, count;
    scanf("%d", &T);
    for (tc = 1; tc <= T; tc++) {
        scanf("%d%d%d%d", &A1, &A2, &B1, &B2);
        count = 0;
        for (i = A1; i <= A2; i++)
            for (j = B1; j <= B2; j++) {
                if (check(i, j) == 1) count++;
            }
        printf("Case #%d: %d\n", tc, count);
    }
    return 0;
}
