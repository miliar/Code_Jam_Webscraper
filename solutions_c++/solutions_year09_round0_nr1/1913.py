#include<cctype> 
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>

using namespace std ;

bool valid[ 20 ][ 30 ] ;
char ch , s[ 5010 ][ 20 ] ;
int l , d , n ;

int main( )
{    
    scanf( "%d %d %d" , &l , &d , &n ) ;
    for( int i = 0 ; i < d ; i ++ )
          scanf( "%s" , &s[ i ] ) ;
    for( int cnt = 1 ; cnt <= n ; ++ cnt )
    {
        int ans = 0 ;
        memset( valid , false , sizeof( valid ) ) ;
        for( int i = 0 ; i < l ; i ++ )
        {
            while( 1 )
            {
                ch = getchar( ) ;
                if( ch >= 'a' && ch <= 'z' )
                {
                    valid[ i ][ ch - 'a' ] = true ;
                    break ;
                }
                else if( ch == '(' )
                {
                    while( 1 )
                    {
                        ch = getchar( ) ;
                        if( ch >= 'a' && ch <= 'z' )
                            valid[ i ][ ch - 'a' ] = true ;
                        if( ch == ')' ) break ;
                    }
                    break ;
                }
            }
        }
        for( int j = 0 ; j < d ; j ++ )
        {
                bool same = true ;
                for( int k = 0 ; k < l ; k ++ )
                     if( !valid[ k ][ s[ j ][ k ] - 'a' ] ) same = false ;
                if( same ) ans ++ ;
        }
        printf( "Case #%d: %d\n" , cnt , ans ) ;
    }

    return 0 ;
}
