#include<stdio.h>

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int t, x, win, complete, i ,j;
    char game[4][4];

    scanf("%d", &t);

    for(x = 1; x <= t; x++) {
        complete = 1;
        /*input*/
        for(i = 0; i < 4; i++)
            for(j = 0; j < 4; j++) {
                scanf(" %c", &game[i][j]);
                if(game[i][j] == '.') complete = 0;
            }
        win = -1;
        /*lin*/
        for(i = 0; i < 4; i++) {
            for(j = 0; j < 4; j++)
                if(game[i][j] != 'X' && game[i][j] != 'T') break;
            if(j == 4) {
                win = 1;
                break;
            }

            for(j = 0; j < 4; j++)
                if(game[i][j] != 'O' && game[i][j] != 'T') break;
            if(j == 4) {
                win = 0;
                break;
            }
        }
        /*col*/
        for(i = 0; i < 4; i++) {
            for(j = 0; j < 4; j++)
                if(game[j][i] != 'X' && game[j][i] != 'T') break;
            if(j == 4) {
                win = 1;
                break;
            }

            for(j = 0; j < 4; j++)
                if(game[j][i] != 'O' && game[j][i] != 'T') break;
            if(j == 4) {
                win = 0;
                break;
            }
        }
        /*diag*/
        for(i = 0; i < 4; i++)
            if(game[i][i] != 'X' && game[i][i] != 'T') break;
        if(i == 4) win = 1;

        for(i = 0; i < 4; i++)
            if(game[i][3-i] != 'X' && game[i][3-i] != 'T') break;
        if(i == 4) win = 1;

        for(i = 0; i < 4; i++)
            if(game[i][i] != 'O' && game[i][i] != 'T') break;
        if(i == 4) win = 0;

        for(i = 0; i < 4; i++)
            if(game[i][3-i] != 'O' && game[i][3-i] != 'T') break;
        if(i == 4) win = 0;

        printf("Case #%d: ", x);
        if(win == 1) printf("X won\n");
        else if(win == 0) printf("O won\n");
        else {
            if(complete == 1) printf("Draw\n");
            else printf("Game has not completed\n");
        }
    }
    return 0;
}
