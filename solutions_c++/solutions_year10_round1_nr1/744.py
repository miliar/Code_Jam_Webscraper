#include <iostream>
#include <algorithm>

using namespace std;

/*
void dump(char * const * const grid, int N) {
    for (int row = 0; row < N; row++) {
        for (int col = 0; col < N; col++) {
            cout << grid[row][col];
        }
        cout << endl;
    }
}
*/

bool isFull(char c) {
    return c != '.';
}

void doCase(int caseNum) {
    int N, K;

    cin >> N >> K;

    char grid[N][N];
    memset(&grid, 0, sizeof(grid));

    for (int row = 0; row < N; row++) {
        for (int col = 0; col < N; col++) {
            cin >> grid[row][col];
        }
    }

    // Rotate
    // Eliminate blank spaces in each row starting from the right
    for (int rnum = 0; rnum < N; rnum++) {
        bool done;

        char* row = grid[rnum];
        do {
            done = true;
            for (int col = N-2; col >= 0; col--) {
                if (isFull(row[col]) && !isFull(row[col+1])) {
                    swap(row[col], row[col+1]);
                    done = false;
                }
            }
        } while (!done);
    }

    bool red = false, blue = false;

    // Across
    for (int rnum = 0; rnum < N && !(red && blue); rnum++) {
        bool done;

        char* row = grid[rnum];

        char status = '.';
        char count = 0;
        for (int col = N - 1; col >= 0 && isFull(row[col]); col--) {
            if (row[col] == status) {
                if (++count >= K) {
                    if (status == 'R') red = true;
                    else if (status == 'B') blue = true;
                }
            } else {
                status = row[col];
                count = 1;
            }
        }
    }

    // Down
    for (int cnum = 0; cnum < N && !(red && blue); cnum++) {

        char status = '.';
        char count = 0;
        for (int rnum = 0; rnum < N; rnum++) {
            if (grid[rnum][cnum] == status) {
                if (++count >= K) {
//                    cout << "Found a string of " << K << " " << status << endl;
                    if (status == 'R') red = true;
                    else if (status == 'B') blue = true;
                }
            } else {
                status = grid[rnum][cnum];
                count = 1;
            }
        }
    }

    // Top-left to bottom-right
    for (int startrow = 0; startrow < N && !(red && blue); startrow++) {
        for (int startcol = 0; startcol < N && !(red && blue); startcol++) {
            bool done;

            char status = '.';
            char count = 0;
            for (int offset = 0; startrow + offset < N && startcol + offset < N; offset++) {
                if (grid[startrow + offset][startcol + offset] == status) {
                    if (++count >= K) {
                        if (status == 'R') red = true;
                        else if (status == 'B') blue = true;
                    }
                } else {
                    status = grid[startrow + offset][startcol + offset];
                    count = 1;
                }
            }
        }
    }

    // Top-right to bottom-left
    for (int startrow = 0; startrow < N && !(red && blue); startrow++) {
        for (int startcol = 0; startcol < N && !(red && blue); startcol++) {
            bool done;

            char status = '.';
            char count = 0;
            for (int offset = 0; startrow + offset < N && startcol - offset >= 0; offset++) {
                if (grid[startrow + offset][startcol - offset] == status) {
                    if (++count >= K) {
                        if (status == 'R') red = true;
                        else if (status == 'B') blue = true;
                    }
                } else {
                    status = grid[startrow + offset][startcol - offset];
                    count = 1;
                }
            }
        }
    }

    const char *result;
    if (red && blue) {
        result = "Both";
    } else if (red) {
        result = "Red";
    } else if (blue) {
        result = "Blue";
    } else {
        result = "Neither";
    }
    
    cout << "Case #" << caseNum << ": " << result << endl;
    /*
    cout << "K == " << K << endl;
    for (int row = 0; row < N; row++) {
        for (int col = 0; col < N; col++) {
            cout << grid[row][col];
        }
        cout << endl;
    }
    */
}

int main() {
    int T;
    cin >> T;

    for (int i = 0; i < T; i++) {
        doCase(i + 1);
    }
}
