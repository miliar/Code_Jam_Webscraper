#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    int n, k, j,  aa, nn, t, i, on;
    scanf("%d",&nn);
    for (aa = 1; aa<=nn; ++aa) {
        scanf("%d %d",&n,&k);
        on = 1;
        for ( i = 1; on && i <= n; ++i ) {
            t = 1 << i;
            j = k % t;
            t >>= 1;
            if ( j < t ) on = 0;
        }
        if ( on )
            printf("Case #%d: ON\n",aa);
        else
            printf("Case #%d: OFF\n",aa);
    }
    return 0;
}

