/* 
 * File:   q1.cpp
 * Author: Milind
 *
 * Created on May 22, 2010, 9:09 AM
 */

#include <iostream>
using namespace std;

const int BLUE = 1;
const int RED = 2;

int checkDiag1(char table[][51], int n, int k, int leftcol, int toprow) {
    int bl_c, bl_r, tr_c, tr_r;
    bl_c = tr_c = leftcol;
    bl_r = tr_r = toprow;
    int retval = 0;
    bool loop = true;

    while (loop) {
        char prevColor = table[bl_r][bl_c];
        int contCount = 1;
        for (int i = bl_r - 1, j = bl_c + 1; i >= tr_r && j <= tr_c; i--, j++) {
            if (table[i][j] == prevColor) {
                contCount++;
                if (contCount >= k) {
                    if (prevColor == 'R')
                        retval |= RED;
                    else if (prevColor == 'B')
                        retval |= BLUE;
//                    cout << "ddd " << bl_r << "," << bl_c << " " << tr_r << "," << tr_c << endl;
                }
            } else {
                contCount = 1;
                prevColor = table[i][j];
            }
        }
        if (++bl_r >= n) {
            bl_r--;
            bl_c++;
        }
        if (++tr_c >= n) {
            tr_c--;
            tr_r++;
        }
        if (bl_r >= n - 1 && bl_c >= n - 1 && tr_c >= n - 1 && tr_r >= n - 1) {
            loop = false;
        }
    }
    return retval;
}

int checkDiag2(char table[][51], int n, int k, int leftcol, int toprow) {
    int tl_c, tl_r, br_c, br_r;
    tl_c = br_c = leftcol;
    tl_r = br_r = n - 1;
    int retval = 0;
    bool loop = true;

    while (loop) {
        char prevColor = table[tl_r][tl_c];
        int contCount = 1;
        for (int i = tl_r + 1, j = tl_c + 1; i <= br_r && j <= br_c; i++, j++) {
            if (table[i][j] == prevColor) {
                contCount++;
                if (contCount >= k) {
                    if (prevColor == 'R')
                        retval |= RED;
                    else if (prevColor == 'B')
                        retval |= BLUE;
//                    cout << "eee " << tl_r << "," << tl_c << " " << br_r << "," << br_c << endl;
                }
            } else {
                contCount = 1;
                prevColor = table[i][j];
            }
        }
        if (--tl_r < toprow) {
            tl_r++;
            tl_c++;
        }
        if (++br_c >= n) {
            br_c--;
            br_r--;
        }
        if (br_r <= toprow && br_c >= n - 1 && tl_c >= n - 1 && tl_r <= toprow) {
            loop = false;
        }
    }
    return retval;
}

int checkRow(char table[][51], int n, int k, int leftcol, int toprow) {
    int retval = 0;

    for (int i = toprow; i < n; i++) {
        char prevColor = table[i][n - 1];
        int contCount = 1;
        for (int j = n - 2; j >= leftcol; j--) {
            if (table[i][j] == prevColor) {
                contCount++;
                if (contCount >= k) {
                    if (prevColor == 'R')
                        retval |= RED;
                    else if (prevColor == 'B')
                        retval |= BLUE;
                }
            } else {
                contCount = 1;
                prevColor = table[i][j];
            }
        }
    }

    return retval;
}

int checkCol(char table[][51], int n, int k, int leftcol, int toprow) {
    int retval = 0;

    for (int j = n - 1; j >= 0; j--) {
        char prevColor = table[toprow][j];
        int contCount = 1;
        for (int i = toprow + 1; i < n; i++) {
            if (table[i][j] == prevColor) {
                contCount++;
                if (contCount >= k) {
                    if (prevColor == 'R')
                        retval |= RED;
                    else if (prevColor == 'B')
                        retval |= BLUE;
                }
            } else {
                contCount = 1;
                prevColor = table[i][j];
            }
        }
    }

    return retval;
}

int main(int argc, char** argv) {
    int t, n, k;
    char table[51][51];

    cin >> t;
    for (int count = 1; count <= t; count++) {
        cin >> n >> k;
        int leftcol = n - 1, toprow;
        for (int i = 0; i < n; i++) {
            cin >> table[i];

            // fix gravity
            int repl = n - 1;
            for (int j = n - 1; j >= 0; j--) {
                if (table[i][j] != '.') {
                    table[i][repl] = table[i][j];
                    repl--;
                }
            }
            // find length of current row to determine bounds
            if (repl + 1 < leftcol) {
                leftcol = repl + 1;
            }
            while (repl >= 0) {
                table[i][repl--] = '.';
            }
        }
        for (toprow = n - 1; toprow >= 0; toprow--) {
            if (table[toprow][n - 1] == '.')
                break;
        }
//        cout << toprow << " " << leftcol << endl;

        // start processing
        int check = 0;
        check |= checkDiag1(table, n, k, leftcol, toprow);
        check |= checkDiag2(table, n, k, leftcol, toprow);
        check |= checkRow(table, n, k, leftcol, toprow);
        check |= checkCol(table, n, k, leftcol, toprow);

        cout << "Case #" << count << ": ";
        if (check & BLUE) {
            if (check & RED) {
                cout << "Both";
            } else {
                cout << "Blue";
            }
        } else if (check & RED) {
            cout << "Red";
        } else {
            cout << "Neither";
        }
        cout << endl;
    }
    return 0;
}
