#include <iostream>
using namespace std;
char name[10010][110];
int sta[10010];
int next[10010];
char s[110];
int cn, ci, i, n, m, z, ans;

void ins( int t )
{
    char ss[110];
    int len, x, i, j;
    len = strlen(s);
    x = 0;
    for ( i = 1; i < len; i++ )
    {
        j = 0;
        while ( i < len && s[i] != '/' )
        {
            ss[j] = s[i];
            i++;
            j++;
        }
        ss[j] = 0;
        for ( j = sta[x]; j != -1; j = next[j] )
        {
            if ( strcmp( name[j], ss ) == 0 )
                break;
        }
        if ( j == -1 )
        {
            if ( t == 1 ) ans++;
            memcpy( name[z], ss, sizeof(ss) );
            j = z;
            next[j] = sta[x];
            sta[x] = j;
            sta[j] = -1;
            z++;
        }
        x = j;
    }
}

int main()
{
    freopen( "A-large.in", "r", stdin );
    freopen( "A-large.out", "w", stdout );
    scanf( "%d", &cn );
    for ( ci = 1; ci <= cn; ci++ )
    {
        scanf( "%d %d", &n, &m );
        sta[0] = -1;
        z = 1;
        for ( i = 0; i < n; i++ )
        {
            scanf( "%s", &s );
            ins( 0 );
        }
        ans = 0;
        for ( i = 0; i < m; i++ )
        {
            scanf( "%s", &s );
            ins( 1 );
        }
        printf( "Case #%d: %d\n", ci, ans );
    }
    return 0;
}
