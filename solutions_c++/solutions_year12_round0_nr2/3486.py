 
#include <stdio.h>
int main () {
        int t,j;
        scanf ( "%d", &t );
        for ( j = 1; j <= t; j++ ) {
        int n, s, p, sum = 0, i;
        scanf ( "%d%d%d", &n, &s, &p);
        int a[n+1];
        for ( i = 0 ; i < n; i++ ) {
        scanf ( "%d", &a[i] );
                if ( a[i] >= 3 * p - 2 )
        sum++;
                
        else if (( a[i] >= ( 3 * p - 4 ) ) && ( a[i] < 3 * p - 2 )) {
         if ( s > 0&&a[i]>0) {
                s--;
                sum++;
        }
        }
        }
        printf ( "Case #%d: %d\n",j,sum);
        }
        return 0;
}