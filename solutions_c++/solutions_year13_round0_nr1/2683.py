#include <iostream>
#include <string>
#include <vector>
#include <cstdio>

using namespace std;

string data[4];
string answer;

void readData() {
    for (int i = 0; i < 4; ++i) {
        cin >> data[i];
    }
}

string solve() {
    vector<int> numX(10), numO(10), numT(10);
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            if (data[i][j] == 'O') {
                numO[i]++;
            }
            if (data[i][j] == 'X') {
                numX[i]++;
            }
            if (data[i][j] == 'T') {
                numT[i]++;
            }
        }
    }

    for (int j = 0; j < 4; ++j) {
        for (int i = 0; i < 4; ++i) {
            if (data[i][j] == 'O') {
                numO[4 + j]++;
            }
            if (data[i][j] == 'X') {
                numX[4 + j]++;
            }
            if (data[i][j] == 'T') {
                numT[4 + j]++;
            }
        }
    }
    for (int i = 0; i < 4; ++i) {
        if (data[i][i] == 'O') {
            numO[8]++;
        }
        if (data[i][i] == 'X') {
            numX[8]++;
        }
        if (data[i][i] == 'T') {
            numT[8]++;
        }
        if (data[i][3 - i] == 'O') {
            numO[9]++;
        }
        if (data[i][3 - i] == 'X') {
            numX[9]++;
        }
        if (data[i][3 - i] == 'T') {
            numT[9]++;
        }
    }

    for (int i = 0; i < 10; ++i) {
        if (numO[i] == 4) {
            return "O won";
        }
        if (numX[i] == 4) {
            return "X won";
        }
        if (numX[i] == 3 && numT[i] == 1) {
            return "X won";
        }
        if (numO[i] == 3 && numT[i] == 1) {
            return "O won";
        }
    }
    int sumDesk = 0;
    for (int i = 0; i < 4; ++i) {
        sumDesk += numX[i] + numO[i] + numT[i];
    }
    if (sumDesk == 16) {
        return "Draw";
    }
    return "Game has not completed";
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        readData();
        answer = solve();
        cout << "Case #" << i + 1 << ": " << answer << endl;
    }
    return 0;
}
