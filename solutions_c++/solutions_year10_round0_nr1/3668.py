/*
// @BEGIN_OF_SOURCE_CODE
// Small input : Acc

#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <vector>
#include <map>
#include <sstream>
#include <set>
#include <math.h>
#define N 1000000
using namespace std;

struct snapper {
    bool power;
    bool on;
} a [10 + 2];

void reset (int n)
{
    for ( int i = 0; i < n; i++ ) {
        a [i].power = false;
        a [i].on = false;
    }
    a [0].power = true;
}

int main ()
{
    //freopen ("A-test.in", "r", stdin);
    //freopen ("A-test.out", "w", stdout);
    int T;
    scanf ("%d", &T);
    int cases = 0;

    while ( T-- ) {
        int n;
        int k;
        scanf ("%d %d", &n, &k);

        reset (n);

        for ( int i = 0; i < k; i++ ) {
            for ( int j = 0; j < n; j++ ) {
                if ( a [j].power )
                    a [j].on = a [j].on ? false : true;
            }
            for ( int j = 0; j < n; j++ ) {
                if ( a [j].power && a [j].on )
                    a [j + 1].power = true;
                else
                    a [j + 1].power = false;
            }
        }

        if ( a [n - 1].power && a [n - 1].on )
            printf ("Case #%d: ON\n", ++cases);
        else
            printf ("Case #%d: OFF\n", ++cases);
    }

    return 0;
}

// @END_OF_SOURCE_CODE
*/
// ------------------------------------------------------------------------------
// @BEGIN_OF_SOURCE_CODE
// Large :

#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <vector>
#include <map>
#include <sstream>
#include <set>
#include <math.h>
#define N 1000000
using namespace std;


int main ()
{
    freopen ("A-large.in", "r", stdin);
    freopen ("A-large.out", "w", stdout);
    int T;
    scanf ("%d", &T);
    int cases = 0;

    while ( T-- ) {
        int n;
        int k;
        scanf ("%d %d", &n, &k);

        int power = 1;

        for ( int i = 0; i < n; i++ )
            power *= 2;

        if ( k % power == power - 1 )
            printf ("Case #%d: ON\n", ++cases);
        else
            printf ("Case #%d: OFF\n", ++cases);
    }

    return 0;
}

// @END_OF_SOURCE_CODE
