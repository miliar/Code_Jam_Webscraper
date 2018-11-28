#include <iostream>
#include <string.h>

using namespace std;

int main() {
    int _cases;
    cin >> _cases;
    for(int _case = 0; _case < _cases; _case++) {
        int n, k;
        cin >> n >> k;
        int board[n][n];
        string s;
        for(int i = n-1; i >= 0; i--) {
            memset(board[i], 0, sizeof(int)*n);
            cin >> s;
            int p = n-1;
            for(int j = n-1; j >= 0; j--) {
                switch(s.at(j)) {
                    case 'R':
                        board[i][p--] = 1;
                        break;
                     case 'B':
                        board[i][p--] = -1;
                        break;
                     case '.':
                        break;
                     default:
                        cout << "Derp has occured" << endl;
                        break;
                }
            }
        }
        /*
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                cout << board[i][j] << " ";
            }
            cout << endl;
        }
        */
        int left[n][n];
        int up[n][n];
        int diag[n][n];
        int diag2[n][n];
        int foundRed = 0, foundBlue = 0;
        for(int i = 0; i < n; i++) {
            memset(left[i], 0, sizeof(int)*n);
            memset(up[i], 0, sizeof(int)*n);
            memset(diag[i], 0, sizeof(int)*n);
            memset(diag2[i], 0, sizeof(int)*n);
            left[i][0] = 1;
            diag[i][0] = 1;
            diag[i][n-1] = 1;
            for(int j = 0; j < n; j++) {
                if(i > 0) {
                   if(board[i][j] == board[i-1][j]) {
                        up[i][j] = up[i-1][j] + 1;
                        if(up[i][j] >= k) {
                            if(board[i][j] == 1) {
                                foundRed = 1;
                            }
                            if(board[i][j] == -1) {
                                foundBlue = 1;
                            }
                        }
                    } else {
                        up[i][j] = 1;
                    }
                } else {
                    up[i][j] = 1;
                }

                if(j > 0) {
                    if(board[i][j-1] == board[i][j]) {
                        left[i][j] = left[i][j-1] + 1;
                        if(left[i][j] >= k) {
                            if(board[i][j] == 1) {
                                foundRed = 1;
                            }
                            if(board[i][j] == -1) {
                                foundBlue = 1;
                            }
                        }
                    } else {
                        left[i][j] = 1;
                    }
                }

                if(j > 0 && i > 0) {
                    if(board[i-1][j-1] == board[i][j]) {
                        diag[i][j] = diag[i-1][j-1] + 1;
                        if(diag[i][j] >= k) {
                            if(board[i][j] == 1) {
                                foundRed = 1;
                            }
                            if(board[i][j] == -1) {
                                foundBlue = 1;
                            }
                        }
                    } else {
                        diag[i][j] = 1;
                    }
                } else {
                    diag[i][j] = 1;
                }

                if(j < n-1 && i > 0) {
                    if(board[i-1][j+1] == board[i][j]) {
                        diag2[i][j] = diag2[i-1][j+1] + 1;
                        if(diag2[i][j] >= k) {
                            if(board[i][j] == 1) {
                                foundRed = 1;
                            }
                            if(board[i][j] == -1) {
                                foundBlue = 1;
                            }
                        }
                    } else {
                        diag2[i][j] = 1;
                    }
                } else {
                    diag2[i][j] = 1;
                }
            }
        }

        cout << "Case #" << (_case+1) << ": ";

        if(foundRed && foundBlue) {
            cout << "Both" << endl;
            continue;
        }

        if(foundRed) {
            cout << "Red" << endl;
            continue;
        }

        if(foundBlue) {
            cout << "Blue" << endl;
            continue;
        }

        cout << "Neither" << endl;

    }
}
