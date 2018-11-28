#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

struct replace {

    char a;
    char b;
    char c;

};

replace combine[ 100 ];
int NumCom;
replace oppose[ 100 ];
int NumOpp;

int main() {

    FILE * output = fopen( "output.txt", "w" );

    int t;
    cin >> t;
    for( int i = 1; i <= t; ++i ) {

        NumCom = 0;
        int c;
        cin >> c;
        for( int j = 1; j <= c; ++j ) {

            char a, b, c;
            cin >> a >> b >> c;

            ++NumCom;
            combine[ NumCom ].a = a;
            combine[ NumCom ].b = b;
            combine[ NumCom ].c = c;

            ++NumCom;
            combine[ NumCom ].a = b;
            combine[ NumCom ].b = a;
            combine[ NumCom ].c = c;

        }

        NumOpp = 0;
        int d;
        cin >> d;
        for( int j = 1; j <= d; ++j ) {

            char a, b;
            cin >> a >> b;

            ++NumOpp;
            oppose[ NumOpp ].a = a;
            oppose[ NumOpp ].b = b;

            ++NumOpp;
            oppose[ NumOpp ].a = b;
            oppose[ NumOpp ].b = a;

        }

        char result[ 1000 ];
        int indexOfResult = -1;
        int n;
        cin >> n;
        for( int j = 1; j <= n; ++j ) {

            char a;
            cin >> a;
            ++indexOfResult;
            result[ indexOfResult ] = a;
            result[ indexOfResult + 1 ] = '\0';

            for( int k = 1; k <= NumCom; ++k ) {
                if( ( result[ strlen( result ) - 2 ] == combine[ k ].a ) && ( result[ strlen( result ) - 1 ] == combine[ k ].b ) ) {
                    result[ strlen( result ) - 2 ] = combine[ k ].c;
                    result[ strlen( result ) - 1 ] = '\0';
                    --indexOfResult;
                    break;
                }
            }


            bool letter[ 1000 ];
            memset( letter, 0, sizeof( letter ) );
            for( int k = 0; k <= int( strlen( result ) ) - 1; ++k ) {
                letter[ result[ k ] ] = 1;
            }

            for( int k = 1; k <= NumOpp; ++k ) {
                if( ( letter[ oppose[ k ].a ] == true ) && ( letter[ oppose[ k ].b ] == true ) ) {
                    result[ 0 ] = '\0';
                    indexOfResult = -1;
                }
            }

        }

        fprintf( output, "Case #%d: [", i );

        if( strlen( result ) == 0 ) {
            fprintf( output, "]\n" );
        } else {

            fprintf( output, "%c", result[ 0 ] );
            for( int j = 1; j <= int( strlen( result ) ) - 1; ++j ) {
                fprintf( output, ", %c", result[ j ] );
            }
            fprintf( output, "]\n" );

        }

    }

    fclose( output );

    return 0;

}
