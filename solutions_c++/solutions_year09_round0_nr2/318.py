#include <iostream>
#include <set>
#include <string>
#include <vector>
#include <algorithm>
#include <map>

int t, h, w;
int A[ 500 ][ 500 ];
int B[ 500 ][ 500 ];

int F[ 500 * 500 ];


int find( int f )
{
    if( F[ f ] != f ) F[ f ] = find( F[ f ] );
    return F[ f ];
}

void unite( int f , int e )
{
    f = find( f );
    e = find( e );
    if ( f&1 ) F[ f ] = e;
    else F[ e ] = f;
}

std::vector< std::pair< int , std::pair< int , int > > > list;

int dx[ 4 ] = { -1 , 0 , 0 , 1 };
int dy[ 4 ] = { 0 , -1 , 1 , 0 };

int main( )
{
    std::cin >> t;
    
    for( int test = 1 ; test <= t ; ++test ) 
    {
        std::cin >> h >> w;

        list.clear( );
                
        for( int i = 0; i < h ; ++i )
            for( int j = 0; j < w; ++j )
            {
                std::cin >> A[ i ][ j ];
                list.push_back( std::make_pair( A[ i ][ j ] , std::make_pair( i , j ) ) );
                
                B[ i ][ j ] = i * w + j;
                F[ i * w + j ] = i * w + j;
            }
        
        std::sort( list.begin( ), list.end( ) );
        
        int cnt = 0;

        for( int i = list.size( ) - 1 ; i >= 0 ; --i )
        {
            int x = list[ i ].second.first;
            int y = list[ i ].second.second;
            int height = list[ i ].first;
                       
            int hh = A[ x ][ y ];
            int ww = -1;
            
            for( int j = 0 ; j < 4 ; ++j )
            if( x + dx[ j ] >= 0 && x + dx[ j ] < h && y + dy[ j ] >= 0 && y + dy[ j ] < w && hh > A[ x + dx[ j ] ][ y + dy[ j ] ] )
            {
                ww = j;
                hh = A[ x + dx[ j ] ][ y + dy[ j ] ];
            }

            if( ww != -1 ) unite( B[ x + dx[ ww ] ][ y + dy[ ww ] ] , B[ x ][ y ] );
        }

        std::cout << "Case #" << test << ":" << std::endl;
        
        char sign = 'a';
        std::map< int , char > M;

        for( int  i = 0 ; i < h ; ++i )
        {
            for( int j = 0 ; j < w ; ++j )
            {
                if( M.find( find( B[ i ][ j ] ) ) == M.end( ) ) M[ find( B[ i ][ j ] ) ] = sign++;
                std::cout << M[ find( B[ i ][ j ] ) ];
                if( j + 1 != w ) std::cout << " ";
            }
            std::cout << std::endl;
        }
    }
    
    return 0;
}