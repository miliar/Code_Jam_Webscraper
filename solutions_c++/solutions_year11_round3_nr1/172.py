#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char table[60][60];
int r, c;

int main()
{
    int aa, nn;
    int i, j, ok;
    scanf("%d",&nn);
    for (aa =1;aa <= nn; ++aa ) {
        scanf("%d %d",&r,&c);
        for ( i = 0; i < r; i++ )
            scanf("%s",table[i]);

        for ( i = 0, ok=1; i < r-1; i++ ) {
            for ( j = 0; j < c-1; j++ ) {
                if ( table[i][j] == '.' ) continue;
                if ( table[i][j] == '#' &&
                    table[i][j+1] == '#' &&
                    table[i+1][j] == '#' &&
                    table[i+1][j+1] == '#' ) {
                    table[i][j] = '/';
                    table[i][j+1] = '\\';
                    table[i+1][j] = '\\';
                    table[i+1][j+1] = '/';
                }
            }
        }
        for ( i = 0; ok && i < r; i++ ) {
            for ( j = 0; ok && j < c; j++ ) {
                if ( table[i][j] == '.' ) continue;
                if ( table[i][j] == '#' ) ok = 0;
            }
        }
        printf("Case #%d:\n",aa);
        if ( !ok ) {
            printf("Impossible\n");
        } else {
            for ( i = 0; i < r; i++ ) {
                printf("%s\n",table[i]);
            }
        }
    }
    return 0;
}
