#include <cstdio>
#include <algorithm>
using namespace std;

int main() {
    freopen("A.out", "w", stdout);
    int cas = 0;
    int t = 0;
    scanf("%d", &cas);
    while (cas--) {
        printf("Case #%d: ", ++t);
        int n = 0, k = 0;
        scanf("%d %d", &n, &k);
        int ans = (k + 1) % (1 << n);
        if (0 == ans) {
            printf("ON\n");
        }
        else {
            printf("OFF\n");
        }
    }
    return 0;
}
