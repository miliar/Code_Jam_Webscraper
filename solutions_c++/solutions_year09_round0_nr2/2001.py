#include<cmath>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<iostream>

#define maxn 110

using namespace std ;

int alt[ maxn ][ maxn ] , q[ 10010 ][ 2 ] , h , t ;
char ans[ maxn ][ maxn ] , type ;

int dir[ 4 ][ 2 ] = { {-1,0} , {0,-1} , {0,1} , {1,0} } ;
int Ncase , m , n ;

void doit( int x , int y ) ;

int main( )
{                    
    scanf( "%d" , &Ncase ) ;
    for( int cnt = 1 ; cnt <= Ncase ; ++ cnt )
    {
        scanf( "%d %d" , &m , &n ) ;
        for( int i = 1 ; i <= m ; i ++ )
           for( int j = 1 ; j <= n ; j ++ ) scanf( "%d" , &alt[ i ][ j ] ) ;
        memset( ans , 0 , sizeof( ans ) ) ;
        type = 'a' - 1 ;
        for( int i = 1 ; i <= m ; i ++ )
             for( int j = 1 ; j <= n ; j ++ )
                  if( !ans[ i ][ j ] )
                  {
                      int x = i , y = j ;
                      while( 1 )
                      {
                          int r = -1 , H = alt[ x ][ y ] ;
                          for( int k = 0 ; k < 4 ; k ++ )
                          {
                              int X = x + dir[ k ][ 0 ] , Y = y + dir[ k ][ 1 ] ;
                              if( X == 0 || X > m || Y == 0 || Y > n ) continue ;
                              if( alt[ X ][ Y ] < H )
                              {
                                  r = k ;
                                  H = alt[ X ][ Y ] ;
                              }
                          }
                          if( r == -1 )
                          {
                              ans[ x ][ y ] = ++ type ;
                              doit( x , y ) ;
                              break ;
                          }    
                          else { x += dir[ r ][ 0 ] ; y += dir[ r ][ 1 ] ; }
                      }
                  }
        
        printf( "Case #%d:\n" , cnt ) ;
                                      
        for( int i = 1 ; i <= m ; i ++ )
           for( int j = 1 ; j <= n ; j ++ )
           {
               printf( "%c" , ans[ i ][ j ] ) ;
               if( j == n && i != m ) printf( "\n" ) ; else printf( " " ) ;
           }
        
        if( cnt != Ncase ) printf( "\n" ) ;
    }
    
    return 0 ;
}

void doit( int x , int y )
{
    h = t = 0 ;
    ++ t ;
    q[ t ][ 0 ] = x ;
    q[ t ][ 1 ] = y ;
    while( h != t )
    {
        ++ h ;
        x = q[ h ][ 0 ] ;
        y = q[ h ][ 1 ] ;
        for( int i = 0 ; i < 4 ; i ++ )
        {
            int X = x + dir[ i ][ 0 ] , Y = y + dir[ i ][ 1 ] ;
            if( X == 0 || X > m || Y == 0 || Y > n || ans[ X ][ Y ] ) continue ;
            int r = -1 , H = alt[ X ][ Y ] ;
            for( int j = 0 ; j < 4 ; j ++ )
            {
                int xx = X + dir[ j ][ 0 ] , yy = Y + dir[ j ][ 1 ] ;
                if( xx == 0 || xx > m || yy == 0 || yy > n ) continue ;
                if( alt[ xx ][ yy ] < H )
                {
                    r = j ;
                    H = alt[ xx ][ yy ] ;
                }
            }
            if( r != -1 && X + dir[ r ][ 0 ] == x && Y + dir[ r ][ 1 ] == y )
            {
                ans[ X ][ Y ] = type ;
                ++ t ;
                q[ t ][ 0 ] = X ;
                q[ t ][ 1 ] = Y ;
            }
        }
    }
}
