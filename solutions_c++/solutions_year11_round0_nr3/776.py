#include <cstdio>
#include <cstring>
using namespace std;

const int MAXN = 1005;
const int INF = 2140000005;

int n;

int main() {
    int t, casN = 0, i;
    int val, sum, rsum, sml;

    scanf("%d", &t);
    while (t-- > 0) {
        scanf("%d", &n);
        sum = rsum = 0;
        sml = INF;
        for (i = 0; i < n; i++) {
            scanf("%d", &val);
            if (val < sml) sml = val;
            sum ^= val;
            rsum += val;
        }
        printf("Case #%d: ", ++casN);
        if (sum != 0) puts("NO");
        else printf("%d\n", rsum - sml);
    }

    return 0;
}
