#include <iostream>

using namespace std;

int T = 0;

void getRuns(char test[4][5], char out[10][5]) {
    // get rows
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 5; ++j) {
            out[i][j] = test[i][j];
        }
    }
    // get cols
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            out[i + 4][j] = test[j][i];
        }
        out[i + 4][4] = '\0';
    }
    // get diags
    for (int i = 0; i < 4; ++i) {
        out[8][i] = test[i][i];
        out[9][i] = test[3-i][i];
    }
    out[8][5] = out[9][5] = '\0';
}

bool contains(char line[4], char c) {
    for (int i = 0; i < 4; ++i) {
        if (line[i] == c)
            return true;
    }
    return false;
}

int main ()
{
    cin >> T;
    char temp[4][5];
    char runs[10][5];
    for (int testCase = 1; testCase <= T; ++testCase) {
        for (int i = 0; i < 4; ++i) {
            cin >> temp[i];
        }
        bool xWon = false, oWon = false, notFull = false;

        getRuns(temp, runs);
        // rows
        for (int i = 0; i < 10; ++i) {
            if (contains(runs[i], '.')) {
                notFull = true;
                continue;
            }
            if (!contains(runs[i], 'O')) {
                xWon = true;
                break;
            }
            if (!contains(runs[i], 'X')) {
                oWon = true;
                break;
            }
        }

        cout << "Case #" << testCase << ": ";
        if (xWon) {
            cout << "X won\n";
        } else if (oWon) {
            cout << "O won\n";
        } else if (notFull) {
            cout << "Game has not completed\n";
        } else {
            cout << "Draw\n";
        }
    }
    return 0;
}
