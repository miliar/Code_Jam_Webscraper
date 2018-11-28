#include <fstream>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

void solve() {
    int a[4][4]; // 0 - O, 1 - X, -1 - ., 2 - T
    char c;
    bool cbd = true;

    for (int i = 0; i < 4; ++i)
        for (int j = 0; j < 4; ++j) {
            fin >> c;
            a[i][j] = (c == 'O' ? 0 :
                       c == 'X' ? 1 :
                       c == '.' ? -1 : 2);
            if (c == '.') cbd = false;
        }

    // rows
    int t;
    for (int i = 0; i < 4; ++i) {
        t = 2;
        for (int j = 0; j < 4; ++j)
            if (t == 2 || t == a[i][j] || a[i][j] == 2) {
                t = (a[i][j] == 2 ? t : a[i][j]);
            } else t = -2;
        if (t == 0 || t == 1) {
            // fout << "Row " << i + 1 << ": t = " << t << "; ";
            fout << (t == 0 ? 'O' : 'X') << " won" << endl;
            return;
        }
    }

    // cols
    for (int j = 0; j < 4; ++j) {
        t = 2;
        for (int i = 0; i < 4; ++i)
            if (t == 2 || t == a[i][j] || a[i][j] == 2) {
                t = (a[i][j] == 2 ? t : a[i][j]);
            } else t = -2;
        if (t == 0 || t == 1) {
            // fout << "Col " << j + 1 << ": t = " << t << "; ";
            fout << (t == 0 ? 'O' : 'X') << " won" << endl;
            return;
        }
    }

    // diag
    t = 2;
    for (int i = 0; i < 4; ++i) {
        if (t == 2 || t == a[i][i] || a[i][i] == 2) {
            t = (a[i][i] == 2 ? t : a[i][i]);
        } else t = -2;
    }
    if (t == 0 || t == 1) {
        // fout << "Diag 1: t = " << t << "; ";
        fout << (t == 0 ? 'O' : 'X') << " won" << endl;
        return;
    }

    t = 2;
    for (int i = 0; i < 4; ++i) {
        if (t == 2 || t == a[i][3-i] || a[i][3-i] == 2) {
            t = (a[i][3-i] == 2 ? t : a[i][3-i]);
        } else t = -2;
    }
    if (t == 0 || t == 1) {
        // fout << "Diag 2: t = " << t << "; ";
        fout << (t == 0 ? 'O' : 'X') << " won" << endl;
        return;
    }
    if (cbd)
        fout << "Draw" << endl;
    else
        fout << "Game has not completed" << endl;
}

int main()
{
    int t;
    fin >> t;
    for (int i = 1; i <= t; ++i) {
        fout << "Case #" << i << ": ";
        solve();
    }

    return 0;
}
