#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

#define MAXN 11000
#define eps (1e-8)
#define INF 1000000000
#define abs(x) ( (x) > 0? (x): -(x) )
#define sqr(x) ((x) * (x))
#define MAX(a, b) ((a) > (b)? (a): (b))
#define MIN(a, b) ((a) < (b)? (a): (b))

typedef long long LL;

int n, m;
char words[MAXN][15];
int loc[MAXN][30], ex[MAXN], len[20][MAXN], order[2][MAXN];

void swap( int &x, int &y ) { int temp = x; x = y; y = temp; }

int main()
{
    int T, ca = 0;
    scanf( "%d", &T );
    while ( T-- )
    {
        memset( loc, 0, sizeof(loc) );
        memset( ex, 0, sizeof(ex) );
        memset( len, 0, sizeof(len) );
        scanf( "%d%d", &n, &m );
        for ( int i = 1; i <= n; ++i )
        {
            scanf( "%s", words[i] );
            for ( int j = 0, t = 1; words[i][j]; ++j, t *= 2 )
            {
                loc[i][words[i][j] - 'a'] |= t;
                ex[i] |= ( 1 << ( words[i][j] - 'a' ) );
            }
            int l = strlen( words[i] );
            len[l][++len[l][0]] = i;
        }
        printf( "Case #%d:", ++ca );
        while ( m-- )
        {
            char list[30];
            scanf( "%s", list );
            int maxp = 0;
            int ansi = 1;
            for ( int i = 1; i <= n; ++i )
            {
                int c = 1;
                int l = strlen( words[i] );
                int k = 0, p = 0;
                order[0][0] = len[l][0];
                for ( int j = 1; j <= len[l][0]; ++j ) 
                {
                    k |= ex[len[l][j]];
                    order[0][j] = len[l][j];
                }
                //cout << loc[i]['t' - 'a'] << endl;
                for ( int j = 0; j < 26; ++j ) if ( ( k & ( 1 << ( list[j] - 'a' ) ) ) != 0 )
                {
                    int tk = 0;
                    int cc = list[j] - 'a';
 //                   cout << i << ' ' << cc << endl;
                    if ( loc[i][cc] == 0 ) p = p + 1;
                    order[c][0] = 0;
                    for ( int id = 1; id <= order[1 - c][0]; ++id )
                    {
                        if ( loc[order[1 - c][id]][cc] == loc[i][cc] )
                        {
                            ++order[c][0];
                            order[c][order[c][0]] = order[1 - c][id];
                            tk |= ex[order[c][order[c][0]]];
                        }
                    }
                    if ( order[c][0] == 1 )
                        break;
                    c = 1 - c;
                    k = tk;
                }
                if ( p > maxp )
                {
                    maxp = p;
                    ansi = order[c][1];
                }
            }
            printf( " %s", words[ansi] );
        }
        puts( "" );
    }
    return 0;
}
