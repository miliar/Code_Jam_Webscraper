#include <iostream>
#include <cstdio>

using namespace std;
char board[1050][17];
int rowcheck(int i) { // i is index of board, j is rownum, we are checking (rownum-1)*4+1...+4, returns 1 for O, 2 for X, 3 for n/a
    for(int j=1; j<=4; j++) {
        int zzz = (j-1)*4+1;
        if(board[i][zzz] == 'X' || board[i][zzz] == 'T') {
            if(board[i][zzz+1] == 'X' || board[i][zzz+1] == 'T') {
                if(board[i][zzz+2] == 'X' || board[i][zzz+2] == 'T') {
                    if(board[i][zzz+3] == 'X' || board[i][zzz+3] == 'T') {
                        return 2;
                    }
                }
            }
        }
        if(board[i][zzz] == 'O' || board[i][zzz] == 'T') {
            if(board[i][zzz+1] == 'O' || board[i][zzz+1] == 'T') {
                if(board[i][zzz+2] == 'O' || board[i][zzz+2] == 'T') {
                    if(board[i][zzz+3] == 'O' || board[i][zzz+3] == 'T') {
                        return 1;
                    }
                }
            }
        }
    }
    return 3;
}
bool emptycheck(int i) { // i is index of board, true if '.', false if no '.'
    for(int ind = 1; ind <= 16; ind++ ) {
        if(board[i][ind] == '.') {return true;}
    }
    return false;
}
int columncheck(int i) { // i is index, j is modulo
    for(int j=1; j<=4; j++) {
        int zzz = j;
        if(board[i][zzz] == 'X' || board[i][zzz] == 'T') {
            if(board[i][zzz+4] == 'X' || board[i][zzz+4] == 'T') {
                if(board[i][zzz+8] == 'X' || board[i][zzz+8] == 'T') {
                    if(board[i][zzz+12] == 'X' || board[i][zzz+12] == 'T') {
                        return 2;
                    }
                }
            }
        }
        if(board[i][zzz] == 'O' || board[i][zzz] == 'T') {
            if(board[i][zzz+4] == 'O' || board[i][zzz+4] == 'T') {
                if(board[i][zzz+8] == 'O' || board[i][zzz+8] == 'T') {
                    if(board[i][zzz+12] == 'O' || board[i][zzz+12] == 'T') {
                        return 1;
                    }
                }
            }
        }
    }
    return 3;
}

int diagcheck (int i) { // i is index, j is back or forwards
    if(board[i][1] == 'O' || board[i][1] == 'T') {
        if(board[i][6] == 'O' || board[i][6] == 'T') {
            if(board[i][11] == 'O' || board[i][11] == 'T') {
                if(board[i][16] == 'O' || board[i][16] == 'T') {
                    return 1;
                }
            }
        }
    }
    if(board[i][1] == 'X' || board[i][1] == 'T') {
        if(board[i][6] == 'X' || board[i][6] == 'T') {
            if(board[i][11] == 'X' || board[i][11] == 'T') {
                if(board[i][16] == 'X' || board[i][16] == 'T') {
                    return 2;
                }
            }
        }
    }
    if(board[i][4] == 'O' || board[i][4] == 'T') {
        if(board[i][7] == 'O' || board[i][7] == 'T') {
            if(board[i][10] == 'O' || board[i][10] == 'T') {
                if(board[i][13] == 'O' || board[i][13] == 'T') {
                    return 1;
                }
            }
        }
    }
    if(board[i][4] == 'X' || board[i][4] == 'T') {
        if(board[i][7] == 'X' || board[i][7] == 'T') {
            if(board[i][10] == 'X' || board[i][10] == 'T') {
                if(board[i][13] == 'X' || board[i][13] == 'T') {
                    return 2;
                }
            }
        }
    }
    return 3;
}
int main() {
    if(fopen("tic.in","r")) {
        freopen("tic.in","r",stdin);
        freopen("tic.out","w",stdout);
    }
    int t;
    cin >> t;
    for(int i=1; i<=t; i++) {
        char c;
        int j = 1;
        while(j <= 16 && cin >> c) {
            if(c == 'X' || c == 'T' || c == '.' || c == 'O') {
                board[i][j] = c;
                j++;
            }
        }
    }
    for(int i=1; i<=t; i++) {
        bool r = emptycheck(i);
        int a = rowcheck(i);
        int b = columncheck(i);
        int c = diagcheck(i);
        if(a == 1 || b == 1 || c == 1) {
            cout << "Case #" << i << ": O won" << '\n';
            continue;
        }
        if(a == 2 || b == 2 || c == 2) {
            cout << "Case #" << i << ": X won" << '\n';
            continue;
        }
        if(a == 3 && b == 3 && c == 3 && !r) {
            cout << "Case #" << i << ": Draw" << '\n';
            continue;
        }
        if(a == 3 && b == 3 && c == 3 && r) {
            cout << "Case #" << i << ": Game has not completed" << '\n';
            continue;
        }
    }
    return 0;
}
