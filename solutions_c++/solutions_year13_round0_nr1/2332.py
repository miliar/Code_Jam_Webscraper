#include <iostream>
#include <string>
#include <vector>

using namespace std;

string solve()
{
    vector<vector<char> > m(4, vector<char>(4, '\0'));
    bool incomplete = false;
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            cin >> m[i][j];
            if (m[i][j] == '.') incomplete = true;
        }
    }

    int c_o[2] = {0, 0}, c_x[2] = {0, 0};
    for (int i = 0; i < 4; ++i) {
        switch (m[i][i]) {
        case 'O':
            ++c_o[0];
            break;
        case 'X':
            ++c_x[0];
            break;
        case 'T':
            ++c_o[0];
            ++c_x[0];
            break;
        default:
            break;
        }

        switch (m[i][3 - i]) {
        case 'O':
            ++c_o[1];
            break;
        case 'X':
            ++c_x[1];
            break;
        case 'T':
            ++c_o[1];
            ++c_x[1];
            break;
        default:
            break;
        }

        int cnt_o[2] = {0, 0}, cnt_x[2] = {0, 0};
        for (int j = 0; j < 4; ++j) {
            switch (m[i][j]) {
            case 'O':
                ++cnt_o[0];
                break;
            case 'X':
                ++cnt_x[0];
                break;
            case 'T':
                ++cnt_o[0];
                ++cnt_x[0];
                break;
            default:
                break;
            }

            switch (m[j][i]) {
            case 'O':
                ++cnt_o[1];
                break;
            case 'X':
                ++cnt_x[1];
                break;
            case 'T':
                ++cnt_o[1];
                ++cnt_x[1];
                break;
            default:
                break;
            }

        }
        if (cnt_o[0] == 4 || cnt_o[1] == 4) {
            return "O won";
        } else if (cnt_x[0] == 4 || cnt_x[1] == 4) {
            return "X won";
        }
    }
    if (c_o[0] == 4 || c_o[1] == 4) {
        return "O won";
    } else if (c_x[0] == 4 || c_x[1] == 4) {
        return "X won";
    }

    if (incomplete) {
        return "Game has not completed";
    } else {
        return "Draw";
    }
}

int main()
{
    int t;
    cin >> t;
    for (int i = 1; i <= t; ++i) {
        cout << "Case #" << i << ": " << solve() << endl;
    }
    return 0;
}
