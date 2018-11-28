#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char convert[300][300];
char rem[300][300];

int main()
{
    int aa, nn, c, d, len[2], i, t, j;
    char buffer[110];
    int cur, pre, l;
    char list[2][110];
    scanf("%d",&nn);
    for ( aa = 1; aa <= nn; ++aa ) {
        scanf("%d",&c);
        memset(convert,0,sizeof(convert));
        memset(rem,0,sizeof(rem));
        for ( i = 0; i < c; i++ ) {
            scanf("%s",buffer);
            convert[buffer[0]][buffer[1]] = convert[buffer[1]][buffer[0]] = buffer[2];
        }
        scanf("%d",&d);
        for ( i = 0; i < d; i++ ) {
            scanf("%s",buffer);
            rem[buffer[0]][buffer[1]] = rem[buffer[1]][buffer[0]] = 1;
        }
        scanf("%d %s",&len[0],list[0]);
        pre = 0; cur = 1;
        while ( 1 ) {
            l = 0; 
            for ( i = 0; i < len[pre]; i++ ) {
                list[cur][l++] = list[pre][i];

                // check
                if ( l > 1 && (t=convert[list[cur][l-1]][list[cur][l-2]]) ) {
                    list[cur][l-2] = t;
                    --l;
                } else {
                    t = list[cur][l-1];
                    for ( j = 0; j < l-1; j++ ) {
                        if ( rem[t][list[cur][j]] ) {
                            l = 0;
                            break;
                        }
                    }
                }
            }

            len[cur] = l;
            list[cur][l] = 0;
            if ( strcmp(list[0],list[1]) == 0 ) break;

            pre = cur;
            cur = 1-cur;
        }
        printf("Case #%d: [",aa);
        if ( len[cur] > 0 ) {
            printf("%c",list[cur][0]);
            for ( i = 1; i < len[cur]; i++ ) {
                printf(", %c",list[cur][i]);
            }
        }
        printf("]\n");
    }
    return 0;
}

