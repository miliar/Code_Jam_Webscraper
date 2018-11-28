#include <algorithm>
#include <iostream>

using namespace std;

int main() {
    int t;
    char board[4][4], c;
    bool notover;

    cin >> t;
    for (int i = 1; i <= t; ++i) {
        notover = false;
        for (int row = 0; row < 4; ++row) {
            for (int col = 0; col < 4; ++col) {
                cin >> c;
                if (c == '.') {
                    notover = true;
                }
                board[row][col] = c;
            }
        }

        int rowcnt[4][4], colcnt[4][4], diagcnt[4], sdiagcnt[4];
        for (int ii = 0; ii < 4; ++ii) {
            for (int jj = 0; jj < 4; ++jj) {
                rowcnt[ii][jj] = 0;
                colcnt[ii][jj] = 0;
            }
            diagcnt[ii] = 0;
            sdiagcnt[ii] = 0;
        }

        for (int row = 0; row < 4; ++row) {
            for (int col = 0; col < 4; ++col) {
                switch (board[row][col]) {
                    case 'X':
                        rowcnt[row][0]++;
                        colcnt[col][0]++;
                        if (row == col) {
                            diagcnt[0]++;
                        }
                        if (row == 3 - col) {
                            sdiagcnt[0]++;
                        }
                        break;
                    case 'O':
                        rowcnt[row][1]++;
                        colcnt[col][1]++;
                        if (row == col) {
                            diagcnt[1]++;
                        }
                        if (row == 3 - col) {
                            sdiagcnt[1]++;
                        }
                        break;
                    case 'T':
                        rowcnt[row][2]++;
                        colcnt[col][2]++;
                        if (row == col) {
                            diagcnt[2]++;
                        }
                        if (row == 3 - col) {
                            sdiagcnt[2]++;
                        }
                        break;
                    case '.':
                        rowcnt[row][3]++;
                        colcnt[col][3]++;
                        if (row == col) {
                            diagcnt[3]++;
                        }
                        if (row == 3 - col) {
                            sdiagcnt[3]++;
                        }
                        break;
                }
            }
        }

        bool xwins = false, owins = false;
        for (int row = 0; row < 4; ++row) {
            if (rowcnt[row][0] == 4 || (rowcnt[row][0] == 3 && rowcnt[row][2] == 1)) {
                xwins = true;
            } else if (rowcnt[row][1] == 4 || (rowcnt[row][1] == 3 && rowcnt[row][2] == 1)) {
                owins = true;
            }
        }

        for (int col = 0; col < 4; ++col) {
            if (colcnt[col][0] == 4 || (colcnt[col][0] == 3 && colcnt[col][2] == 1)) {
                xwins = true;
            } else if (colcnt[col][1] == 4 || (colcnt[col][1] == 3 && colcnt[col][2] == 1)) {
                owins = true;
            }
        }

        if (diagcnt[0] == 4 || (diagcnt[0] == 3 && diagcnt[2] == 1)) {
            xwins = true;
        } else if (diagcnt[1] == 4 || (diagcnt[1] == 3 && diagcnt[2] == 1)) {
            owins = true;
        }
        if (sdiagcnt[0] == 4 || (sdiagcnt[0] == 3 && sdiagcnt[2] == 1)) {
            xwins = true;
        } else if (sdiagcnt[1] == 4 || (sdiagcnt[1] == 3 && sdiagcnt[2] == 1)) {
            owins = true;
        }
        
        cout << "Case #" << i << ": ";
        if (xwins) {
            cout << "X won" << endl;
        } else if (owins) {
            cout << "O won" << endl;
        } else if (notover) {
            cout << "Game has not completed" << endl;
        } else {
            cout << "Draw" << endl;
        }
    }
}
