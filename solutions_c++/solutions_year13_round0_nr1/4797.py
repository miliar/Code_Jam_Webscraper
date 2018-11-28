#include <iostream>
#include <cstdio>

using namespace std;

char board[4][4];

char check(int y, int x, int dy, int dx) {
    char checked = board[y][x];
    int j = 1;
    if (checked == 'T') {
        checked = board[y+dy][x+dx];
        j++;
    }
    if (checked == '.')
        return 0;
    while (j < 4) {
        if (board[y+j*dy][x+j*dx] != checked && board[y+j*dy][x+j*dx] != 'T')
            break;
        j++;
    }
    if (j == 4)
        return checked;
    return 0;
}

char solve() {
    int i,j;
    char winner;
    for (i = 0; i < 4; i++) {
       scanf("%c%c%c%c\n", &board[i][0], &board[i][1], &board[i][2], &board[i][3]);
    }
    char temp;
    scanf("%c", temp);

    //rows
    winner = check(0,0,0,1); if (winner != 0) return winner;
    winner = check(1,0,0,1); if (winner != 0) return winner;
    winner = check(2,0,0,1); if (winner != 0) return winner;
    winner = check(3,0,0,1); if (winner != 0) return winner;
    //cols
    winner = check(0,0,1,0); if (winner != 0) return winner;
    winner = check(0,1,1,0); if (winner != 0) return winner;
    winner = check(0,2,1,0); if (winner != 0) return winner;
    winner = check(0,3,1,0); if (winner != 0) return winner;

    winner = check(0,0,1,1); if (winner != 0) return winner;
    winner = check(0,3,1,-1); if (winner != 0) return winner;


    //no winner yet
    for (i = 0; i < 4; i++) {
        for (j = 0; j < 4; j++) {
            if (board[i][j] == '.')
                return '.';
        }
    }
    return 'd';
}

char xWon[] = "X won";
char oWon[] = "O won";
char draw[] = "Draw";
char playing[] = "Game has not completed";

char* getStatus(char s) {
    if (s == 'X')
        return xWon;
    else if(s == 'O')
        return oWon;
    else if (s == 'd')
        return draw;
    else
        return playing;
}

int main()
{
    int t;
    scanf("%d\n", &t);
    char winner;
    for (int i = 1; i <= t; i++) {
        winner = solve();
        printf("Case #%d: %s\n", i, getStatus(winner));
    }
    return 0;
}
