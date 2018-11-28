#include <iostream>

int main(){
	freopen ("A-large.in", "r", stdin);
	freopen ("A-large.out", "w", stdout);
	int t,n,k;
    scanf ("%d", &t);
    int cases = 0;

    while (t--) {
        scanf ("%d %d", &n, &k);

        if ( (k+1)%(1<<n) == 0 )
            printf ("Case #%d: ON\n", ++cases);
        else
            printf ("Case #%d: OFF\n", ++cases);
    }

    return 0;
}
