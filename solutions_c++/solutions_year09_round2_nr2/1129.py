#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>

using namespace std ;

char s[ 100 ] ;
int cnt[ 10 ] ;

int main( )
{
    int Ncase ;

    //freopen( "in.txt" , "r" , stdin ) ;
    //freopen( "out.txt" , "w" , stdout ) ;
    
    scanf( "%d" , &Ncase ) ;
    gets( s ) ;
    
    for( int N = 1 ; N <= Ncase ; ++ N )
    {
        memset( s , 0 , sizeof( s ) ) ;
        gets( s ) ;
        memset( cnt , 0 , sizeof( cnt ) ) ;
        int i , l = strlen( s ) ;
        for( i = l - 1 ; i >= 0 ; i -- )
        {
            int x = s[ i ] - '0' ;
            bool find = false ;
            for( int j = x + 1 ; j < 10 ; j ++ )
            {
                if( cnt[ j ] > 0 )
                {
                    find = true ;
                    cnt[ j ] -- ;
                    cnt[ x ] ++ ;
                    s[ i ] = j + '0' ;
                    break ;
                }
            }
            if( find )  break ;
            cnt[ x ] ++ ;
            
            if( i == 0 )
            {
                cnt[ 0 ] ++ ;
                for( int j = 1 ; j < 10 ; j ++ )
                     if( cnt[ j ] > 0 )
                     {
                         cnt[ j ] -- ;
                         s[ 0 ] = j + '0' ;
                         break ;
                     }
                break ;
            }
        }
        for( int j = 0 ; j < 10 ; j ++ )
             while( cnt[ j ] -- ) s[ ++ i ] = j + '0' ;
        
        printf( "Case #%d: %s\n" , N , s ) ;
    }
    
    return 0 ;
}
