#include <cstdio>
#include <algorithm>

using namespace std;

int aa[1100];

int main()
{
    int cn, cns;

    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);

    scanf("%d", &cns);
    for (cn = 0; cn < cns; cn++) {
        int n;
        scanf("%d", &n);
        int sum = 0;
        for (int i = 0; i < n; i++) {
            scanf("%d", &aa[i]);
            sum ^= aa[i];
        }
        sort(aa, aa + n);
        printf("Case #%d: ", cn + 1);
        if (sum == 0) {
            int ans = 0;
            for (int i = 1; i < n; i++) {
                ans += aa[i];
            }
            printf("%d\n", ans);
        } else {
            printf("NO\n");
        }

    }
    return 0;
}
