#include <fstream>

using namespace std;

int main(int argc, char** argv) {
    ifstream fin(argv[1]);
    ofstream fout(argv[2]);

    int T;
    fin >> T;
    for (int t = 1; t <= T; ++t) {
        int R, C;
        fin >> R >> C;
        char picture[51][51];
        bool possible = true;
        for (int r = 0; r < R; ++r) {
            fin >> picture[r];
        }
        for (int i = 0; i < R; ++i) {
            for (int j = 0; j < C; ++j) {
                if (picture[i][j] == '#') {
                    if (i == R-1 || j == C-1) {
                        possible = false;
                    }
                    else if (picture[i][j+1] == '#' && picture[i+1][j] == '#' && picture[i+1][j+1] == '#') {
                        picture[i][j] = '/';
                        picture[i+1][j+1] = '/';
                        picture[i+1][j] = '\\';
                        picture[i][j+1] = '\\';
                    }
                    else {
                        possible = false;
                    }
                }
                if (!possible)
                    break;
            }
            if (!possible)
                break;
        }
        fout << "Case #" << t << ':' << endl;
        if (possible) {
            for (int i = 0; i < R; ++i) {
                fout << picture[i] << endl;
            }
        }
        else fout << "Impossible" << endl;
    }
}

