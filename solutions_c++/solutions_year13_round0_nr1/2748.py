#include <iostream>

using namespace std;

int T, n;
char a[4][4];

void check(char c, int& now) {
    if (now == -1) return;
    if (c == '.') {
        now = -1;
        return;
    }
    if (c == 'X' && now == 2) {
        now = -1;
        return;
    }
    if (c == 'O' && now == 1) {
        now = -1;
        return;
    }
    if (c == 'X') now = 1;
    if (c == 'O') now = 2;
}

int main() {
    cin >> T;
    for(int t = 0; t < T; ++t) {
        bool freecell = false;
        for(int i = 0; i < 4; ++i) {
            for(int j = 0; j < 4; ++j) {
                cin >> a[i][j];
                if (a[i][j] == '.') {
                    freecell = true;
                }
            }
        }
        int ans = 0;
        for(int i = 0; i < 4; ++i) {
            int now = 0;
            for(int j = 0; j < 4; ++j) {
                check(a[i][j], now);
            }
            if (now > 0) {
                ans = now;
            }
        }
        for(int i = 0; i < 4; ++i) {
            int now = 0;
            for(int j = 0; j < 4; ++j) {
                check(a[j][i], now);
            }
            if (now > 0) {
                ans = now;
            }
        }
        int now = 0;
        for(int i = 0; i < 4; ++i) {
            check(a[i][i], now);
        }
        if (now > 0) {
            ans = now;
        }
        now = 0;
        for(int i = 0; i < 4; ++i) {
            check(a[i][3 - i], now);
        }
        if (now > 0) {
            ans = now;
        }

        cout << "Case #" << t + 1 << ": ";
        if (ans) {
            if (ans == 1) {
                cout << "X won" << endl;
            } else {
                cout << "O won" << endl;
            }
        } else {
            if (freecell) {
                cout << "Game has not completed" << endl;
            } else {
                cout << "Draw" << endl;
            }
        }
    }
}
