#include <cstdio>
#include <cmath>
#include <iostream>
#include <cstring>
using namespace std;
int a[1000010];

int main() {
  //  freopen("C-large.in", "r", stdin);
  //  freopen("c.out", "w", stdout);
    int T, n, cas = 1;
    scanf("%d", &T);
    while (T--) {
        int ans = 0, tot = 0, mi = 10000000;
        scanf("%d", &n);
        for (int i = 0; i < n; ++i) {
            scanf("%d", &a[i]);
            ans ^= a[i];
            tot += a[i];
            if (a[i] < mi) {
                mi = a[i];
            }
        }
        if (ans) {
            printf("Case #%d: NO\n", cas++);
        } else {
            printf("Case #%d: %d\n", cas++, tot - mi);
        }
    }
  //  system("pause");
    return 0;
}
