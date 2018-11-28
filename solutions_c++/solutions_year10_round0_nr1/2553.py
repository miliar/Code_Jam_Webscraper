#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <string>
#include <sstream>
#include <ctype.h>  // isdigit(), isalnum(), isalpha()
#include <vector>
using namespace std;

bool dbg = false;

#define DBG if( dbg )

int main( int argc, char* argv[] )
{
    // freopen("sample.txt","r",stdin);
    // freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
    // freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
    freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);

    if ( argc != 1 ) dbg = true;

    char line[1000];
    fgets(line,1000,stdin);
    int ncases = atoi(line);
    DBG printf( "ncases = %d\n", ncases );

    for ( int iCase = 0; iCase < ncases; iCase++ )
    {
        int N;
        scanf( "%d", &N );
        long int K;
        scanf( "%ld", &K );

        DBG printf( "Lei N:%d K:%ld\n", N, K );

        // snap now
        bool all_on = true;
        long int number = K;
        for ( int ii = 0; ii < N; ii++ )
        {
            DBG printf( "number: %ld\n", number );
            all_on &=  ((number % 2) == 1);
            number /= 2;
        }

        printf( "Case #%d: ", iCase+1 );
        if ( all_on )
            printf( "ON" );
        else
            printf( "OFF" );
        printf( "\n" );

    }

    return 0;
}
