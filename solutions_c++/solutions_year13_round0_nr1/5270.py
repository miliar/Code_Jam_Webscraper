#include <iostream>
#include <sstream>
#include <algorithm>
#include <fstream>
#include <set>
#include <vector>
#include <map>

using namespace std;

int main() {
    ifstream cin("A-large.in");
    ofstream cout("out.txt");
    int T;
    cin >> T;
    for (size_t t = 1; t <= T; t++) {
        char f[4][4];
        bool dot = false;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                cin >> f[i][j];
                if (f[i][j] == '.')
                    dot = true;
            }
        }
        char cur = '.';
        bool ok = true;
        for (size_t i = 0; i < 4; i++) {
            cur = f[i][0];
            ok = true;
            for (size_t j = 1; j < 4; j++) {
                if (cur == 'T')
                    cur = f[i][j];
                else if (f[i][j] != 'T' && cur != f[i][j])
                    ok = false;
            }
            if (ok && cur != '.')
                break;
            cur = f[0][i];
            ok = true;
            for (size_t j = 1; j < 4; j++) {
                if (cur == 'T')
                    cur = f[j][i];
                else if (f[j][i] != 'T' && cur != f[j][i])
                    ok = false;
            }
            if (ok && cur != '.')
                break;
        }
        if (! ok || cur == '.') {
            cur = f[0][0];
            ok = true;
            for (size_t i = 1; i < 4; i++) {
                if (cur == 'T')
                    cur = f[i][i];
                else if (f[i][i] != 'T' && cur != f[i][i])
                    ok = false;
            }
            if (! ok || cur == '.') {
                cur = f[0][3];
                ok = true;
                for (size_t i = 1; i < 4; i++) {
                    if (cur == 'T')
                        cur = f[i][3-i];
                    else if (f[i][3-i] != 'T' && cur != f[i][3-i])
                        ok = false;
                }
            }
        }
        cout << "Case #" << t << ": ";
        if (ok && cur != '.')
            cout << cur << " won";
        else if (dot)
            cout << "Game has not completed";
        else
            cout << "Draw";
        cout << endl;
    }
}

