#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
using namespace std;

char tr[ 26 ] ;

int main()
{
/*
    memset( tr , 255 , sizeof( tr ) ) ;
    for ( int AAA = 3 ; AAA ; AAA -- )
    {
        string s , t ;
        getline( cin , s ) ;
        getline( cin , t ) ;

        for ( int i = 0 ; i < s . length() ; i ++ )
        {
            if ( s[ i ] != ' ' )
                tr[ s[ i ] - 'a' ] = t[ i ] ;
        }
    }
    for ( int i = 0 ; i < 26 ; i ++ )
        cout << "tr[ " << i << " ] = '" << ( char ) ( tr[ i ] ) << "' ;" << endl;
*/
freopen( "A-small-attempt0.in" , "r" , stdin ) ;
freopen( "A-small-attempt0.out" , "w" , stdout ) ;

tr[ 0 ] = 'y' ;
tr[ 1 ] = 'h' ;
tr[ 2 ] = 'e' ;
tr[ 3 ] = 's' ;
tr[ 4 ] = 'o' ;
tr[ 5 ] = 'c' ;
tr[ 6 ] = 'v' ;
tr[ 7 ] = 'x' ;
tr[ 8 ] = 'd' ;
tr[ 9 ] = 'u' ;
tr[ 10 ] = 'i' ;
tr[ 11 ] = 'g' ;
tr[ 12 ] = 'l' ;
tr[ 13 ] = 'b' ;
tr[ 14 ] = 'k' ;
tr[ 15 ] = 'r' ;
tr[ 16 ] = 'z' ; //q
tr[ 17 ] = 't' ;
tr[ 18 ] = 'n' ;
tr[ 19 ] = 'w' ;
tr[ 20 ] = 'j' ;
tr[ 21 ] = 'p' ;
tr[ 22 ] = 'f' ;
tr[ 23 ] = 'm' ;
tr[ 24 ] = 'a' ;
tr[ 25 ] = 'q' ; //z

    int test , T = 0 ;
    string s ;
    scanf( "%d" , &test ) ;
    getline( cin , s ) ;
    for ( ; test ; test -- )
    {
        getline( cin , s ) ;
        for ( int i = 0 ; i < s . length() ; i ++ )
            if ( s[ i ] != ' ' )
                s[ i ] = tr[ s[ i ] - 'a' ] ;
        cout << "Case #" << ++ T << ": " << s << endl;
    }
}
