#include <fstream>

using namespace std;

char map[101][101];

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");

    int t;
    fin >> t;
    for (int cont = 1; cont <= t; ++cont) {
        int n;
        fin >> n;
        double total[n];
        double win[n];
        double wp[n], owp[n], oowp[n];

        for (int i = 0; i != n; ++i) {
            total[i] = win[i] = wp[i] = owp[i] = oowp[i] = 0;
        }

        for (int i = 0; i != n; ++i) {
            fin >> map[i];
            for (int j = 0; j != n; ++j) {
                switch (map[i][j]) {
                    case '.':
                        break;
                    case '0':
                        ++total[i];
                        break;
                    case '1':
                        ++win[i];
                        ++total[i];
                        break;
                }
            }
            wp[i] = win[i] / total[i];
        }

        for (int i = 0; i != n; ++i) {
            for (int j = 0; j != n; ++j) {
                if (map[i][j] == '.') continue;
                double tmp = (map[i][j] == '1') ? 0 : 1;
                owp[i] += (win[j] - tmp) / (total[j] - 1);
            }
            owp[i] /= total[i];
        }

        for (int i = 0; i != n; ++i) {
            for (int j = 0; j != n; ++j) {
                if (map[i][j] != '.') {
                    oowp[i] += owp[j];
                }
            }
            oowp[i] /= total[i];
        }

        fout << "Case #" << cont << ":" << endl;
        for (int i = 0; i != n; ++i) {
            fout << (0.25 * wp[i] + 0.5 * owp[i] + 0.25 * oowp[i]) << endl;
        }
    }


    fin.close();
    fout.close();
    return 0;
}
