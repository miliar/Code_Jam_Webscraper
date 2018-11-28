#include <algorithm>
#include <cstdio>
#include <climits>
using namespace std;

int main()
{
    int cases, n, a[1992];
    scanf("%d", &cases);
    for (int T = 1; T <= cases; T++) {
        int xorsum = 0, sum = 0, mina = INT_MAX;
        scanf("%d", &n);
        for (int i = 0; i < n; i++) {
            scanf("%d", &a[i]);
            xorsum ^= a[i];
            mina = min(mina, a[i]);
            sum += a[i];
        }
        printf("Case #%d: ", T);
        if (xorsum)
            puts("NO");
        else
            printf("%d\n", sum-mina);
    }
}
