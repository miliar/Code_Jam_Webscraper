#include <vector>
#include <set>
#include <map>
#include <deque>
#include <algorithm>
#include <sstream>
#include <cmath>
#include <cstdio>
#include <iostream>

using namespace std;

int main ()
{
    int T, R, C;
    vector<vector<int> > field;
    string str;
    bool possible;
    char *letters = ".#/\\\\/";

    cin >> T;
    for (int test = 0; test < T; ++test) {
        printf ("Case #%d:\n", test + 1);

        cin >> R >> C;
        field.assign (R, vector<int> (C, 0));
        possible = true;

        for (int i = 0; i < R; ++i) {
            cin >> str;

            for (int j = 0; j < C; ++j) {
                if (str[j] == '#') {
                    field[i][j] = 1;
                }
            }
        }


        for (int i = 0; i < R && possible; ++i) {
            for (int j = 0; j < C && possible; ++j) {
                if (field[i][j] == 1) {
                    if (i == R - 1 || j == C - 1) {
                        possible = false;
                        continue;
                    } else {
                        if (field[i + 1][j] == 1 && field[i][j + 1] == 1 &&
                            field[i + 1][j + 1] == 1) {

                            field[i][j] = 2;
                            field[i][j + 1] = 3;
                            field[i + 1][j] = 4;
                            field[i + 1][j + 1] = 5;
                        } else {
                            possible = false;
                        } 
                    }
                }
            }
        }

        if (!possible) {
            printf ("Impossible\n");
        } else {
            for (int i = 0; i < R; ++i) {
                for (int j = 0; j < C; ++j) {
                    printf ("%c", letters[field[i][j]]);
                }

                printf ("\n");
            }
        }
    }
    return 0;
}
