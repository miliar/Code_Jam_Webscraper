/* 
 * File:   main.cpp
 * Author: waleed
 *
 * Created on April 13, 2013, 1:12 AM
 */

#include <cstdlib>
#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cstring>
#include <string>
#include <cctype>
#include <stack>
#include <queue>
#include <list>
#include <vector>
#include <map>
#include <sstream>
#include <cmath>
#include <bitset>
#include <utility>
#include <set>
#include <numeric>
#include <fstream>

#define INF_MAX 2147483647
#define INF_MIN -2147483647
#define pi acos(-1.0)
#define N 1000000
#define LL long long

#define For(i, a, b) for( int i = (a); i < (b); i++ )
#define Fors(i, sz) for( size_t i = 0; i < sz.size (); i++ )
#define Fore(it, x) for(typeof (x.begin()) it = x.begin(); it != x.end (); it++)
#define Set(a, s) memset(a, s, sizeof (a))
#define Read(r) freopen(r, "r", stdin)
#define Write(w) freopen(w, "w", stdout)

#define isOn(S, j) (S & (1 << j))
#define setBit(S, j) (S |= (1 << j))
#define clearBit(S, j) (S &= ~(1 << j))
#define toggleBit(S, j) (S ^= (1 << j))
#define lowBit(S) (S & (-S))
#define setAll(S, n) (S = (1 << n) - 1)

using namespace std;

int main(int argc, char** argv) {
    fstream cin("in.in", ios::in);
    fstream cout("out.out", ios::out);
    int cas;
    cin >> cas;
    for (int cs = 1; cs <= cas; cs++) {
        char boa[4][4];
        bool over = true, won = false;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                cin >> boa[i][j];
            }
        }
        bool x = true, o = true, no = true;
        for (int i = 0; i < 4 && !won; i++) {
            x = true, o = true, no = true;
            for (int j = 0; j < 4; j++) {
                if (boa[i][j] == 'X') {
                    o = false;
                    no = false;
                } else if (boa[i][j] == 'O') {
                    x = false;
                    no = false;
                } else if (boa[i][j] == '.') {
                    x = false;
                    o = false;
                    over = false;
                }
            }
            if (x || o) {
                won = true;
            }
        }
        if (!won) {
            x = true, o = true, no = true;

            for (int j = 0; j < 4 && !won; j++) {
                x = true, o = true, no = true;
                for (int i = 0; i < 4; i++) {
                    if (boa[i][j] == 'X') {
                        o = false;
                        no = false;
                    } else if (boa[i][j] == 'O') {
                        x = false;
                        no = false;
                    } else if (boa[i][j] == '.') {
                        x = false;
                        o = false;
                    }
                }
                if (x || o) {
                    won = true;
                }
            }
        }
        if (!won) {
            x = true, o = true, no = true;

            for (int i = 0, j = 0; i < 4 && !won; i++, j++) {
                if (boa[i][j] == 'X') {
                    o = false;
                    no = false;
                } else if (boa[i][j] == 'O') {
                    x = false;
                    no = false;
                } else if (boa[i][j] == '.') {
                    x = false;
                    o = false;
                }
            }
            if (x || o) {
                won = true;
            }
        }
        if (!won) {
            x = true, o = true, no = true;

            for (int i = 0, j = 3; i < 4 && !won; i++, j--) {
                if (boa[i][j] == 'X') {
                    o = false;
                    no = false;
                } else if (boa[i][j] == 'O') {
                    x = false;
                    no = false;
                } else if (boa[i][j] == '.') {
                    x = false;
                    o = false;
                }
            }

            if (x || o) {
                won = true;
            }
        }
        if (x) {
            cout << "Case #" << cs << ": X won" << endl;
        } else if (o) {
            cout << "Case #" << cs << ": O won" << endl;
        } else if (over) {
            cout << "Case #" << cs << ": Draw" << endl;
        } else {
            cout << "Case #" << cs << ": Game has not completed" << endl;
        }
    }

    return 0;
}
