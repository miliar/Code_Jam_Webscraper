#include<stdio.h>
#include<string.h>



int N;

char data[ 2003 ];

char mapping[ 33 ] ;


void mmap( char a, char b )
{
        mapping[ a - 'a' ] = b - 'a';
}
int main ( )
{
        gets( data );
        sscanf( data, "%d", &N );

        for( int i = 0; i < 26; i ++ ) mapping[ i ] = i ;
        mmap( 'a', 'y' );
        mmap( 'b', 'h' );
        mmap( 'c', 'e' );
        mmap( 'd', 's' );
        mmap( 'e', 'o' );
        mmap( 'f', 'c' );
        mmap( 'g', 'v' );
        mmap( 'h', 'x' );
        mmap( 'i', 'd' );
        mmap( 'j', 'u' );
        mmap( 'k', 'i' );
        mmap( 'l', 'g' );
        mmap( 'm', 'l' );
        mmap( 'n', 'b' );
        mmap( 'o', 'k' );
        mmap( 'p', 'r' );
        mmap( 'q', 'z' );
        mmap( 'r', 't' );
        mmap( 's', 'n' );
        mmap( 't', 'w' );
        mmap( 'u', 'j' );
        mmap( 'v', 'p' );
        mmap( 'w', 'f' );
        mmap( 'x', 'm' );
        mmap( 'y', 'a' );
        mmap( 'z', 'q' );


        for( int i = 1; i <= N; i ++ )
        {
                gets( data );
                for( int j = 0 ; j < strlen( data ); j ++ )
                {
                        if( data[ j ] >= 'A' && data[ j ] <= 'Z' )
                                data[ j ] = mapping[ data[ j ] - 'A' ] + 'A' ;
                        if( data[ j ] >= 'a' && data[ j ] <= 'z' )
                                data[ j ] = mapping[ data[ j ] - 'a' ] + 'a' ;

                }
                printf("Case #%d: ", i );
                printf("%s\n", data );
        }

        return 0;
}
