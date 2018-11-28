#include <cstdio>
#include <cstring>
#include <string>
using namespace std;

bool win(const char table[4][5], char mine, char both)
{
    int row[4], col[4], diag[2];
    memset(row, 0, sizeof(row));
    memset(col, 0, sizeof(col));
    memset(diag, 0, sizeof(diag));
    for(int r=0; r<4; ++r) {
        for (int c=0; c<4; ++c) {
            if (mine==table[r][c] || both==table[r][c]) {
                ++row[r];
                ++col[c];
                if (r-c == 0) ++diag[0];
                if (r+c == 3) ++diag[1];
            }
        }
    }
    for(int i=0; i<4; ++i) {
        if (row[i]==4 || col[i]==4) return true;
    }
    if (diag[0]==4 || diag[1]==4) return true;
    return false;
}

bool full(const char table[4][5])
{
    for (int r=0; r<4; ++r) {
        for (int c=0; c<4; ++c) {
            if (table[r][c]=='.') {
                return false;
            }
        }
    }
    return true;
}

int main(int argc, char** argv)
{
    FILE *input, *output;
    if (argc==2) {
        input = fopen(argv[1], "r");
        output = fopen((string(argv[1])+".out").c_str(), "w");
    } else {
        return 1;
    }
    int T;
    char M[4][5];
    fscanf(input, "%d", &T);
    for (int z=1; z<=T; ++z) {
        for (int i=0; i<4; ++i) {
            fscanf(input, "%s", M[i]);
        }
        bool O = win(M, 'O', 'T');
        bool X = win(M, 'X', 'T');
        bool F = full(M);
        fprintf(output, "Case #%d: ", z);
        if (O) {
            fputs("O won\n", output);
        } else if(X) {
            fputs("X won\n", output);
        } else if(F) {
            fputs("Draw\n", output);
        } else {
            fputs("Game has not completed\n", output);
        }
    }
    return 0;
}
