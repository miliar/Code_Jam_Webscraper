#include <fstream>
#include <iostream>

using namespace std;

char update(char old, char n) {
    if (old == '.' || n == '.')
        return '.';
    if (old == 'X' && n == 'X')
        return 'X';
    if (old == 'O' && n == 'O')
        return 'O';
    if (n == 'T')
        return old;
    if (old == 'T')
        return n;
    if (old == 'O' && n == 'X')
        return '.';
    if (old == 'X' && n == 'O')
        return '.';

    cout << "fail, old: " << old << ", new: " << n;
    return 'Z';
}

void processGame(ifstream &f) {
    string lines[4];
    bool game_over = true;
    char diags[2] = {'T', 'T'};
    char cols[4] = {'T', 'T', 'T', 'T'};
    char rows[4] = {'T', 'T', 'T', 'T'};

    for (int i = 0; i < 4; i++)
        getline(f, lines[i]);

    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            if (lines[i][j] == '.')
                game_over = false;
            cols[i] = update(cols[i], lines[i][j]);
            rows[i] = update(rows[i], lines[j][i]);
        }
        diags[0] = update(diags[0], lines[i][i]);
        diags[1] = update(diags[1], lines[i][3-i]);
    }

    for (int i = 0; i < 4; i++) {
        if (rows[i] == 'X' || cols[i] == 'X' || (i < 2 && diags[i] == 'X')) {
            cout << "X won";
            return;
        }
        if (rows[i] == 'O' || cols[i] == 'O' || (i < 2 && diags[i] == 'O')) {
            cout << "O won";
            return;
        }
    }

    if (game_over)
        cout << "Draw";
    else
        cout << "Game has not completed";
}

int main(int argc, char **argv) {
    ifstream f(argv[1]);
    string line;
    getline(f, line);
    int num_testcases = atoi(line.c_str());

    for (int i = 0; i < num_testcases; i++) {
        cout << "Case #" << (i+1) << ": ";
        processGame(f);
        cout << endl;
        getline(f, line);
    }
}
