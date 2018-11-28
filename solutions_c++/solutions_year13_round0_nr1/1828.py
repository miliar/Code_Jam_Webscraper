#include <cstdio>
#include <iostream>

using namespace std;
string mat[4];

bool puno() {
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            if (mat[i][j] == '.') {
                return false;
            }
        }
    }
    return true;
}

bool wins(char c) {
    bool ok = true;
    for (int i = 0; i < 4; i++) {
        if (mat[i][i] != c && mat[i][i] != 'T') {
            ok = false;
            break;
        }
    }

    if (ok) return true;
    ok = true;
    
    for (int i = 0; i < 4; i++) {
        if (mat[i][3-i] != c && mat[i][3-i] != 'T') {
            ok = false;
            break;
        }
    }

    if (ok) return true;
    ok = true;

    for (int i = 0; i < 4; i++) {
        ok = true;
        for (int j = 0; j < 4; j++) {
            if (mat[i][j] != c && mat[i][j] != 'T') {
                ok = false;
                break;
            }
        }
        if (ok) return true;
    }

    if (ok) return true;
    ok = true;

    for (int i = 0; i < 4; i++) {
        ok = true;
        for (int j = 0; j < 4; j++) {
            if (mat[j][i] != c && mat[j][i] != 'T') {
                ok = false;
                break;
            }
        }
        if (ok) return true;
    }
    if (ok) return true;
    ok = true;

    return false;
}

int main() {
    
    int t;
    cin >> t;
    for (int kei = 1; kei <= t; kei++) {
        cout << "Case #" << kei << ": ";
        bool full = true;
        bool tapos = false;
        for (int i = 0; i < 4; i++) {
            cin >> mat[i];
        }
        if (wins('X')) {
            cout << "X won" << endl;
        }
        else if (wins('O')) {
            cout << "O won" << endl;
        }
        else if (puno()) {
            cout << "Draw" << endl;
        }
        else {
            cout << "Game has not completed" << endl;
        }
    }
    return 0;
}
