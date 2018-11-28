#include <cstdio>
#include <cstring>
#include <algorithm>
#define MAXN ( 1 << 7 )
using namespace std;

struct el
{
    int x, y, d;
    el () { x = y = d = 0; }
    el (int _x, int _y, int _d) : x(_x), y(_y), d(_d) {}
};

int cmp (const el &a, const el &b)
{
    return a.d < b.d;
}

int t , brt, n, m, col, br;
int a[MAXN][MAXN] , sol[MAXN][MAXN];
el sp[MAXN*MAXN];
int dirx[4] = {  -1, 0, 0, 1};
int diry[4] = { 0,  -1, 1, 0};
char basins[32];

void clear ()
{
    memset ( a , 0 , sizeof(a));
    memset ( sol , 0 , sizeof(sol));
    for (int i=0; i < 32; ++i)
        basins[i] = ' ';

    col = br = 0;
}

el move (el f)
{
    int moved = 1;
    while ( moved && !sol[f.x][f.y] )
    {
        el ans = el ( -1,-1,f.d );
        for (int p=0; p < 4; ++p)
            if (f.x + dirx[p] >= 0 && f.x + dirx[p] < n )
            if (f.y + diry[p] >= 0 && f.y + diry[p] < m )
            {
                if( a[f.x + dirx[p]][ f.y + diry[p] ] < ans.d )
                {
                    ans.x = f.x + dirx[p];
                    ans.y = f.y + diry[p];
                    ans.d = a[f.x + dirx[p]][ f.y + diry[p] ];
                }
            }

        moved = ( ans.x != -1 );
        if (ans.x != -1) f = ans;
    }
    return f;
}

int main ()
{
    scanf ( "%d", &t );

    while ( t-- )
    {
        clear ();

        scanf ( "%d%d" , &n, &m );
        for (int i=0; i < n; ++i)
            for (int j=0; j < m; ++j)
            {
                scanf ( "%d" , &a[i][j] );
                sp[i*m + j] = el ( i , j , a[i][j] );
            }

        sort ( sp, sp + n*m, cmp );
        //printf ( "%d %d %d\n" , sp[0].x, sp[0].y, sp[0].d );

        for (int i=0;i < n*m; ++i)
        {
            el ans = move ( sp[i] );

            //printf ( "for el( %d %d %d ) the basin is el (%d %d %d)\n", sp[i].x, sp[i].y,sp[i].d , ans.x, ans.y, ans.d );
            if ( ans.x == sp[i].x && ans.y == sp[i].y && ans.d == sp[i].d )
            {
                col ++;
                sol[ sp[i].x ][ sp[i].y ] = col;
            }
            else
            {
                sol[ sp[i].x ][ sp[i].y ] = sol[ans.x][ans.y];
            }
        }

        for (int i=0; i < n; ++i)
            for (int j=0; j < m; ++j)
                if ( basins[ sol[i][j] ] == ' ' )
                {
                    basins[ sol[i][j] ]= char ((br++) + 'a');
                }

        printf ( "Case #%d:\n" , ++brt );
        for (int i=0; i < n; ++i)
        {
            for (int j=0; j < m; ++j)
                printf ( "%c " , basins[ sol[i][j] ] );
            printf ( "\n" );
        }
    }
    return 0;
}
