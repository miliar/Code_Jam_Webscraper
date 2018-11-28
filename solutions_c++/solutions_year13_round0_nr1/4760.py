#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char table[10][10];

int check(char c)
{
    int ret = 0;
    int i, j, k;
    for ( i = 0; !ret && i < 4; i++ ) {
        for ( k = 0, j = 0; j < 4; j++ ) {
            if (table[i][j] == c || table[i][j] == 'T') {
                k++;
            }
        }
        if (k == 4) {
            ret = 1;
        }

        for ( k = 0, j = 0; !ret && j < 4; j++ ) {
            if (table[j][i] == c || table[j][i] == 'T') {
                k++;
            }
        }
        if (k == 4) {
            ret = 1;
        }
    }

    for ( i = 0, j = 0, k = 0; !ret && i < 4; i++, j++ ) {
        if (table[i][j] == c || table[i][j] == 'T') {
            k++;
        }
    }
    if (k == 4) {
        ret = 1;
    }

    for ( i = 0, j = 3, k = 0; !ret && i < 4; i++, j-- ) {
        if (table[i][j] == c || table[i][j] == 'T') {
            k++;
        }
    }
    if (k == 4) {
        ret = 1;
    }

    return ret;
}

int main()
{
    int aa, nn, i, j, k;
    char buffer[20];
    char win = 0;
    gets(buffer);
    nn = atoi(buffer);
    for (aa = 1; aa <= nn; ++aa) {
        for (i = 0; i < 4; i++ ) {
            gets(table[i]);
        }
        gets(buffer);

        for ( i = 0, k = 0; i < 4; i++ ) {
            for (j = 0; j < 4; j++) {
                if (table[i][j] == '.') {
                    k++;
                }
            }
        }
        win = 0;
        if (check('X')) win = 'X';
        if (check('O')) win = 'O';
        if (win) {
            printf("Case #%d: %c won\n",aa,win);
        } else if (!k) {
            printf("Case #%d: Draw\n",aa);
        } else {
            printf("Case #%d: Game has not completed\n",aa);
        }
    }

    return 0;
}
