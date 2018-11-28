#include <cstdio>
#include <cstring>

using namespace std;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int ti = 0; ti < T; ti++) {
        int n, A, B, C, D, x0, y0, M;
        scanf("%d%d%d%d%d%d%d%d", &n, &A, &B, &C, &D, &x0, &y0, &M);

        long long sum[3][3], sum2[3][3], result = 0;
        memset(sum, 0, sizeof(sum));
        memset(sum2, 0, sizeof(sum2));

        int x = x0, y = y0;
        for (int i = 0; i < n; i++) {
            result += sum2[(3 - (x % 3)) % 3][(3 - (y % 3)) % 3];
            for (int a = 0; a < 3; a++) {
                for (int b = 0; b < 3; b++) {
                    sum2[(a + x) % 3][(b + y) % 3] += sum[a][b];
                }
            }
            sum[x % 3][y % 3]++;
            x = ((long long)A * x + B) % M;
            y = ((long long)C * y + D) % M;
        }
        printf("Case #%d: %lld\n", ti + 1, result);
    }
    return 0;
}
