#include <fstream>

using namespace std;

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");

    int t;
    fin >> t;
    for (int cont = 1; cont <= t; ++cont) {
        int r, c;
        fin >> r >> c;
        char map[r][c];

        for (int i = 0; i != r; ++i) {
            for (int j = 0; j != c; ++j) {
                fin >> map[i][j];
            }
        }

        bool answer = true;

        for (int i = 0; i != r; ++i) {
            for (int j = 0; j != c; ++j) {
                if (map[i][j] == '#') {
                    if ((i + 1 >= r) || (j + 1 >= c)
                        || (map[i + 1][j] != '#') || (map[i][j + 1] != '#') || (map[i + 1][j + 1] != '#')) {
                        answer = false;
                        break;
                    }
                    else {
                        map[i][j] = '/';
                        map[i + 1][j] = '\\';
                        map[i][j + 1] = '\\';
                        map[i + 1][j + 1] = '/';
                    }
                }
            }
            if (!answer) break;
        }

        fout << "Case #" << cont << ":" << endl;
        if (answer) {
            for (int i = 0; i != r; ++i) {
                for (int j = 0; j != c; ++j) {
                    fout << map[i][j];
                }
                fout << endl;
            }
        }
        else {
            fout << "Impossible" << endl;
        }
    }


    fin.close();
    fout.close();
    return 0;
}
