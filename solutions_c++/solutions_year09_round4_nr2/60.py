#include <algorithm>
#include <vector>
#include <string>
#include <queue>

#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;

const int MAX = 52;

int R, S, F;

char grid[ MAX ][ MAX ];

int dist[ MAX ][ MAX ][ MAX ][ MAX ];

struct state {
    int a, b;
    int l, r;
    int d;

    state() {}
    state( int _a, int _b, int _l, int _r, int _d ) { a = _a; b = _b; l = _l; r = _r; d = _d; }

    inline int &ref() { return dist[a][b][l][r]; }

    friend bool operator < ( const state &A, const state &B ) {
        return A.d > B.d;
    }
};

int visina( int a, int b )
{
    for( int i = a+1; i < R; ++i )
        if( grid[i][b] == '#' )
            return i - a - 1;

    return R-1 - a;
}

void update( priority_queue< state > &pq, state S )
{
    if( S.ref() != -1 && S.ref() <= S.d ) return;
    S.ref() = S.d;
    pq.push( S );
}

inline bool valid( state &sad, int a, int b, bool rupa = true )
{
    if( b < 0 || b >= S ) return false;
    if( rupa && grid[a+1][b] == '.' ) return false;
    if( grid[a][b] == '.' ) return true;
    return sad.l <= b && b < sad.r;
}

int main( void )
{
    int test; scanf( "%d", &test );

    for( int t = 0; t < test; ++t ) {
        scanf( "%d %d %d", &R, &S, &F );

        for( int i = 0; i < R; ++i )
            scanf( "%s", grid[i] );

        memset( dist, -1, sizeof dist );
        priority_queue< state > pq;

        state start( 0, 0, 0, 0, 0 );
        start.ref() = 0;
        pq.push( start );

        int sol = -1;

        while( !pq.empty() ) {
            state sad = pq.top(); pq.pop();
            if( sad.d > sad.ref() ) continue;

            if( sad.a == R-1 ) {
                sol = sad.ref();
                break;
            }

            if( grid[sad.a+1][sad.b] == '.' ) {
                int h = visina( sad.a, sad.b );
                if( h < F ) update( pq, state( sad.a+h, sad.b, 0, 0, sad.ref() ) );
            }
            else {
                for( int d = -1; d <= 1; d += 2 )
                    if( valid( sad, sad.a, sad.b+d, false ) ) {
                        if( grid[sad.a+1][sad.b+d] == '.' )
                            update( pq, state( sad.a+1, sad.b+d, 0, 0, sad.ref() ) );
                        else
                            update( pq, state( sad.a, sad.b+d, sad.l, sad.r, sad.ref() ) );
                    }

                if( valid( sad, sad.a, sad.b-1 ) )
                    for( int i = sad.b; i < S && valid( sad, sad.a, i ); ++i )
                        update( pq, state( sad.a+1, i-1, sad.b-1, i, sad.ref() + i-sad.b+1 ) );

                if( valid( sad, sad.a, sad.b+1 ) )
                    for( int i = sad.b; i >= 0 && valid( sad, sad.a, i ); --i )
                        update( pq, state( sad.a+1, i+1, i+1, sad.b+2, sad.ref() + sad.b-i+1 ) );
            }
        }

        if( sol == -1 )
            printf( "Case #%d: No\n", t+1 );
        else
            printf( "Case #%d: Yes %d\n", t+1, sol );
    }

    return 0;
}

