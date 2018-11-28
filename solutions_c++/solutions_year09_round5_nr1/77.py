#include <algorithm>
#include <vector>
#include <string>
#include <queue>
#include <map>

#include <cstdio>
#include <cstring>
#include <cmath>

using namespace std;

const int MAX = 15;

const int dx[4] = { -1, 0, 1, 0 };
const int dy[4] = { 0, -1, 0, 1 };

int R, S, n;

char grid[ MAX ][ MAX ];
char goal[ MAX ][ MAX ];

queue< long long > Q;
map< long long, int > dist;
map< long long, bool > memo;

pair< int, int > niz[100];
pair< int, int > tmp[100];

int cookie = 1;
int ima[ MAX ][ MAX ];

int dset[100];
int find( int x ) { if( x == dset[x] ) return x; return dset[x] = find( dset[x] ); }
void merge( int a, int b ) { a = find( a ); b = find( b ); if( a != b ) dset[a] = b; }

inline void unpack( long long state )
{
    ++cookie;

    for( int i = n-1; i >= 0; --i ) {
        niz[i].second = state % 16; state /= 16;
        niz[i].first = state % 16; state /= 16;
        ima[ niz[i].first ][ niz[i].second ] = cookie;
    }
}

inline long long pack()
{
    long long ret = 0;

    for( int i = 0; i < n; ++i ) {
        ret = ret * 16 + tmp[i].first;
        ret = ret * 16 + tmp[i].second;
    }

    return ret;
}

bool danger( long long state )
{
    if( memo.count( state ) ) return memo[state];

    for( int i = 0; i < n; ++i )
        dset[i] = i;

    for( int p = 0; p < n; ++p ) {
        for( int d = 0; d < 4; ++d ) {
            int x = tmp[p].first + dx[d];
            int y = tmp[p].second + dy[d];

            for( int i = 0; i < n; ++i )
                if( x == tmp[i].first && y == tmp[i].second )
                    merge( p, i );
        }
    }

    bool ret = false;

    for( int i = 0; i < n; ++i )
        if( find( i ) != find( 0 ) )
            ret = true;

    return memo[state] = ret;
}

void printaj()
{
    char t[ MAX ][ MAX ];
    memset( t, 0, sizeof t );

    for( int i = 0; i < R; ++i )
        for( int j = 0; j < S; ++j ) {
            t[i][j] = grid[i][j];
            if( t[i][j] == 'o' ) t[i][j] = '.';
        }

    for( int i = 0; i < n; ++i )
        t[ niz[i].first ][ niz[i].second ] = 'o';

    for( int i = 0; i < R; ++i )
        puts( t[i] );
}

int solve()
{
    long long start = 0;
    long long finish = 0;

    for( int i = 0; i < R; ++i )
        for( int j = 0; j < S; ++j ) {
            if( grid[i][j] == 'o' ) {
                start = start * 16 + i;
                start = start * 16 + j;
            }

            if( goal[i][j] == 'x' ) {
                finish = finish * 16 + i;
                finish = finish * 16 + j;
            }
        }

    if( start == finish ) return 0;

    for( ; !Q.empty(); Q.pop() );
    dist.clear();
    memo.clear();

    Q.push( start );
    dist[start] = 0;
    memo[start] = false;

    for( ; !Q.empty(); Q.pop() ) {
        long long sad = Q.front();
        unpack( sad );

        for( int p = 0; p < n; ++p ) {
            for( int d = 0; d < 4; ++d ) {
                int x = niz[p].first + dx[d];
                int y = niz[p].second + dy[d];
                int x0 = x - 2*dx[d];
                int y0 = y - 2*dy[d];

                if( x < 0 || x >= R || x0 < 0 || x0 >= R ) continue;
                if( y < 0 || y >= S || y0 < 0 || y0 >= S ) continue;
                if( grid[x][y] == '#' || grid[x0][y0] == '#' ) continue;
                if( ima[x][y] == cookie || ima[x0][y0] == cookie ) continue;

                for( int i = 0; i < n; ++i )
                    tmp[i] = niz[i];

                tmp[p] = pair< int, int >( x, y );
                sort( tmp, tmp + n );
                long long nov = pack();

                if( nov == finish ) return dist[sad] + 1;
                if( danger( nov ) && memo[sad] ) continue;

                if( dist.count( nov ) == 0 ) {
                    dist[nov] = dist[sad] + 1;
                    Q.push( nov );
                }
            }
        }
    }

    return -1;
}

int main( void )
{
    int test; scanf( "%d", &test );

    for( int t = 0; t < test; ++t ) {
        scanf( "%d %d", &R, &S );
        n = 0;

        memset( grid, 0, sizeof grid );
        memset( goal, 0, sizeof goal );

        for( int i = 0; i < R; ++i )
            scanf( "%s", grid[i] );

        for( int i = 0; i < R; ++i )
            for( int j = 0; j < S; ++j ) {
                goal[i][j] = grid[i][j];

                if( goal[i][j] == 'o' )
                    goal[i][j] = '.';
                else if( goal[i][j] == 'w' ) {
                    goal[i][j] = 'x';
                    grid[i][j] = 'o';
                }

                if( grid[i][j] == 'x' ) grid[i][j] = '.';
                if( grid[i][j] == 'o' ) ++n;
            }

        printf( "Case #%d: %d\n", t+1, solve() );
    }

    return 0;
}

