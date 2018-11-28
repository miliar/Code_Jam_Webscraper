#include <cstdlib>
#include <cstdio>
#include <iostream>

using namespace std;

int main() {
    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; ++i) {
        int n, sumaXor = 0, min = 10000000, sumaR = 0;
        scanf("%d", &n);

        while (n--) {
            int x;
            scanf("%d", &x);
            sumaXor ^= x;
            sumaR += x;
            if (x < min)
                min = x;
        }

        if (sumaXor != 0)
            printf("Case #%d: NO\n", i);
        else
            printf("Case #%d: %d\n", i, (sumaR-min) );

    }
    return 0;
}
