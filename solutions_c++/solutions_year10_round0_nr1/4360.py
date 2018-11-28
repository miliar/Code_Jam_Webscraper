#include <iostream>
#define N 1000000
using namespace std;

struct snap {
	    bool power;
	    bool connected;
	} a [10 + 8];

	void reset (long n)
	{
	    for ( long i = 0; i < n; i++ ) {
	        a [i].power = false;
	        a [i].connected = false;
	    }
	    a [0].power = true;
	}

	int main ()
	{
	    freopen ("A-small-attempt3.in", "r", stdin);
	    freopen ("A-small-attempt3.out", "w", stdout);

	    long T;
	    scanf ("%d", &T);
	    long cases = 0;

	    while ( T-- ) {
	        long n;
	        long k;
	        scanf ("%d %d", &n, &k);

	        reset (n);

	        for ( long i = 0; i < k; i++ ) {
	            for ( long j = 0; j < n; j++ ) {
	                if ( a [j].power )
	                    a [j].connected = a [j].connected ? false : true;
	            }
	            for ( long j = 0; j < n; j++ ) {
	                if ( a [j].power && a [j].connected )
	                    a [j + 1].power = true;
                else
	                    a [j + 1].power = false;
	            }
	        }

	        if ( a [n - 1].power && a [n - 1].connected )
	            printf ("Case #%d: ON\n", ++cases);
         else
	            printf ("Case #%d: OFF\n", ++cases);
	    }
        return 0;
	  
	}
