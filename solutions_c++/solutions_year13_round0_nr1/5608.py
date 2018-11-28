
#include <fstream>
using namespace std;

int main()
{
    ifstream fin("A-small-attempt1.in");
    ofstream fou("out");
    int n;
    fin >> n;
    char b[4][4];
    for (int i = 0; i < n; ++i) {

        bool draw = true;
        for (int r = 0; r < 4; ++r)
            for (int c = 0; c < 4; ++c) {
                fin >> b[r][c];
                if ('.' == b[r][c]) draw = false;
            }

        fou << "Case #" << i + 1 << ": ";

        if ('T' == b[0][0] &&
            '.' != b[1][1] && b[1][1] == b[2][2] && b[2][2] == b[3][3]) {
            fou << b[1][1] << " won" << endl;
            continue;
        }

        if ('.' != b[0][0] &&
            (b[0][0] == b[1][1] || 'T' == b[1][1]) &&
            (b[1][1] == b[2][2] || 'T' == b[2][2]) &&
            (b[2][2] == b[3][3] || 'T' == b[3][3])) {
            fou << b[0][0] << " won" << endl;
            continue;
        }

        if ('T' == b[0][3] &&
            '.' != b[1][2] && b[1][2] == b[2][1] && b[2][1] == b[3][0]) {
            fou << b[1][2] << " won" << endl;
            continue;
        }

        if ('.' != b[0][3] &&
            (b[0][3] == b[1][2] || 'T' == b[1][2]) &&
            (b[1][2] == b[2][1] || 'T' == b[2][1]) &&
            (b[2][1] == b[3][0] || 'T' == b[3][0])) {
            fou << b[0][3] << " won" << endl;
            continue;
        }

        bool ok = false;
        for (int j = 0; j < 4; ++j) {
            if ('T' == b[j][0] &&
                '.' != b[j][1] && b[j][1] == b[j][2] && b[j][2] == b[j][3]) {
                fou << b[j][1] << " won" << endl;
                ok = true;
                break;
            }

            if ('T' == b[0][j] &&
                '.' != b[1][j] && b[1][j] == b[2][j] && b[2][j] == b[3][j]) {
                fou << b[1][j] << " won" << endl;
                ok = true;
                break;
            }

            if ('.' != b[j][0] &&
                (b[j][0] == b[j][1] || 'T' == b[j][1]) &&
                (b[j][1] == b[j][2] || 'T' == b[j][2]) &&
                (b[j][2] == b[j][3] || 'T' == b[j][3])) {
                fou << b[j][0] << " won" << endl;
                ok = true;
                break;
            }

            if ('.' != b[0][j] &&
                (b[0][j] == b[1][j] || 'T' == b[1][j]) &&
                (b[1][j] == b[2][j] || 'T' == b[2][j]) &&
                (b[2][j] == b[3][j] || 'T' == b[3][j])) {
                fou << b[0][j] << " won" << endl;
                ok = true;
                break;
            }
        }

        if (!ok) {
            if (draw) fou << "Draw" << endl;
            else fou << "Game has not completed" << endl;
        }

    }
    return 0;
}
