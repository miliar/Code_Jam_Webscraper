#include <cstdio>
#include <cstring>

int na, nb, parent[2][101]/*, used[2][101]*/, t, start[2][101], end[2][101];
int size[2];
int s[2][2000], e[2][2000];

int tomins(char *s)
{
    return ((s[0]-'0') * 10 + s[1] - '0') * 60 + (s[3]-'0')*10 + s[4]-'0';
}

void dfs(int side, int v, int p)
{
    parent[side][v] = p;

    int ind = -1, i;
    for ( i = 0 ; i < size[side^1] ; i++ )
        if ( /*used[side^1][i] == 0 */ parent[side^1][i] == -1 && start[side^1][i] >= end[side][v] + t &&
             (ind == -1 || start[side^1][i] < start[side^1][ind] ) )
            ind = i;

    if ( ind != -1 )
        dfs(side^1, ind, v);
}

int main()
{
    int T, i, j;
    char str[1000];
    scanf( "%d", &T );
    for ( int cas = 1 ; cas <= T ; cas++ )
    {
        scanf( "%d%d%d", &t, &na, &nb );

        size[0] = na;
        size[1] = nb;
        memset(s,0,sizeof(s));
        memset(e,0,sizeof(e));

        for ( i = 0 ; i < na ; i++ )
        {
            scanf( "%s", &str );
            //start[0][i] = tomins(str);
            s[0][tomins(str)]++;
            scanf( "%s", &str );
            //end[0][i] = tomins(str);
            e[1][tomins(str)+t]++;
//            used[0][i] = 0;
//            parent[0][i] = -1;
        }

        for ( i = 0 ; i < nb ; i++ )
        {
            scanf( "%s", &str );
//            start[1][i] = tomins(str);
            s[1][tomins(str)]++;
            scanf( "%s", &str );
//            end[1][i] = tomins(str);
            e[0][tomins(str)+t]++;
//            used[1][i] = 0;
//            parent[1][i] = -1;
        }

        int res1 = 0, res2 = 0;

        for ( i = j = 0 ; ; )
        {
            while( i < 2000 && s[0][i] == 0 ) i++;
            while( j < 2000 && e[0][j] == 0 ) j++;

            if ( i >= 2000 )
                break;

            if ( j <= i )
            {
                s[0][i]--;
                e[0][j]--;
            }
            else
            {
                s[0][i]--;
                res1++;
            }
        }

        for ( i = j = 0 ; ; )
        {
            while( i < 2000 && s[1][i] == 0 ) i++;
            while( j < 2000 && e[1][j] == 0 ) j++;

            if ( i >= 2000 )
                break;

            if ( j <= i )
            {
                s[1][i]--;
                e[1][j]--;
            }
            else
            {
                s[1][i]--;
                res2++;
            }
        }

        printf( "Case #%d: %d %d\n", cas, res1, res2 );
    }
    return 0;
}