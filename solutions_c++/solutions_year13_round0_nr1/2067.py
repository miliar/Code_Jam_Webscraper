#include <cassert>
#include <cstdio>
#include <cstring>
#include <functional>
#include <initializer_list>
#include <string>
#include <vector>

using namespace std;

#define forn(i, n) for (int i = 0; i < (n); i++)

const int n = 4;
char a[n+2][n+2];

string go() {
    int xs = 0, os = 0, ts = 0;
    forn(i, n) forn(j, n) xs += (a[i][j] == 'X'), os += (a[i][j] == 'O'), ts += (a[i][j] == 'T');

    assert(0 <= ts && ts <= 1);
    assert(xs-1 <= os && os <= xs);
    assert(xs + os + ts <= n*n);

    forn(i, n) {
        auto fs = vector<function<char(int)>> {
            [i](int j) { return a[i][j]; },
            [i](int j) { return a[j][i]; },
            [](int j) { return a[j][j]; },
            [](int j) { return a[j][n-1-j]; }
        };

        for (auto c : {'X', 'O'}) {
            for (auto f : fs) {
                bool all = true;
                forn(j, n) all &= (f(j) == c || f(j) == 'T');
                if (all) return string("") + c + " won";
            }
        }
    }

    return xs + os + ts == n*n ? "Draw" : "Game has not completed";
}

int main() {
    int __;
    scanf("%d", &__);
    forn(_, __) {
        forn(i, n) scanf("%s", a[i]);
        string ans = go();
        printf("Case #%d: %s\n", _+1, ans.c_str());
    }
    return 0;
}

