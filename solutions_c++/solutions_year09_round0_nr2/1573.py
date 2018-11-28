#include <cstdio>
#include <iostream>
#include <cstring>

using namespace std;

int  a[101][101];
char m[101][101];
int h, w;
char next;

int const dx[] = { 0, -1, 1, 0 };
int const dy[] = { -1, 0, 0, 1 };

char dfs(int i, int j)
{
//    cout << "dfs(" << i << ',' << j << ")\n";

    if( m[i][j] )
        return m[i][j];

    int mn = 1<<29;
    int bk = -1;

    for( int k = 0; k != 4; ++k )
    {
        int y = i + dy[k];
        int x = j + dx[k];

        if( y < 0 || y >= h || x < 0 || x >= w )
            continue;
        if( a[y][x] >= a[i][j] )
            continue;

        if( a[y][x] < mn )
        {
            mn = a[y][x];
            bk = k;
        }
    }

    if( bk == -1 )
        return m[i][j] = next++;
    else
        return m[i][j] = dfs(i + dy[bk], j + dx[bk]);

}

void solve()
{
    for( int i = 0; i != h; ++i )
    for( int j = 0; j != w; ++j )
        if( !m[i][j] )
            dfs(i, j);
}

int main()
{
    int T;
    scanf("%d", &T);

    for( int C = 1; C <= T; ++C )
    {
        scanf("%d %d", &h, &w);
        for( int i = 0; i != h; ++i )
        for( int j = 0; j != w; ++j )
            scanf("%d", &a[i][j]);

        memset(m, 0, sizeof(m));
        next = 'a';
        solve();

        printf("Case #%d:\n", C);
        for( int i = 0; i != h; ++i )
        {            
            for( int j = 0; j != w; ++j )
                printf("%.*s%c", !!j, " ", m[i][j]);
            printf("\n");
        }
    }

    return 0;
}
