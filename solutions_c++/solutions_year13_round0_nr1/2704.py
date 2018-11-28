#include <iostream>
#include <cstdio>
using namespace std;

string a[11];

bool win(char c) {
    for(int i = 0; i < 4; ++i) {
        bool bad = false;
        for(int j = 0; j < 4; ++j)
            if (a[i][j] != c && a[i][j] != 'T')
                bad = true;
        if (!bad) return true;
    }

    for(int j = 0; j < 4; ++j) {
        bool bad = false;
        for(int i = 0; i < 4; ++i)
            if (a[i][j] != c && a[i][j] != 'T')
                bad = true;
        if (!bad) return true;
    }

    bool bad = false;
    for(int i = 0; i < 4; ++i)
        if (a[i][i] != c && a[i][i] != 'T')
            bad = true;
    if (!bad) return true;

    bad = false;
    for(int i = 0; i < 4; ++i)
        if (a[i][3-i] != c && a[i][3-i] != 'T')
            bad = true;
    if (!bad) return true;
    return false;
}

bool hasEmpty() {
    for(int i = 0; i < 4; ++i)
        for(int j = 0; j < 4; ++j)
            if (a[i][j] == '.')
                return true;
    return false;
}

int main() {
    freopen("A1.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int ntest; cin >> ntest;
    for(int test = 1; test <= ntest; ++test) {
        for(int i = 0; i < 4; ++i)
            cin >> a[i];

        cout << "Case #" << test << ": ";

        if (win('X')) cout << "X won";
        else if (win('O')) cout << "O won";
        else if (hasEmpty()) cout << "Game has not completed";
        else cout << "Draw";
        cout << endl;
    }
    return 0;
}
