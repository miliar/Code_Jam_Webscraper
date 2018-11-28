#include <fstream>
#include <iostream>
using namespace std;

ifstream fin("tic.in");
ofstream fout("tic.out");

char s[5][5];
char type[2] = {'X', 'O'};

bool canDraw() {
    for (int i = 1; i <= 4; ++i)
        for (int j = 1; j <= 4; ++j)
            if (s[i][j] == '.')
                return 0;
    return 1;
}

bool testDiag(char c) {
    bool d1 = 1, d2 = 1;
    for (int i = 1; i <= 4; ++i) {
        if (s[i][i] != c && s[i][i] != 'T')
            d1 = 0;
        if (s[i][5 - i] != c && s[i][5 - i] != 'T')
            d2 = 0;
    }
    return d1 || d2;
}

bool testLine(int line, char c) {
    for (int i = 1; i <= 4; ++i)
        if (s[line][i] != c && s[line][i] != 'T')
            return 0;
    return 1;
}

bool testColumn(int col, char c) {
    for (int i = 1; i <= 4; ++i)
        if (s[i][col] != c && s[i][col] != 'T')
            return 0;
    return 1;
}


void solve() {
    int win = 0;

    for (int i = 0; i <= 1 && !win; ++i) {
        if (testDiag(type[i])) {
            win = i + 1;
            break;
        }
        for (int j = 1; j <= 4; ++j)
            if (testLine(j, type[i]) || testColumn(j, type[i])) {
                win = i + 1;
                break;
            }
    }

    if (win) {
        if (win == 1)
            fout << "X won";
        else
            fout << "O won";
    }
    else {
        if (canDraw())
            fout << "Draw";
        else
            fout << "Game has not completed";
    }

    fout << "\n";
}

int main() {
    int T;
    fin >> T;

    for (int i = 1; i <= T; ++i) {
        fin.get();

        for (int i = 1; i <= 4; ++i)
            fin.getline(s[i] + 1, 5);

        fout << "Case #" << i << ": ";
        solve();
    }

    return 0;
}



