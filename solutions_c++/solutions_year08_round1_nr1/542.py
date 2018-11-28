#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<string>
#include<vector>
#include<map>
#include<set>

using namespace std;
vector< long long  > v1;
vector< long long  > v2;
long long  n;

int main()
{
    freopen( "al.txt" , "r" , stdin );
    freopen( "al.out" , "w" , stdout );
    
    long long   i , j , k , aCase , nCase  , tmp , result;
    scanf( "%I64d" , &nCase );
    for( i = 0; i < nCase ; i++ ){
        scanf( "%I64d" , &n );
        v1.clear();
        v2.clear();
        for( j = 0; j < n; j++ ){
            scanf( "%I64d"  , &tmp );
            v1.push_back( tmp );
        }
        for( j = 0; j < n; j++ ){
            scanf( "%I64d" , &tmp );
            v2.push_back( tmp );
        }
        sort( v1.begin() , v1.end() );
        sort( v2.begin() , v2.end() );
        for( result = 0 , j = 0; j < n; j++ )
            result += v1[ j ] * v2[ n - j - 1 ];
        printf( "Case #%I64d: %I64d\n" , i + 1 , result );
    }
    return 0;
    
}
