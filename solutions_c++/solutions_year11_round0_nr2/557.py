#include <cmath>
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

#define MAXN 110
#define eps (1e-8)
#define INF 1000000000
#define abs(x) ( (x) > 0? (x): -(x) )
#define sqr(x) ((x) * (x))
#define MAX(a, b) ((a) > (b)? (a): (b))
#define MIN(a, b) ((a) < (b)? (a): (b))

typedef long long LL;

int c, d, n;
char map[30][30];
bool clr[30][30];

void swap( int &x, int &y ) { int temp = x; x = y; y = temp; }

int main()
{
    int T, ca = 0;
    scanf( "%d", &T );
    while ( T-- )
    {
        memset( map, 0, sizeof(map) );
        memset( clr, 0, sizeof(clr) );
        scanf( "%d", &c );
        for ( int i = 1; i <= c; ++i )
        {
            char maps[5];
            scanf( "%s", maps );
            map[maps[0] - 'A'][maps[1] - 'A'] = maps[2];
            map[maps[1] - 'A'][maps[0] - 'A'] = maps[2];
        }
        scanf( "%d", &d );
        for ( int i = 1; i <= d; ++i )
        {
            char clrs[5];
            scanf( "%s", clrs );
            clr[clrs[0] - 'A'][clrs[1] - 'A'] = true;
            clr[clrs[1] - 'A'][clrs[0] - 'A'] = true;
        }
        scanf( "%d", &n );
        int cnt = 0;
        char inputs[MAXN], que[MAXN];
        scanf( "%s", inputs );
        for ( int i = 0; i < n; ++i )
        {
            que[++cnt] = inputs[i];
            while ( cnt > 1 && map[que[cnt] - 'A'][que[cnt - 1] - 'A'] != 0 )
            {
                que[cnt - 1] = map[que[cnt] - 'A'][que[cnt - 1] - 'A'];
                --cnt;
            }
            for ( int j = 1; j < cnt; ++j ) if ( clr[que[j] - 'A'][que[cnt] - 'A'] ) 
                cnt = 0;
        }
        printf( "Case #%d: ", ++ca );
        if ( cnt == 0 ) puts( "[]" ); else
        {
            printf( "[" );
            for ( int i = 1; i < cnt; ++i ) printf( "%c, ", que[i] );
            printf( "%c]\n", que[cnt] );
        }
    }
    return 0;
}
