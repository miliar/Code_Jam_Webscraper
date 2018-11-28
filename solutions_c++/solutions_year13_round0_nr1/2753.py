#include <iostream>
#include <string>
#include <vector>

using namespace std;

int depth(int r, int c, int dr, int dc, char lookedFor, const vector<string> &v) {
    if (r < 0 || r >= 4 || c < 0 || c >= 4) return 0;
    if (!(v[r][c] == lookedFor || v[r][c] == 'T')) {
        return 0;
    }
    return 1 + depth(r+dr,c+dc,dr,dc,lookedFor,v);
}

bool check(char c, const vector<string> &v) {
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            if (depth(i,j,0,1,c,v) >= 4) return true;
            if (depth(i,j,1,0,c,v) >= 4) return true;
            if (depth(i,j,1,1,c,v) >= 4) return true;
            if (depth(i,j,1,-1,c,v) >= 4) return true;
        }
    }
    return false;
}

void solve() {
    vector<string> board(4);
    for (int i = 0; i < 4; ++i) cin >> board[i];
    if (check('X',board)) { 
        cout << "X won" << endl;
        return;
    } 
    if (check('O',board)) {
        cout << "O won" << endl;
        return;
    }
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            if (board[i][j] == '.') {
                cout << "Game has not completed" << endl;
                return;
            }
        }
    }
    cout << "Draw" << endl;
    return;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; ++i) {
        cout << "Case #" << (i+1) << ": ";
        solve();
    }
}
