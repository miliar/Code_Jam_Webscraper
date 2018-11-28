#define FILENAME "A-small"
/* -------------------------------------------------------------------------- */
#include <iostream>
#include <fstream>
#include <map>
#include <sstream>
#include <vector>
#include <algorithm>

#define INPUT_EXT ".in"
#define OUTPUT_EXT ".out"
#define MAX_T 50
#define MAX_C 50
#define MAX_R 50

using namespace std;

int main(int argc, char** argv)
{
    fstream input(FILENAME INPUT_EXT);
    ofstream output(FILENAME OUTPUT_EXT, ios_base::out);

    int T = 0; // Test cases
    int R = 0; // Max. lines
    int C = 0; // Length of one line

    input >> T;
    for (int i=0; i<T; i++) {
        input >> R;
        input >> C;

        int numHash = 0;

        char matrix[R][C];
        for (int j=0; j<R; j++) {
            char line[C];
            input >> line;
            for (int k=0; k<C; k++) {
                matrix[j][k] = line[k];
                if (line[k] == '#') {
                    numHash++;
                }
            }
        }

        bool nosol = false;
        if (numHash%4 != 0) {
            nosol = true;
        }
        if (numHash == 0) {
            goto noHashes;
        }
        for (int j=0; j<R && nosol == false; j++) {
            for (int k=0; k<C && nosol == false; k++) {
                if (matrix[j][k] == '#') {
                    if (!(j+1 < R && k+1 < C)) {
                        nosol = true;
                    }
                    if (!(matrix[j][k+1] == '#' &&
                        matrix[j+1][k] == '#' && matrix [j+1][k+1] == '#')) {
                        nosol = true;
                    } else {
                        matrix[j][k] = '/';
                        matrix[j][k+1] = '\\';
                        matrix[j+1][k] = '\\';
                        matrix[j+1][k+1] = '/';
                    }
                }
            }
        }
noHashes:
        output << "Case #" << i+1 << ":" << endl;
        if (nosol == true) {
            output << "Impossible" << endl;
        } else {
            for (int j=0; j<R && nosol == false; j++) {
                for (int k=0; k<C && nosol == false; k++) {
                    output << matrix[j][k];
                }
                output << endl;
            }
        }
    }

    output.close();
    input.close();

    return 0;
}
