#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>

using namespace std;

int main()
{
//    cout << (int)'O' << ", " << (int)'X' << ", " << (int)'.' << ", " << (int)'T' << endl;
    int count[200][0];
    char winner;
    int T;
    cin >> T;
    for (int k = 1; k <= T; ++k) {
        winner = 0;
        bool done = 1;
        string board[4];
        for (int i = 0; i < 4; ++i)
            cin >> board[i];

        int sums[4][2];
        memset(sums, 0, sizeof(sums));
        for (int i = 0; i < 4; ++i) {
            for (int j = 0; j < 4; ++j) {
                sums[i][0] += board[i][j];
                sums[i][1] += board[j][i];
                if (board[i][j] == '.')
                    done = 0;
            }
        }

        int sumdiag = board[0][0] + board[1][1] + board[2][2] + board[3][3];
        int sumdiag2 = board[0][3] + board[1][2] + board[2][1] + board[3][0];
        if (sumdiag == 4 * 'X' || sumdiag == 3 * 'X' + 'T' ||
            sumdiag2 == 4 * 'X' || sumdiag2 == 3 * 'X' + 'T')
            winner = 'X';
        if (sumdiag == 4 * 'O' || sumdiag == 3 * 'O' + 'T' ||
            sumdiag2 == 4 * 'O' || sumdiag2 == 3 * 'O' + 'T')
            winner = 'O';
        for (int i = 0; i < 4; ++i) {
            if (sums[i][0] == 4 * 'X' || sums[i][0] == 3 * 'X' + 'T' ||
                    sums[i][1] == 4 * 'X' || sums[i][1] == 3 * 'X' + 'T')
                winner = 'X';
            if (sums[i][0] == 4 * 'O' || sums[i][0] == 3 * 'O' + 'T' ||
                    sums[i][1] == 4 * 'O' || sums[i][1] == 3 * 'O' + 'T')
                winner = 'O';
        }
        cout << "Case #" << k << ": ";
        if (winner == 'X' || winner == 'O')
            cout << winner << " won" << endl;
        if (winner == 0 && done)
            cout << "Draw" << endl;
        if (winner == 0 && !done)
            cout << "Game has not completed" << endl;
    }
}
