#include <fstream>
using namespace std;

const int dlin[] = {-1, 0, 0, 1};
const int dcol[] = {0, -1, 1, 0};

ifstream in;
ofstream out;

int H, W, alt[101][101];
char label[101][101];

char fill(int i, int j, char current) {
    label[i][j] = '@';

    int lowx = -1, lowy = -1, lowalt = alt[i][j];
    for (int t = 0; t < 4; ++t) {
        int lin = i + dlin[t];
        int col = j + dcol[t];
        if (lin >= 0 && lin < H && col >= 0 && col < W) {
            if (alt[lin][col] < lowalt)
                lowalt = alt[lin][col], lowx = lin, lowy = col;
        }
    }

    if (lowalt == alt[i][j]) // sink
        label[i][j] = current;
    else
        if (label[lowx][lowy] == '.')
            label[i][j] = fill(lowx, lowy, current);
        else
            label[i][j] = label[lowx][lowy];

    return label[i][j];
}


int main(int argc, char **argv) {

    in.open(argv[1]);
    out.open(argv[2]);

    int T;
    in >> T;

    for (int i = 1; i <= T; ++i) {

        in >> H >> W;
        for (int j = 0; j < H; ++j)
            for (int k = 0; k < W; ++k) {
                in >> alt[j][k];
                label[j][k] = '.';
            }

        char current = 'a';
        for (int j = 0; j < H; ++j)
            for (int k = 0; k < W; ++k)
                if (label[j][k] == '.')
                    if (fill(j, k, current) == current)
                        ++current;

        out << "Case #" << i << ":\n";
        for (int j = 0; j < H; ++j) {
            for (int k = 0; k < W; ++k)
                out << label[j][k] << " ";
            out << "\n";
        }
    }

    in.close();
    out.close();

    return 0;
}
