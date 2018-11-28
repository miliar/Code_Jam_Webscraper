#include <iostream>
#include <string>

using namespace std;

string d[4];

bool checkH(int i, char T) {
    return
        ((d[i][0] == T) || (d[i][0] == 'T')) &&
        ((d[i][1] == T) || (d[i][1] == 'T')) &&
        ((d[i][2] == T) || (d[i][2] == 'T')) &&
        ((d[i][3] == T) || (d[i][3] == 'T'));
}

bool checkV(int i, char T) {
    return
        ((d[0][i] == T) || (d[0][i] == 'T')) &&
        ((d[1][i] == T) || (d[1][i] == 'T')) &&
        ((d[2][i] == T) || (d[2][i] == 'T')) &&
        ((d[3][i] == T) || (d[3][i] == 'T'));
}

bool checkD(char T) {
    return
       (((d[0][0] == T) || (d[0][0] == 'T')) &&
        ((d[1][1] == T) || (d[1][1] == 'T')) &&
        ((d[2][2] == T) || (d[2][2] == 'T')) &&
        ((d[3][3] == T) || (d[3][3] == 'T'))) ||

       (((d[0][3] == T) || (d[0][3] == 'T')) &&
        ((d[1][2] == T) || (d[1][2] == 'T')) &&
        ((d[2][1] == T) || (d[2][1] == 'T')) &&
        ((d[3][0] == T) || (d[3][0] == 'T')));
}

int main(int argc, char* argv[])
{
    int T;
    cin >> T;
    for (int t = 0; t != T; ++t) {
        for (int i = 0; i != 4; ++i)
            cin >> d[i];
        for (int i = 0; i != 4; ++i) {
            if (checkH(i, 'O') || checkV(i, 'O')) {
                cout << "Case #" << (t + 1) << ": O won\n";
                goto __continue_outer;
            }
            if (checkH(i, 'X') || checkV(i, 'X')) {
                cout << "Case #" << (t + 1) << ": X won\n";
                goto __continue_outer;
            }
        }
        if (checkD('O')) {
            cout << "Case #" << (t + 1) << ": O won\n";
            goto __continue_outer;
        }
        if (checkD('X')) {
            cout << "Case #" << (t + 1) << ": X won\n";
            goto __continue_outer;
        }
        for (int i = 0; i != 4; ++i) {
            for (int j = 0; j != 4; ++j) {
                if (d[i][j] == '.')
                    goto __not_draw;
            }
        }
        cout << "Case #" << (t + 1) << ": Draw\n";
        goto __continue_outer;
        __not_draw:
        cout << "Case #" << (t + 1) << ": Game has not completed\n";
        __continue_outer: {}
    }
    return 0;
}

