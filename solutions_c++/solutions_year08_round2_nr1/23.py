#include <cstdio>

int main() {
    int N;
    scanf("%d", &N);
    for (int c = 1; c <= N; c ++) {
        long long n, A, B, C, D, x0, y0, M;
        scanf("%I64d %I64d %I64d %I64d %I64d %I64d %I64d %I64d", &n, &A, &B, &C, &D, &x0, &y0, &M);
        long long num[3][3];
        for (int i = 0; i < 3; i ++) {
            for (int j = 0; j < 3; j ++) {
                num[i][j] = 0;
            }
        }
        for (int i = 0; i < n; i ++) {
            num[x0 % 3][y0 % 3] += 1;
            x0 = (A * x0 + B) % M;
            y0 = (C * y0 + D) % M;
        }
        long long res = 0;
        for (int i = 0; i < 3; i ++) {
            for (int j = 0; j < 3; j ++) {
                res += num[i][j] * (num[i][j] - 1) * (num[i][j] - 2) / 6;
            }
            res += num[i][0] * num[i][1] * num[i][2];
            res += num[0][i] * num[1][i] * num[2][i];
        }
        res += num[0][0] * num[1][1] * num[2][2];
        res += num[0][0] * num[1][2] * num[2][1];
        res += num[0][1] * num[1][2] * num[2][0];
        res += num[0][1] * num[1][0] * num[2][2];
        res += num[0][2] * num[1][0] * num[2][1];
        res += num[0][2] * num[1][1] * num[2][0];
        printf("Case #%d: %I64d\n", c, res);
    }
    return 0;
}
