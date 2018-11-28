#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
int n, k;
int main()
{
    int tc, cn;
    int i, j;
    int fl;
    int state;
    scanf("%d", &tc);
    for (cn = 1; cn <= tc; cn++) {
        scanf("%d%d", &n, &k);
        state = 0;
        for (i = 0; i < k; i++) {
            fl = 1;
            for (j = 0; j < n && fl; j++) {
                if (((1 << j) & state) == 0) {
                    fl = 0;
                    state |= (1 << j);
                }
                else {
                    state -= (1 << j);
                }
            }
        }
        if (state == (1 << n) - 1) {
            printf("Case #%d: ON\n", cn);
        }
        else {
            printf("Case #%d: OFF\n", cn);
        }
    }
    return 0;
}
