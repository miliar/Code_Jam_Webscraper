#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_A 30
#define MAX_LEN 20
#define MAX_WORD 5111

char s[MAX_WORD][MAX_LEN];
bool b[MAX_LEN][MAX_A];
int l, d, n;
char w[MAX_LEN*MAX_A];
int c;
void Solve( )
{
    ++c;
    int res = 0;
    int ind = 0;
    scanf( "%s", w );
    memset( b, 0, sizeof( b ) );
    int len = strlen( w );
    for( int i = 0; i < len; ++i )
        if( w[i] == '(' )
        {
            ++i;
            while( w[i] != ')' ) b[ind][w[i++]-'a'] = 1;
            ind++;
        }
        else b[ind++][w[i]-'a'] = 1;
    for( int i = 0; i < d; ++i )
    {
        int count = 0;
        for( int j = 0; j < l; ++j )
            if( b[j][s[i][j]-'a'] ) count++;
            else break;
        if( count == l ) res++;
    }
    printf( "Case #%d: %d\n", c, res );    
}

int main( )
{
    freopen( "in.in", "r", stdin );
    freopen( "out.txt", "w", stdout );
    scanf( "%d %d %d", &l, &d, &n );
    for( int i = 0; i < d; ++i )
        scanf( "%s", s[i] );
    for( int i = 0; i < n; ++i )
        Solve( );
    return 0;
}
