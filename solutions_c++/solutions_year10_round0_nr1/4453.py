#include <iostream>
using namespace std;

struct list {
    int power;
    int on;
} snapper [32];

int main ()
{
    
      freopen ("A-small-attempt2.in", "r", stdin);
    freopen ("A-small-attempt2.out", "w", stdout);
    int test_case, case_no=0;
    scanf ("%d", &test_case);
   

    while ( test_case-- ) {
        int n;
        long int k;
        scanf ("%d %ld", &n, &k);

        for ( int i = 0; i < n; i++ ) {
        snapper [i].power = 0;
        snapper [i].on = 0;
        }
        snapper [0].power = 1;

        for ( int i = 0; i < k; i++ ) {
            for ( int j = 0; j < n; j++ ) {
                if ( snapper [j].power )
                    snapper [j].on = snapper [j].on ? 0 : 1;
            }
            for ( int j = 0; j < n; j++ ) {
                if ( snapper [j].power && snapper [j].on )
                    snapper [j + 1].power = 1;
                else
                    snapper [j + 1].power = 0;
            }
        }

        if ( snapper[n - 1].power && snapper [n - 1].on )
            printf ("Case #%d: ON\n", ++case_no);
        else
            printf ("Case #%d: OFF\n", ++case_no);
    }

    return 0;
}


