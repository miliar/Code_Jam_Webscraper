#include <cstdio>
#include <fstream>
#include <vector>

using namespace std;

const int MaxN = 1000100;

int ret[ MaxN ], offset;

vector< int > T;

int query( int i, int k )
{
    --T[i];
    if ( i >= offset ) return i - offset;
    if ( T[i * 2] >= k ) return query( i * 2, k );
    return query( i * 2 + 1, k - T[i * 2] );
}

int main( void )
{
    int t, n, k;
    ifstream in( "C-large.in" );
    ofstream out( "C.out" );
    in >> t;
    for( int R = 1; R <= t; ++R )
    {
         in >> n;
         T.clear();
         for( offset = 1; offset < n; offset *= 2 );
         T.resize( 2 * offset, 0 );
         for( int i = offset; i < n + offset; ++i )
              T[i] = 1;
         
         for( int i = offset - 1; i; --i )
              T[i] = T[i * 2] + T[i * 2 + 1];
         
         int p = 1;
         for( int i = 1; i <= n; ++i )
         {
              p += i - 1;
              p %= T[1];
              if ( !p ) p = T[1];
              ret[query( 1, p ) + 1] = i;
         } 
         in >> k;
         out << "Case #" << R << ":";
         for( int i = 1; i <= k; ++i )
         {
              int b;
              in >> b;
              out << " " << ret[b];
         }
         out << endl;
    }
    return 0;
}
