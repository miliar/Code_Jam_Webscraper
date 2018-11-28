
#include <stdio.h>
int main () 
{
        int t;
	int j;
        scanf ( "%d", &t );
        for ( j = 1; j <= t; j++ ) {
        int n;
	int s;
	int p;
	int sum = 0;
	int i;
        scanf ( "%d%d%d", &n, &s, &p);
        int arr[n+1];
        for ( i = 0 ; i < n; i++ ) {
        scanf ( "%d", &arr[i] );
                if ( arr[i] >= 3 * p - 2 )
        sum++;
                
        else if (( arr[i] >= (3*p-4)) && (arr[i]<3*p-2 )) {
         if ( s > 0&&arr[i]>0) {
                s--;
                sum++;
        }
        }
        }
        printf ( "Case #%d: %d\n",j,sum);
        }
        return 0;
}