#include <cstdio>
#include <cassert>
#include <algorithm>
using std::swap;

int main() {
    int t, T, n;
    int i, j;
    int a[50];
    char buf[50];

    scanf("%d", &T);
    for (t = 1; t <= T; t++) {
        printf("Case #%d: ", t);
        scanf("%d", &n);
        for (i = 0; i < n; i++) {
            scanf("%s", buf);
            //printf("%s\n", buf);
            a[i] = 0;
            for (j = 0; j < n; j++)
                if (buf[j] == '1') a[i] = j;
            //printf("%d ", a[i]);
        }
        //printf("\n");
        int ans = 0;
        for (i = 0; i < n; i++) {
            if (a[i] <= i) continue;
            for (j = i + 1; j < n; j++)
                if (a[j] <= i) break;
            assert(j != n);
            for ( ; j > i; j--) {
                swap(a[j], a[j - 1]);
                ans++;
            }
        }
        printf("%d\n", ans);
    }
}
