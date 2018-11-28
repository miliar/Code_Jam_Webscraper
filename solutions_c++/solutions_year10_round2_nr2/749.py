#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <map>
#include <algorithm>

using namespace std;

int bfs( long long C[][2], int n, int k, int b, int t );

int main()
{
    int t, tc = 0, n, k, b, time;
    scanf( "%d", &t );
    while( tc++ < t )
    {
        printf( "Case #%d: ", tc );
        scanf( "%d%d%d%d", &n, &k, &b, &time );
        long long chiks[ n ][ 2 ];
        for( int i = 0; i < n; ++i )
            scanf( "%lld", &chiks[ i ][ 0 ] ); /* xi */
        for( int i = 0; i < n; ++i )
            scanf( "%lld", &chiks[ i ][ 1 ] ); /* vi */
        int mini = bfs( chiks, n, k, b, time );
        if( mini == -1 )
            printf( "IMPOSSIBLE\n" );
        else
            printf( "%d\n", mini );
    }
    return 0;
}

class chik
{
    public:
        chik( long long C[][2], int n )
        {
            for( int i = 0; i < n; ++i )
                M.push_back( pair< int, int >( C[ i ][ 0 ], C[ i ][ 1 ] ) );
            for( int i = 0; i < n; ++i )
                mapa += 'A' + i;
            sw = 0;
        }
        chik( vector< pair< long long, long long > > &Q, int i, string g )
        {
            M = vector< pair< long long, long long > >( Q.begin(), Q.end() );
            sw = i;
            mapa = g;
        }
        int count( long long b, long long t )
        {
            int c = 0, n = M.size();
            for( int i = n - 1; i >= 0; --i )
                if( M[ i ].first + ( t * M[i].second ) < b ) /* no llega la del frente */
                    break;
                else
                    ++c;
            return c;
        }
        vector< pair< long long, long long > > M;
        string mapa;
        int sw;
};

bool operator<( const chik &a, const chik &b )
{
    return a.sw > b.sw;
}

int bfs( long long C[][2], int n, int k, int b, int t )
{
    priority_queue< chik > Q;
    map< string, int > MAP;
    Q.push( chik( C, n ) );
    while( !Q.empty() )
    {
        chik T = Q.top();
        Q.pop();
        if( T.count( b, t ) >= k )
            return T.sw;
        if( T.sw > 15 || MAP[ T.mapa ] > 1 )
            continue;
        MAP[ T.mapa ] = 2;
        for( int i = 0, s = T.M.size() - 1; i < s; ++i )
        {
            chik W( T.M, T.sw + 1, T.mapa );
            pair< long long, long long > tmp = W.M[ i ];
            W.M[ i ] = W.M[ i + 1 ];
            W.M[ i + 1 ] = tmp;
            char tmpc = W.mapa[ i ];
            W.mapa[ i ] = W.mapa[ i + 1 ];
            W.mapa[ i + 1 ] = tmpc;
            if( MAP[ W.mapa ] < 2 )
                Q.push( W );
        }
    }
    return -1;
}
