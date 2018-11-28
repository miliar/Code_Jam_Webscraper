#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cstdlib>

using namespace std;

int main(int argc, char** argv) {

    ifstream in("input.in");
    ofstream out("output.out");

    int O = 0, X = 1, T = 2, D = 4;
    int N;
    string str;
    in >> N;

    for (int cs = 0; cs < N; cs++) {
        getline(in, str);
        vector< vector<int> > g(4);
        bool wf = false;
        bool e_s = false;

        for (int r = 0; r < 4; r++) {
            getline(in, str);
            for (int c = 0; c < str.size(); c++) {
                if (str[c] == 'O') g[r].push_back(O);
                if (str[c] == 'X') g[r].push_back(X);
                if (str[c] == 'T') g[r].push_back(T);
                if (str[c] == '.') {
                    g[r].push_back(D);
                    e_s = true;
                }
            }
        }

        int x_g = 0, o_g = 0;
        int c_x_g = 0, c_o_g = 0;

        for (int i = 0; i < 4; i++) {
            if (g[i][i] == X || g[i][i] == T) x_g++;
            if (g[i][i] == O || g[i][i] == T) o_g++;

            if (g[i][3 - i] == X || g[i][3 - i] == T) c_x_g++;
            if (g[i][3 - i] == O || g[i][3 - i] == T) c_o_g++;
        }

        if (x_g == 4 || c_x_g == 4) {
            out << "Case #" << cs + 1 << ": X won" << endl;
            wf = true;
        }
        if (o_g == 4 || c_o_g == 4) {
            out << "Case #" << cs + 1 << ": O won" << endl;
            wf = true;
        }

        if (!wf)
            for (int i = 0; i < 4; i++) {
                x_g = 0;
                o_g = 0;
                c_x_g = 0, c_o_g = 0;

                for (int j = 0; j < 4; j++) {
                    if (g[i][j] == X || g[i][j] == T) x_g++;
                    if (g[i][j] == O || g[i][j] == T) o_g++;

                    if (g[j][i] == X || g[j][i] == T) c_x_g++;
                    if (g[j][i] == O || g[j][i] == T) c_o_g++;
                }

                if (x_g == 4 || c_x_g == 4) {
                    out << "Case #" << cs + 1 << ": X won" << endl;
                    wf = true;
                }

                if (o_g == 4 || c_o_g == 4) {
                    out << "Case #" << cs + 1 << ": O won" << endl;
                    wf = true;
                }
            }

        if (!wf) {
            if (e_s)
                out << "Case #" << cs + 1 << ": Game has not completed" << endl;
            else
                out << "Case #" << cs + 1 << ": Draw" << endl;
        }

    }
    return 0;
}

