#include <iostream>

using namespace std;

void x_won() { cout << "X won"; }
void o_won() { cout << "O won"; }
void draw() { cout << "Draw"; }
void incomplete() { cout << "Game has not completed"; }

void do_testcase() {
    short int row_sums[4];
    short int col_sums[4];
    short int diag1_sum = 0, diag2_sum = 0;
    for (unsigned short int i = 0; i < 4; ++i) {
        row_sums[i] = col_sums[i] = 0;
    }
    short int t_row = -7, t_col = -7;

    bool filled = true;
    for (unsigned short int i = 0; i < 4; ++i) {
        for (unsigned short int j = 0; j < 4; ++j) {
            char c;
            short int x = 0;
            cin >> c;
            switch (c) {
                case '.':
                    filled = false;
                    break;
                case 'X':
                    x = 1;
                    break;
                case 'O':
                    x = -1;
                    break;
                case 'T':
                    t_row = i;
                    t_col = j;
                    break;
            }
            row_sums[i] += x;
            col_sums[j] += x;
            if (i == j) {
                diag1_sum += x;
            }
            if (i == 3 - j) {
                diag2_sum += x;
            }
        }
    }

    bool xw = false, ow = false;
    if (diag1_sum == 4 || (diag1_sum == 3 && t_row == t_col)) {
        xw = true;
    }
    if (diag1_sum == -4 || (diag1_sum == -3 && t_row == t_col)) {
        ow = true;
    }
    if (diag2_sum == 4 || (diag2_sum == 3 && t_row == 3 - t_col)) {
        xw = true;
    }
    if (diag2_sum == -4 || (diag2_sum == -3 && t_row == 3 - t_col)) {
        ow = true;
    }
    for (unsigned short int i = 0; i < 4; ++i) {
        if (row_sums[i] == 4 || (row_sums[i] == 3 && t_row == i)) {
            xw = true;
        }
        if (col_sums[i] == 4 || (col_sums[i] == 3 && t_col == i)) {
            xw = true;
        }
        if (row_sums[i] == -4 || (row_sums[i] == -3 && t_row == i)) {
            ow = true;
        }
        if (col_sums[i] == -4 || (col_sums[i] == -3 && t_col == i)) {
            ow = true;
        }
    }
    if (xw && ow) {
        draw();
    } else if (xw) {
        x_won();
    } else if (ow) {
        o_won();
    } else if (!filled) {
        incomplete();
    } else {
        draw();
    }
}

int main(int argc, char *argv[]) {
    unsigned int T;
    cin >> T;
    for (unsigned int i = 0; i < T; ++i) {
        cout << "Case #" << (i + 1) << ": ";
        do_testcase();
        cout << endl;
    }
}
