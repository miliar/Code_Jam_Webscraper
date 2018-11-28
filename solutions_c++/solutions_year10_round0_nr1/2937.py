#include <iostream>
#include <cstdio>

using namespace std;

int main() {
    int cases;

    scanf("%d", &cases);

    for (int tcase = 1; tcase <= cases; tcase++) {
        int n, k;

        scanf("%d %d", &n, &k);

        printf("Case #%d: ", tcase);

        int x = ((1 << n) - 1);
        // printf("%2d %2d - %04x = %04x    ", n, k, k & x, x);
        if ((k & x) == x) {
            printf("ON\n");
        } else {
            printf("OFF\n");
        }
    }

    return 0;
}
