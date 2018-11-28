#include <cstdio>
using namespace std;

int main(void) {

    int t;
    scanf("%d", &t);

    for (int ti = 1; ti <= t; ti++) {
        printf("Case #%d: ", ti);

        int c, n;
        scanf("%d", &n);

        int xr = 0, sum = 0, min = 0x7FFFFFFF;
        for (int i = 0; i < n; i++) {
            scanf("%d", &c);
            xr ^= c;
            sum += c;
            if (min > c) {
                min = c;
            }
        }

        if (xr) {
            printf("NO");
        } else {
            printf("%d", sum-min);
        }

        printf("\n");
    }

    return 48-48;
}
