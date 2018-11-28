#include <fstream>

using namespace std;

int c2i(char c) {
    switch(c) {
        case 'Q': return 0;
        case 'W': return 1;
        case 'E': return 2;
        case 'R': return 3;
        case 'A': return 4;
        case 'S': return 5;
        case 'D': return 6;
        case 'F': return 7;
        default: return 8;
    }
}

int main(int argc, char* argv[]) {
    ifstream fin(argv[1]);
    ofstream fout(argv[2]);
    int T;
    fin >> T;

    for (int t = 1; t <= T; ++t) {
        int C;
        fin >> C;
        char base1, base2, nonbase;
        char combination[9][9];
        bool opposed[9][9];
        for (int i = 0; i < 9; ++i)
            for (int j = 0; j < 9; ++j) {
                combination[i][j] = 0;
                opposed[i][j] = false;
            }
        for (int c = 0; c < C; ++c) {
            fin.get(base1).get(base1).get(base2).get(nonbase);
            combination[c2i(base1)][c2i(base2)] = combination[c2i(base2)][c2i(base1)] = nonbase;
        }
        int D;
        fin >> D;
        for (int d = 0; d < D; ++d) {
            fin.get(base1).get(base1).get(base2);
            opposed[c2i(base1)][c2i(base2)] = opposed[c2i(base2)][c2i(base1)] = true;
        }
        int N;
        fin >> N;
        fin.get(base1);
        char invoke[100];
        int top = -1;
        for (int n = 0; n < N; ++n) {
            fin.get(base1);
            bool opp = false;
            if (top >= 0 && combination[c2i(invoke[top])][c2i(base1)] != 0) {
                invoke[top] = combination[c2i(invoke[top])][c2i(base1)];
                continue;
            }
            for (int i = 0; i <= top; ++i) {
                if (opposed[c2i(invoke[i])][c2i(base1)]) {
                    top = -1;
                    opp = true;
                    break;
                }
            }
            if (opp)
                continue;
            invoke[++top] = base1;
        }
        fout << "Case #" << t << ": [";
        for (int i = 0; i < top; ++i)
            fout << invoke[i] << ", ";
        if (top >= 0)
            fout << invoke[top];
        fout << ']' << endl;
    }
}

