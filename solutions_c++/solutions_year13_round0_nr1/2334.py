#include <iostream>
#include <string>
using namespace std;

int check(int a, int b, int c, int d) {
    int x = a * b * c * d;
    if (x == 0) {
        return 0;
    }
    if ((x == 1) || (x == 3)) {
        return 1;
    }
    if ((x == 16) || (x == 24)) {
        return 2;
    }
    return 0;
}

int main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": ";
        int ar[4][4];
        bool empty = false;
        for (int j = 0; j < 4; ++j) {
            string s;
            cin >> s;
            for (int k = 0; k < 4; ++k) {
                if (s[k] == '.') {
                    ar[j][k] = 0;
                    empty = true;
                }
                if (s[k] == 'X') ar[j][k] = 1;
                if (s[k] == 'O') ar[j][k] = 2;
                if (s[k] == 'T') ar[j][k] = 3;
            }
        }

        int p = 0;
        for (int j = 0; j < 4; ++j) {
            p += check(ar[j][0], ar[j][1], ar[j][2], ar[j][3]);
            if (p) break;
            p += check(ar[0][j], ar[1][j], ar[2][j], ar[3][j]);
            if (p) break;
        }
        if (p == 0) p += check(ar[0][0], ar[1][1], ar[2][2], ar[3][3]);
        if (p == 0) p += check(ar[0][3], ar[1][2], ar[2][1], ar[3][0]);

        if (p == 1) {
            cout << "X won\n";
        } else if (p == 2) {
            cout << "O won\n";
        } else if (empty) {
            cout << "Game has not completed\n";
        } else {
            cout << "Draw\n";
        }
    }
}
