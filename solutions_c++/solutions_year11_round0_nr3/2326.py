#include <iostream>
using namespace std;
const int maxn = 1000 + 10, maxint = 1000000000;

int n, p[maxn];

int main(void)
{
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; i++) {
        scanf("%d", &n);
        int sum0, sum1;
        sum0 = sum1 = 0;
        for (int j = 0; j < n; j++) {
            scanf("%d", &p[j]);
            sum0 ^= p[j];
            sum1 += p[j];
        }
        printf("Case #%d: ", i);
        if (sum0)
            printf("NO\n");
        else {
            int x = p[0];
            for (int j = 1; j < n; j++)
                if (x >= p[j])
                    x = p[j];
            int ans = sum1 - x;
            printf("%d\n", ans);
        }
    }
    return 0;
}
