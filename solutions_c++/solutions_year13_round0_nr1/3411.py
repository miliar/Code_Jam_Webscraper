#include <cstdio>

int T, TT;
char board[4][4];

int win(char w) {
    int i, j;
    for (i = 0; i < 4; i++) {
        for (j = 0; j < 4; j++)
            if (board[i][j] != w && board[i][j] != 'T')
                break;
        if (j == 4)
            return 1;
    }
    for (i = 0; i < 4; i++) {
        for (j = 0; j < 4; j++)
            if (board[j][i] != w && board[j][i] != 'T')
                break;
        if (j == 4)
            return 1;
    }
    for (i = 0; i < 4; i++) {
        if (board[i][i] != w && board[i][i] != 'T')
            break;
    }
    if (i == 4)
        return 1;
    for (i = 0; i < 4; i++)
        if (board[i][3-i] != w && board[i][3-i] != 'T')
            break;
    if (i == 4)
        return 1;
    return 0;
}

int main() {
    scanf("%d", &TT);
    for (T = 1; T <= TT; T++) {
        printf("Case #%d: ", T);
        int i, j;
        for (i = 0; i < 4; i++)
            scanf("%s", board[i]);
        if (win('X')) {
            printf("X won\n");
            continue;
        }
        if (win('O')) {
            printf("O won\n");
            continue;
        }
        for (i = 0; i < 4; i++) {
            for (j = 0; j < 4; j++)
                if (board[i][j] == '.')
                    break;
            if (j != 4)
                break;
        }
        if (i != 4)
            printf("Game has not completed\n");
        else
            printf("Draw\n");
    }
}