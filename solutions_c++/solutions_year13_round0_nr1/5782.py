#include <cstdio>

char b[4][5];
int  n[4][5][8];

void go(bool& won, int y, int x, int dy, int dx, char c, int counter, int d) {
    if(x >= 0 && x < 4 && y >= 0 && y < 4 && b[y][x] == c && n[y][x][d] == 0) {
        n[y][x][d] = 1;
        if(counter == 4) {
            won = true;
        } else {
            go(won, y + dy, x + dx, dy, dx, c, counter + 1, d);
        }
    }
}

bool run(char c) {
    for(int i = 0; i < 4; ++i) {
        for(int j = 0; j < 4; ++j) {
            for(int k = 0; k < 8; ++k) {
                n[i][j][k] = 0;
            }
        }
    }

/*
  0 1 2
  7 + 3
  6 5 4
*/
    bool won = false;
    for(int i = 0; i < 4; ++i) {
        for(int j = 0; j < 4; ++j) {
            if(b[i][j] == c) {
                if(n[i][j][0] == 0) {
                    go(won, i, j, -1, -1, c, 1, 0);
                    if(won) {
                        return true;
                    }
                }
                if(n[i][j][1] == 0) {
                    go(won, i, j, -1, 0, c, 1, 1);
                    if(won) {
                        return true;
                    }
                }
                if(n[i][j][2] == 0) {
                    go(won, i, j, -1, +1, c, 1, 2);
                    if(won) {
                        return true;
                    }
                }
                if(n[i][j][3] == 0) {
                    go(won, i, j, 0, +1, c, 1, 3);
                    if(won) {
                        return true;
                    }
                }
                if(n[i][j][4] == 0) {
                    go(won, i, j, +1, +1, c, 1, 4);
                    if(won) {
                        return true;
                    }
                }
                if(n[i][j][5] == 0) {
                    go(won, i, j, +1, 0, c, 1, 5);
                    if(won) {
                        return true;
                    }
                }
                if(n[i][j][6] == 0) {
                    go(won, i, j, +1, -1, c, 1, 6);
                    if(won) {
                        return true;
                    }
                }
                if(n[i][j][7] == 0) {
                    go(won, i, j, 0, -1, c, 1, 7);
                    if(won) {
                        return true;
                    }
                }
            }
        }
    }

    return won;
}

int main() {

    int T, cases = 0;
    scanf("%d", &T);
    while(T-- > 0) {
        while(getchar() != '\n') {
        }
        printf("Case #%d: ", (++cases));
        for(int i = 0; i < 4; ++i) {
            scanf("%s", b[i]);
            while(getchar() != '\n') {
            }
        }
        bool hasS = false;
        bool hasT = false;
        int xt = -1, yt = -1;
        for(int i = 0; i < 4; ++i) {
            for(int j = 0; j < 4; ++j) {
                if(b[i][j] == 'T') {
                    hasT = true;
                    xt = j;
                    yt = i;
                }
                if(b[i][j] == '.') {
                    hasS = true;
                }
            }
        }
        bool Owon = false;
        bool Xwon = false;
        if(hasT) {
            b[yt][xt] = 'O';

            Owon = run('O');

            b[yt][xt] = 'X';

            Xwon = run('X');
        } else {
            Owon = run('O');
            Xwon = run('X');
        }
        if(Owon) {
            puts("O won");
        } else if(Xwon) {
            puts("X won");
        } else if(hasS) {
            puts("Game has not completed");
        } else {
            puts("Draw");
        }

    }
    return 0;
}
