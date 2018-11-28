#include <cstdio>
#include <string>
#define maxn 510

char str[maxn];
const char oop[20] = "welcome to code jam";
int len = strlen ( oop );
int fn[10000][maxn];

int main()
{
    freopen ( "c:\\C-small-attempt0.in", "r", stdin );
    freopen("c:\\C-small-attempt0.out","w",stdout);
    int n;
    int Case;
    int i, j;
    for (scanf ( "%d%*c", &n ),  Case = 1 ; Case <= n ;Case++ )
    {
        memset ( fn , 0 , sizeof ( fn ) );
        gets ( str );
        int slen = strlen ( str );

        for ( int i = 0 ; i < slen ; ++i ) {
            if ( str[i] == oop[0] ) {
                if ( i )
                    fn[0][i] = fn[0][i-1] + 1;
                else
                    fn[0][i] = 1;
            }
            else
                fn[0][i] = fn[0][i-1];
        }

        for ( int i = 1 ; i < len ; ++i ) {
            for ( int j = i ; j < slen - len + i + 1 ; ++j ) {
                if ( str[j] == oop[i] )
                    fn[i][j] = fn[i-1][j-1] + fn[i][j-1];
                else
                    fn[i][j] = fn[i][j-1];
            }
        }
        printf ( "Case #%d: %04d\n", Case , fn[len-1][slen-1] );
    }
    return 0;
}