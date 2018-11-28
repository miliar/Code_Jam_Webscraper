#include <cstdio>
using namespace std;
#include <iostream>
#include <vector>
#include <string>

bool wins(char X, char a) {
    return (a == X) || (a == 'T');
}

bool wins(vector<string> a, char X, int i, int j, int di, int dj) {
    for (int k = 0; k < 4; ++k) {
        if (!wins(X, a[i + di * k][j + dj * k])) return false;
    }
    return true;
}

bool wins(vector<string> a, char X) {
    for (int i = 0; i < 4; ++i) {
        if (wins(a, X, 0, i, 1, 0) || wins(a, X, i, 0, 0, 1)) return true;
    }
    if (wins(a, X, 0, 0, 1, 1) || wins(a, X, 3, 0, -1, 1)) return true;
    return false;
}


void solve(int t) {
    vector<string> a(4);
    cin >> a[0] >> a[1] >> a[2] >> a[3];
    cout << "Case #" << t << ": ";
    bool X = wins(a, 'X');
    bool O = wins(a, 'O');
    if (X && !O) cout << "X won";
    if (X && O) while (true) cerr << "BUG" << endl;
    if (!X && !O) {
        bool has_free = false;
        for (int i = 0; i < 4; ++i) for (int j = 0; j < 4; ++j) if (a[i][j] == '.') has_free = true;
        if (has_free) cout << "Game has not completed"; else cout << "Draw";
    }
    if (!X && O) cout << "O won";
    cout << endl;
}


int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        solve(i + 1);
    }
}

