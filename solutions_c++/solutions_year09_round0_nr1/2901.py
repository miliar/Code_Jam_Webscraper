#include <stdio.h>
#include <string.h>
#define lM 16
#define dM 5001

char word[dM][lM];
char text[1000];
int st[dM], ed[dM];
int count;

int main()
{
    freopen("A.in", "r", stdin);
    freopen("slyar.out", "w", stdout);
    int l, d, n;
    int i, j, k;
    int T = 0;
    bool flag;
    scanf( "%d%d%d", &l, &d, &n );
    for( i = 0; i < d; i++ )
            scanf( "%s", word[i] );
    while( n-- )
    {
        flag = true;
        count = 0;
        scanf( "%s", text );
        for( j = i = 0; text[i]; i++ )
        {
            if( text[i] == '(' )
                flag = false;
            else if( text[i] == ')' )
                flag = true;
            else if( text[i] != '(' && text[i] != ')' &&
                     text[i - 1] == '(' && !flag )
            {
                ed[j] = st[j] = i;
                j++;
            }
            else if( flag )
            {
                ed[j] = st[j] = i;
                j++;
            }
            else if( !flag )
                ed[j - 1]++;
        }
        for( i = 0; i < d; i++ )
        {
            for( j = 0; word[i][j]; j++ )
            {
                for( k = st[j]; k < ed[j]; k++ )
                {
                    if( text[k] == word[i][j] )
                        break;
                }
                if( text[k] != word[i][j] )
                    break;
            }
            if( !word[i][j] )
                count++;
        }
        printf( "Case #%d: %d\n", ++T, count );
    }
    fclose(A);
    fclose(stdout);
return 0;
}
