#include <iostream>
#include <string>
using namespace std;

string s[4];

bool eq(char c, int i, int j) {
    return s[i][j] == c || s[i][j] == 'T';
}

bool won(char c) {
    bool res = false;

    bool d1 = true, d2 = true;
    for (int i = 0; i < 4; i++) {
        bool row = true, col = true;
        for (int j = 0; j < 4; j++) {
            row &= eq(c, i, j);
            col &= eq(c, j, i);
        }
        d1 &= eq(c, i, i);
        d2 &= eq(c, i, 3 - i);
        res |= row || col;
    }

    return res || d1 || d2;
}

int main()
{
    int t;
    cin >> t;

    for (int tc = 1; tc <= t; tc++) {
        bool completed = true;
        for (int j = 0; j < 4; j++) {
            cin >> s[j];
            completed &= s[j].find('.') == string::npos;
        }

        cout << "Case #" << tc << ": ";

        if (won('O')) cout << "O won";
        else if (won('X')) cout << "X won";
        else {
            if (!completed) cout << "Game has not completed";
            else cout << "Draw";
        }
        cout << endl;
    }

    return 0;
}
