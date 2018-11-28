#include <stdio.h>
#include<stdlib.h>


int main() {

    //freopen ( "C:\\A.in", "r", stdin );
    //freopen ( "C:\\A.out", "w", stdout );
    int T, k;
    int l, p, c;
    int ans, sum;
    scanf ( "%d", &T );
    for ( k = 1; k <= T; k++ ) {
        ans = 0;
        sum = 0;
        scanf ( "%d %d %d", &l, &p, &c );

        while ( l  < p )
        {
            l *= c;
            ans++;
        }
        ans--;
        while ( ans )
        {
            sum++;
            ans /= 2;
        }
        printf ( "Case #%d: %d\n", k, sum );
    }
    return 0;
}
