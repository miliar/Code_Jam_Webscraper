#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

int a[1000];

int main() {
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    int cas;
    scanf("%d", &cas);
    for (int T = 1; T <= cas; T++) {
        int n;
        scanf("%d", &n);
        for (int i = 0; i < n; i++) {
            scanf("%d", &a[i]);
        }
        int res = 0, sum = 0
        int vmin = 0x3F3F3F3F;
        for (int i = 0; i < n; i++) {
            if (a[i] < vmin) {
                vmin = a[i];
            }
            res ^= a[i];
            sum += a[i];
        }
        printf("Case #%d: ", T);
        if (res != 0) {
            puts("NO");
        } else {
            printf("%d\n", sum - vmin);
        }
    }
}