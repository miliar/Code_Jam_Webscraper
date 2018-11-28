#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

const int N = 4;

enum PositionStatus {
    DRAW,
    X_WON,
    O_WON,
    UNCOMPLETED
};

const int DIRECTIONS_COUNT = 4;
const int dx[DIRECTIONS_COUNT] = {1, 0, 1, 1},
          dy[DIRECTIONS_COUNT] = {0, 1, 1, -1};
          
bool isFullLine (vector<string> const & a, int x, int y, int dir, string const & s) {
    for (int i = 0; i < N; ++i) {
        // cout << a[x][y] << " " << s << "\n";
        if (find(s.begin(), s.end(), a[x][y]) == s.end()) {
            // cout << "\n";
            return false;
        }
        x += dx[dir];
        y += dy[dir];
    }
    return true;
}

PositionStatus getPositionStatus (vector<string> const & a) {
    int e = 0;
    bool existsT = false;
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < N; ++j) {
            if (a[i][j] == 'X' || a[i][j] == 'O') {
                ++e;
            }
            else if (a[i][j] == 'T') {
                existsT = true;
            }
        }
    }
    
    bool hasWon = false;
    string s = "T";
    if (e % 2 == 1) {
        s += 'X';
    }
    else {
        s += 'O';
    }
    
    for (int i = 0; i < 4; ++i) {
        hasWon |= isFullLine(a, i, 0, 1, s);
        hasWon |= isFullLine(a, 0, i, 0, s);
    }
    hasWon |= isFullLine(a, 0, 0, 2, s);
    hasWon |= isFullLine(a, 0, 3, 3, s);
    
    if (hasWon) {
        if (e % 2 == 1) {
            return X_WON;
        }
        else {
            return O_WON;
        }
    }
    else if (e == N * N - (existsT ? 1 : 0)) {
        return DRAW;
    }
    else {
        return UNCOMPLETED;
    }
}

void solveCase (int caseNum) {
    vector<string> a(N);
    for (int i = 0; i < N; ++i) {
        cin >> a[i];
    }
    
    PositionStatus positionStatus = getPositionStatus(a);
    
    cout << "Case #" << caseNum + 1 << ": ";
    switch (positionStatus) {
        case DRAW:
            cout << "Draw";
            break;
        case X_WON:
            cout << "X won";
            break;
        case O_WON:
            cout << "O won";
            break;
        case UNCOMPLETED:
            cout << "Game has not completed";
    }
    cout << "\n";
}

int main () {
    int testsCount;
    cin >> testsCount;
    for (int i = 0; i < testsCount; ++i) {
        solveCase(i);
    }
    return 0;
}
