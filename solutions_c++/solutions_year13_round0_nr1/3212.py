#include <cstdio>

char board[4][4];

char readandanswer() { //X, O, D or N
    char read;
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            do {
                scanf("%c", &read);
            } while (read != 'T' && read != 'X' && read != 'O' && read != '.');
            board[i][j] = read;
        }
    }
/*    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            printf("%c", board[i][j]);
        }
        printf("\n");
    }
*/    
    char winner = 'N';
    bool completed = true;

    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            if (board[i][j] == '.') completed = false;
        }
    }

    for (int i = 0; i < 4; i++) {
        if (winner != 'N') break;
        for (int j = 0; j < 4; j++) {
            if (board[i][j] == 'T') continue;
            if (board[i][j] == '.') {
                winner = 'N';
                break;
            }
            if (winner == 'N') winner = board[i][j];
            if (board[i][j] != winner) {
                winner = 'N';
                break;
            }
        }
    }
    
    if (winner == 'N')
    for (int i = 0; i < 4; i++) {
        if (winner != 'N') break;
        for (int j = 0; j < 4; j++) {
            if (board[j][i] == 'T') continue;
            if (board[j][i] == '.') {
                winner = 'N';
                break;
            }
            if (winner == 'N') winner = board[j][i];
            if (board[j][i] != winner) {
                winner = 'N';
                break;
            }
        }
    }

    if (winner == 'N')
    for (int i = 0; i < 4; i++) {
            if (board[i][i] == 'T') continue;
            if (board[i][i] == '.') {
                winner = 'N';
                break;
            }
            if (winner == 'N') winner = board[i][i];
            if (board[i][i] != winner) {
                winner = 'N';
                break;
            }
    }

    if (winner == 'N')
    for (int i = 0; i < 4; i++) {
            if (board[i][3-i] == 'T') continue;
            if (board[i][3-i] == '.') {
                winner = 'N';
                break;
            }
            if (winner == 'N') winner = board[i][3-i];
            if (board[i][3-i] != winner) {
                winner = 'N';
                break;
            }
    }

    if (completed && winner == 'N') return 'D';
    return winner;
}

int main() {
    int n;
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        printf("Case #%d: ", i + 1);
        switch(readandanswer()) {
            case 'X': printf("X won\n"); break;
            case 'O': printf("O won\n"); break;
            case 'D': printf("Draw\n"); break;
            case 'N': printf("Game has not completed\n"); break;
        }
    }
}
