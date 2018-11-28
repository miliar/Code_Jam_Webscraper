#include <stdio.h>

char grid[4][4];

int check(char grid[4][4], char ch) {
    // Horizontal
    for (int i = 0; i < 4; i++)
        if (grid[i][0] == ch && grid[i][1] == ch && grid[i][2] == ch && grid[i][3] == ch) {
            return 1;
        }

    // Vertical
    for (int i = 0; i < 4; i++)
        if (grid[0][i] == ch && grid[1][i] == ch && grid[2][i] == ch && grid[3][i] == ch) {
            return 1;
        }

    // Diagonal
    if (grid[0][0] == ch && grid[1][1] == ch && grid[2][2] == ch && grid[3][3] == ch) return 1;
    if (grid[0][3] == ch && grid[1][2] == ch && grid[2][1] == ch && grid[3][0] == ch) return 1;
}

int main() {
    int N;

    scanf("%d", &N);
    for (int caseN = 1; caseN <= N; caseN++) {
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                scanf(" %c", &grid[i][j]);

        int complete = 1;
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                if (grid[i][j] == '.') complete = 0;

        int tr = -1, tc = -1;
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                if (grid[i][j] == 'T') {
                    tr = i;
                    tc = j;
                    goto breakloop;
                }

breakloop:
        if (tr != -1) grid[tr][tc] = 'X';
        int xwin = check(grid, 'X');
        if (tr != -1) grid[tr][tc] = 'O';
        int owin = check(grid, 'O');
        if (tr != -1) grid[tr][tc] = 'T';

        printf("Case #%d: ", caseN);
        if (xwin) {
            printf("X won\n");
        } else if (owin) {
            printf("O won\n");
        } else if (complete) {
            printf("Draw\n");
        } else {
            printf("Game has not completed\n");
        }
    }
    return 0;
}
