#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

int stringToNumber( char * s ) {

    int result = 0;
    for( int i = 0; i <= strlen( s ) - 1; ++i ) {
        result *= 10;
        result += s[ i ] - '0';
    }

    return result;

}

int main() {

    FILE * out = fopen( "output.txt", "w" );

    int t;
    cin >> t;
    for( int i = 1; i <= t; ++i ) {

        int nubmerOfButtons;
        cin >> nubmerOfButtons;

        int o[ 200 ];
        int b[ 200 ];
        int order[ 110 ];
        int indexOfO = 0;
        int indexOfB = 0;
        int indexOfOrder = 0;

        for( int j = 1; j <= nubmerOfButtons; ++j ) {

            char robot;
            cin >> robot;
            char button[ 10 ];
            cin >> button;

            order[ ++indexOfOrder ] = robot;

            if( robot == 'O' ) {
                o[ ++indexOfO ] = stringToNumber( button );
            } else {
                b[ ++indexOfB ] = stringToNumber( button );
            }

        }

        int po = 1;
        int pb = 1;
        indexOfO = 1;
        indexOfB = 1;
        int numorder = indexOfOrder;
        indexOfOrder = 1;

        int CurTask = order[ 1 ];
        for( int j = 1; j <= 2147483647; ++j ) {

            if( indexOfOrder >= numorder + 1 ) {
                fprintf( out, "Case #%d: %d\n", i, j - 1 );
                break;
            }

            if( CurTask == 'O' ) {

                if( o[ indexOfO ] > po ) {
                    ++po;
                } else if( o[ indexOfO ] < po ) {
                    --po;
                } else {
                    ++indexOfO;
                    CurTask = order[ ++indexOfOrder ];
                }

                if( b[ indexOfB ] > pb ) {
                    ++pb;
                } else if( b[ indexOfB ] < pb ) {
                    --pb;
                }

            } else {

                if( b[ indexOfB ] > pb ) {
                    ++pb;
                } else if( b[ indexOfB ] < pb ) {
                    --pb;
                } else {
                    ++indexOfB;
                    CurTask = order[ ++indexOfOrder ];
                }

                if( o[ indexOfO ] > po ) {
                    ++po;
                } else if( o[ indexOfO ] < po ) {
                    --po;
                }

            }

        }

    }

    return 0;

}
