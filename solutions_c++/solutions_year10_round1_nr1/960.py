#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void display(int size, int* data) {
    static const char cell[4] = ".RB";
    for ( int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            //cout << data[i*size + j];
            int c = data[i * size + j];
            if ( c > 2) {
                cout << "?";
            } else {
                cout << cell[data[i*size + j]];
            }
        }
        cout << endl;
    }
}

void rotate(int size, int* mat) {
    int* rotated = new int[size * size];
    for (int i = 0; i < size * size; i++ ) rotated[i] = 0;
    for (int row = 0; row < size; row++) {
        int target = size - 1;
        for (int column = size - 1; column >= 0; column--) {
            if (mat[row * size + column] != 0) {
                //cout << "(" << row << "," << column << ") -> (" << target << "," << (size - 1 - row) << ")" << endl;
                rotated[ target * size + (size - 1 - row)] = mat[row * size + column];
                target --;
            }
        }
        // for (; target >= 0; target--) {
        //     rotated[target * size + row] = 0;
        // }
    }
    memcpy(mat, rotated, sizeof(int) * size * size);
    delete[] rotated;
}

void show_state(int size, unsigned int* state, int shift) {
    for (int i = 0; i < size; i++) {
        for ( int j = 0; j < size; j++) {
            cout << (((state[i * size + j]) >> shift) & 0xff) << " ";
        }
        cout << endl;
    }
}

int propagate(int size, int* mat, unsigned int* state, int target, int row, int column, int shift) {
    if (row < 0 || row >= size ) return 0;
    if (column < 0 || column >= size) return 0;
    int pos = row * size + column;
    if (mat[pos] == mat[target]) {
        //cout << "propagate from " << row << "," << column << " to " << (target / size) << "," << (target % size) << endl;
        int cnt = ((state[pos] >> shift) & 0xff) + 1;
        state[target] = (((0xff << shift) ^ 0xffffffff) & state[target]) | (cnt << shift);
        //cout << hex << (0xff << shift) << " : " << ((0xff << shift) ^ 0xffffffff) << endl;
        //cout << hex << state[pos] << ", " << cnt << ", " << state[target] << dec << endl;
        return 1;
    }
    return 0;
}

int check(int size, int K, int*mat ) {
    unsigned int *state = new unsigned int[size * size];
    int filled = 0;
    for (int color = 1; color <= 2; color++) {
        for (int i = 0; i < size * size; i++ ) {
            if (mat[i] == color) {
                state[i] = 0;//0x010101;
            } else {
                state[i] = 0;
            }
        }
        
        for (int i = 0; i < size; i++) {
            for (int row = 0; row < size; row++) {
                for (int col = 0; col < size; col++) {
                    int p = row * size + col;
                    if (mat[p] == color) {
                        if (propagate(size, mat, state, p, row + 1, col, 0) ) {
                            // cout << "vertical\n";
                            // show_state(size, state, 0);
                        }
                        if (propagate(size, mat, state, p, row, col + 1, 8)) {
                            // cout << "horizontal\n";
                            // show_state(size, state, 8);
                        }
                        if (propagate(size, mat, state, p, row + 1, col + 1, 16)){
                            // cout << "diagonal1\n";
                            // show_state(size, state, 16);
                        }
                        if (propagate(size, mat, state, p, row - 1, col + 1, 24)){
                            // cout << "diagonal2\n";
                            // show_state(size, state, 24);
                        }
                    }
                }
            }
        }
        // for ( int i = 0; i < 4; i++ ) {
        //     cout << "#Color " << color << ", Direction " << i << endl;
        //     show_state(size, state, i * 8);
        // }
        for (int i = 0; i < size * size; i++) {
            for (int j = 0; j < 32; j+= 8) {
                if (((state[i] >> j) & 0xff) == K - 1) {
                    filled |= (1 << (color - 1));
                    break;
                }
            }
        }
    }
    delete[] state;
    return filled;
}

int main(int argc, char** argv) {
    ifstream f(argv[1]);
    int T;
    int N;
    int K;
    f >> T;
    for (int cn = 1; cn <= T; cn++) {
        f >> N >> K;
        //cout << N << ", " << K << endl;
        int *mat = new int[N * N];
        string line;
        int* ptr = mat;
        for (int i = 0; i < N; i++) {
            f >> line;
            //cout << line << endl;
            for (int j = 0; j < N; j++) {
                switch (line.c_str()[j]) {
                case '.':
                    *ptr = 0; break;
                case 'R':
                    *ptr = 1; break;
                case 'B':
                    *ptr = 2; break;
                default:
                    cerr << "error : " << line;
                    exit(-1);
                }
                ptr++;
            }
        }
        //display(N, mat);
        rotate(N, mat);
        //display(N, mat);
        cout << "Case #" << cn << ": ";
        switch (check(N, K, mat) ) {
        case 0: cout << "Neither\n"; break;
        case 1: cout << "Red\n"; break;
        case 2: cout << "Blue\n"; break;
        case 3: cout << "Both\n"; break;
        default:
            cout << "???\n"; break;
        }
        //fall(N, mat);
        delete[] mat;
    }
    
        
    return 0;
}
