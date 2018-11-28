#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAXN = 1005;

int a[MAXN];
int nTests, n;

int main() {
    freopen("EXAMPLE.INP", "r", stdin);
    freopen("C.OUT", "w", stdout);
    scanf("%d", &nTests);
    for (int t = 1; t <= nTests; t++) {
        scanf("%d", &n);
        for (int i = 1; i <= n; i++)
            scanf("%d", a + i);

        printf("Case #%d: ", t);

        int sxor = 0, sum = 0, minA = a[1];
        for (int i = 1; i <= n; i++) {
            sxor ^= a[i];
            sum += a[i];
            minA = min(minA, a[i]);
        }

        if (sxor == 0) {
            int res = sum - minA;
            printf("%d", res);
        }
        else printf("NO");

        if (t < nTests) printf("\n");
    }
}
