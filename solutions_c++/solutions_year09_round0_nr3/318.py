#include <iostream>
#include <set>
#include <string>
#include <vector>
#include <algorithm>
#include <map>

int DP[ 5001 ][ 20 ];
char word[ 10000 ];

int main( )
{
    int t;
    std::string text = "welcome to code jam";
    
    gets( word );
    sscanf( word , "%d" , &t );
    
    for( int test = 1 ; test <= t ; ++test )
    {
        gets( word );
        
        int n = strlen( word );
        
        for( int i = 0 ; i < n ; ++i )
            for( int j = 0 ; j < 20 ; ++j )
                DP[ i ][ j ] = 0;
        
        DP[ 0 ][ 0 ] = 1;
        
        for( int i = 1 ; i <= n ; ++i )
        {
            DP[ i ][ 0 ] = 1;
            for( int j = 1; j <= 19 ; ++j )
            {
                DP[ i ][ j ] = DP[ i - 1 ][ j ];
                if( text[ j - 1 ] == word[ i - 1 ] )
                    DP[ i ][ j ] = (DP[ i ][ j ] + DP[ i - 1 ][ j - 1 ]) % 10000;
            }
        }
        printf( "Case #%d: %.4d\n", test, DP[ n ][ 19 ] );
    }
    
    return 0;
}