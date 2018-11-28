#include<cstdio>
#include<string>
#include<map>
#include<cstdlib>
using namespace std;

int s , q;
map < string , int > name;

int main()
{
//    freopen( "A-small-attemp2.in" , "r" , stdin );
//    freopen( "a-small-attemp2.out" , "w" , stdout );
    freopen( "A-large.in" , "r" , stdin );
    freopen( "A-large.out" , "w" , stdout );
    int i , j  ,k , a_case , n_case , cnt , result;
    char buf[ 200 ];
    scanf( "%d" , &n_case );
    for( a_case  = 1;  a_case <= n_case; a_case++ ){
        scanf( "%d" , &s );
        name.clear();
        for( i = 0;  i < s; i++ ){
            scanf( " %[^\n]" , buf );
            name[ string( buf ) ] = 0;
        }
        scanf( "%d" , &q );
        for( result = 0 ,  cnt = 0 , i = 0; i < q; i++ ){
            scanf( " %[^\n]" , buf );
            if( name[ string( buf ) ] == 0 ){
                if( cnt == s - 1 ){
                    for( map< string , int > ::iterator itr = name.begin(); itr != name.end(); ++itr )
                        itr->second = 0;
                    result++;
                    cnt = 0;
                }
                cnt++;
                name[ string( buf ) ] = 1;
            }
        }
        printf( "Case #%d: %d\n" , a_case , result );
    }
//    while( 1 );
    return 0;
}

    
            
        
            
            
            
                
                
            
            
        
        
