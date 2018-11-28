


#include <stdio.h>
 int main () {
 int t,j;
 scanf ( "%d", &t );
 for ( j = 1; j <= t; j++ ) {
 int n, s, p1, summ2 = 0, i;
 scanf ( "%d%d%d", &n, &s, &p1);
 int a[n+1];
 for ( i = 0 ; i < n; i++ ) {
 scanf ( "%d", &a[i] );
 if ( a[i] >= 3 * p1 - 2 )
 summ2++;

 else if (( a[i] >= ( 3 * p1 - 4 ) ) && ( a[i] < 3 * p1 - 2 )) {
 if ( s > 0&&a[i]>0) {
 s--;
 summ2++;
 }
 }
 }
 printf ( "Case #%d: %d\n",j,summ2);
 }
 return 0;
 }





