#include <stdio.h>

char board[4][4];

bool checkWin(char player)
{
    bool win;

    // check rows
    for (int r = 0; r < 4; r++) {
        win = true;
        for (int c = 0; c < 4; c++) 
            if (board[r][c] != 'T' && board[r][c] != player) win = false;
        if (win) return true;
    }
    // check columns
    for (int c = 0; c < 4; c++) {
        win = true;
        for (int r = 0; r < 4; r++)
            if (board[r][c] != 'T' && board[r][c] != player) win = false;
        if (win) return true;
    }
    // check primary diagonal
    win = true;
    for (int r = 0; r < 4; r++)
        if (board[r][r] != 'T' && board[r][r] != player) win = false;
    if (win) return true;
    // check secondary diagnoal
    win = true;
    for (int r = 0; r < 4; r++)
        if (board[r][3-r] != 'T' && board[r][3-r] != player) win = false;
    if (win) return true;

    return false;
}

int main()
{
    int nprob;

    scanf("%d", &nprob);
    for (int prob = 0; prob < nprob; prob++) {
        bool done = true;

        for (int r = 0; r < 4; r++)
            for (int c = 0; c < 4; c++) {
                char ch;
                scanf("%c", &ch);
                while (ch != 'X' && ch != 'O' && ch != 'T' && ch != '.')
                    scanf("%c", &ch);
                if (ch == '.') done = false;
                board[r][c] = ch;
            }

        printf("Case #%d: ", prob+1);
        if (checkWin('X')) 
            printf("X won\n");
        else if (checkWin('O'))
            printf("O won\n");
        else if (!done)
            printf("Game has not completed\n");
        else
            printf("Draw\n");
    }

    return 0;
}
