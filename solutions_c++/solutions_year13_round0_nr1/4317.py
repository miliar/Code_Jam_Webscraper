// I/O Includes

#include<new>
#include<cstdio>
#include<cctype>
#include<cmath>
#include<cstdlib>
#include<cstring>
#include<sstream>
#include<iostream>
#include<strstream>

// Data Structure Includes

#include<map>
#include<set>
#include<list>
#include<stack>
#include<deque>
#include<queue>
#include<vector>
#include<bitset>
#include<string>
#include<iterator>
#include<algorithm>

// Standard Namespace Inclusion

using namespace std;

// Supporting Macros

#define SZ( C )                 ( ( int ) ( ( C ).size() ) )
#define ALL( C )                ( C ).begin() , ( C ).end()
#define TR( C , it )            for( typeof( ( C ).begin() ) it = ( C ).begin(); it != ( C ).end() ; ++it )
#define LN( STRING )            ( ( int ) ( STRING ).length() )
#define SPRESENT( C , x )       ( ( ( C ).find( x ) ) != ( C ).end() )
#define CPRESENT( C , x )       ( find( ALL( C ) , x ) != ( C ).end() )
#define PB                      push_back

// Typedefed Versions of Data Types

typedef vector< int > VI;
typedef vector< VI > VVI;
typedef vector< string > VS;
typedef pair< int ,int > PII;
typedef long long LL;
typedef unsigned long long ULL;

int main(){

    freopen("/home/ankit/Desktop/A-large.in" , "rb" , stdin);
    freopen("/home/ankit/Desktop/A-large.out" , "wb" , stdout);

    int T;
    cin >> T;

    int test = 0;

    while( T-- ){

        ++test;

        char board[ 4 ][ 4 ];

        for(int i = 0 ; i < 4 ; ++i)
            for(int j = 0 ; j < 4 ; ++j)
                cin >> board[ i ][ j ];


        vector< string > rowStrings;
        vector< string > columnStrings;
        vector< string > diagonalStrings;

        // form the vector of row strings
        for(int i = 0 ; i < 4 ; ++i){

            string rowStr = "";
            rowStr = rowStr + board[ i ][ 0 ] + board[ i ][ 1 ] + board[ i ][ 2 ] + board[ i ][ 3 ];

            rowStrings.PB( rowStr );
        }

        // form the vector of column strings
        for(int i = 0 ; i < 4 ; ++i){

            string colStr = "";
            colStr = colStr + board[ 0 ][ i ] + board[ 1 ][ i ] + board[ 2 ][ i ] + board[ 3 ][ i ];

            columnStrings.PB( colStr );
        }

        // form the vector of diagonal strings
        string diagStr = "";
        diagStr = diagStr + board[ 0 ][ 0 ] + board[ 1 ][ 1 ] + board[ 2 ][ 2 ] + board[ 3 ][ 3 ];

        diagonalStrings.PB( diagStr );

        diagStr = "";
        diagStr = diagStr + board[ 0 ][ 3 ] + board[ 1 ][ 2 ] + board[ 2 ][ 1 ] + board[ 3 ][ 0 ];

        diagonalStrings.PB( diagStr );

        // check if X won or not
        bool xWon = false;

        for(int i = 0 ; i < SZ( rowStrings ) ; ++i){

            int count = 0;

            for(int j = 0 ; j < LN( rowStrings[ i ] ) ; ++j){

                if( rowStrings[ i ].at( j ) == 'X' )
                    ++count;
            }

            if( count == 4 || ( count == 3 && rowStrings[ i ].find('T') != string::npos ) ){

                xWon = true;
                break;

            }
        }


        for(int i = 0 ; i < SZ( columnStrings ) ; ++i){

            int count = 0;

            for(int j = 0 ; j < LN( columnStrings[ i ] ) ; ++j){

                if( columnStrings[ i ].at( j ) == 'X' )
                    ++count;
            }

            if( count == 4 || ( count == 3 && columnStrings[ i ].find('T') != string::npos ) ){

                xWon = true;
                break;
            }
        }


        for(int i = 0 ; i < SZ( diagonalStrings ) ; ++i){

            int count = 0;

            for(int j = 0 ; j < LN( diagonalStrings[ i ] ) ; ++j){

                if( diagonalStrings[ i ].at( j ) == 'X' )
                    ++count;
            }

            if( count == 4 || ( count == 3 && diagonalStrings[ i ].find('T') != string::npos ) ){

                xWon = true;
                break;
            }
        }

        if( xWon ){

            cout << "Case #" << test << ": X won" << endl;
            continue;
        }

        // check if O won or not
        bool oWon = false;

        for(int i = 0 ; i < SZ( rowStrings ) ; ++i){

            int count = 0;

            for(int j = 0 ; j < LN( rowStrings[ i ] ) ; ++j){

                if( rowStrings[ i ].at( j ) == 'O' )
                    ++count;
            }

            if( count == 4 || ( count == 3 && rowStrings[ i ].find('T') != string::npos ) ){

                oWon = true;
                break;

            }
        }


        for(int i = 0 ; i < SZ( columnStrings ) ; ++i){

            int count = 0;

            for(int j = 0 ; j < LN( columnStrings[ i ] ) ; ++j){

                if( columnStrings[ i ].at( j ) == 'O' )
                    ++count;
            }

            if( count == 4 || ( count == 3 && columnStrings[ i ].find('T') != string::npos ) ){

                oWon = true;
                break;
            }
        }


        for(int i = 0 ; i < SZ( diagonalStrings ) ; ++i){

            int count = 0;

            for(int j = 0 ; j < LN( diagonalStrings[ i ] ) ; ++j){

                if( diagonalStrings[ i ].at( j ) == 'O' )
                    ++count;
            }

            if( count == 4 || ( count == 3 && diagonalStrings[ i ].find('T') != string::npos ) ){

                oWon = true;
                break;
            }
        }

        if( oWon ){

            cout << "Case #" << test << ": O won" << endl;
            continue;
        }

        // check if the game has not ended yet
        bool checkPeriod = false;

        if( !xWon && !oWon ){

            for(int i = 0 ; i < 4 ; ++i){
                for(int j = 0 ; j < 4 ; ++j){

                    if( board[ i ][ j ] == '.' ){
                        checkPeriod = true;
                        break;
                    }
                }

                if( checkPeriod )
                    break;
            }

            if( checkPeriod ){
                cout << "Case #" << test << ": Game has not completed" << endl;
                continue;
            }

            else{
                cout << "Case #" << test << ": Draw" << endl;
                continue;
            }

        }

    }

    getchar();
    getchar();

    return 0;
}
