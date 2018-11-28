#include <cstring>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

string getStatus(vector<string> board) {
    int N = 4;
    bool over = true;
    int rowcount[N][2];
    int colcount[N][2];
    int diagcount[2][2];

    memset(rowcount, 0, sizeof(rowcount));
    memset(colcount, 0, sizeof(colcount));
    memset(diagcount, 0, sizeof(diagcount));

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (board[i][j] == '.')
                over = false;
            else if (board[i][j] == 'X') {
                rowcount[i][0]++;
                colcount[j][0]++;
                if (i == j)
                    diagcount[0][0]++;
                if (N - i - 1 == j)
                    diagcount[1][0]++;
            } else if (board[i][j] == 'O') {
                rowcount[i][1]++;
                colcount[j][1]++;
                if (i == j)
                    diagcount[0][1]++;
                if (N - i - 1 == j)
                    diagcount[1][1]++;
            } else if (board[i][j] == 'T') {
                rowcount[i][0]++;
                colcount[j][0]++;
                rowcount[i][1]++;
                colcount[j][1]++;
                if (i == j) {
                    diagcount[0][0]++;
                    diagcount[0][1]++;
                }
                if (N - i - 1 == j) {
                    diagcount[1][0]++;
                    diagcount[1][1]++;
                }
            }
        }
    }

    for (int i = 0; i < N; i++) {
        if (rowcount[i][0] == N || colcount[i][0] == N)
            return "X won";
        if (rowcount[i][1] == N || colcount[i][1] == N)
            return "O won";
    }

    for (int i = 0; i < 2; i++) {
        if (diagcount[i][0] == N)
            return "X won";
        if (diagcount[i][1] == N)
            return "O won";
    }

    if (over)
        return "Draw";
    return "Game has not completed";
}

int main() {
    int T;
    cin >> T;

    for (int i = 1; i <= T; i++) {
        vector<string> board;
        string temp;
        for (int j = 0; j < 4; j++) {
            cin >> temp;
            board.push_back(temp);
        }

        cout << "Case #" << i << ": " << getStatus(board) << endl;
    }

    return 0;
}
