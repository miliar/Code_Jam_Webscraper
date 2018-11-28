#include <iostream>
#include <iomanip>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <string>
#include <cstring>
#include <sstream>
#include <cmath>
#include <algorithm>
#include <ctime>
#include <cassert>
#include <functional>
#include <iterator>
#include <complex>

using namespace std;
typedef long double LD;
typedef long long LL;
typedef unsigned long long ULL;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    int nTests;
    cin >> nTests;

    const int N = 4;
    char a[N][N];
    const char s[2] = {'X', 'O'};

    for (int test = 0; test < nTests; ++test) {
        cerr << test << '\n';
        bool hasDot = false;
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < N; ++j) {
                cin >> a[i][j];
                if (a[i][j] == '.') {
                    hasDot = true;
                }
            }
        }
        bool won[2] = {};

        for (int c = 0; c < 2; ++c) {
            bool ok;

            for (int i = 0; i < N; ++i) {
                ok = true;
                for (int j = 0; j < N; ++j) {
                    if (!(a[i][j] == s[c] || a[i][j] == 'T')) {
                        ok = false;
                    }
                }
                won[c] |= ok;
            }

            for (int j = 0; j < N; ++j) {
                ok = true;
                for (int i = 0; i < N; ++i) {
                    if (!(a[i][j] == s[c] || a[i][j] == 'T')) {
                        ok = false;
                    }
                }
                won[c] |= ok;
            }

            ok = true;
            for (int i = 0; i < N; ++i) {
                if (!(a[i][i] == s[c] || a[i][i] == 'T')) {
                    ok = false;
                }
            }
            won[c] |= ok;

            ok = true;
            for (int i = 0; i < N; ++i) {
                if (!(a[i][N - 1 - i] == s[c] || a[i][N - 1 - i] == 'T')) {
                    ok = false;
                }
            }
            won[c] |= ok;
        }

        cout << "Case #" << test + 1 << ": ";
        assert(!(won[0] && won[1]));
        if (won[0]) {
            cout << s[0] << " won";
        } else if (won[1]) {
            cout << s[1] << " won";
        } else if (!hasDot) {
            cout << "Draw";
        } else {
            cout << "Game has not completed";
        }
        cout << '\n';
    }

    return 0;
}