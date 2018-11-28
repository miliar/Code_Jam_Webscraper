#include <cstdio>
#include <string>
using namespace std;

#define forn(i, n) for (int i=0; i<(n); ++i)

char a[10][10];

bool check(char c) {
    forn (i, 4) {
        int cnt = 0;
        forn (j, 4)
            cnt += a[i][j] == c || a[i][j] == 'T';
        if (cnt == 4) return true;
        cnt = 0;
        forn (j, 4)
            cnt += a[j][i] == c || a[j][i] == 'T';
        if (cnt == 4) return true;
    }
    int cnt = 0;
    forn (i, 4)
        cnt += a[i][i] == c || a[i][i] == 'T';
    if (cnt == 4) return true;
    cnt = 0;
    forn (i, 4)
        cnt += a[i][3-i] == c || a[i][3-i] == 'T';
    if (cnt == 4) return true;
    return false;
}

string solve() {
    if (check('X')) return "X won";
    if (check('O')) return "O won";
    forn (i, 4) forn (j, 4)
        if (a[i][j] == '.')
            return "Game has not completed";
    return "Draw";
}

int main() {
    int tc; scanf("%d", &tc);
    for (int tt = 1; tt <= tc; ++tt) {
        gets(a[0]);
        for (int i=0; i<4; ++i)
            gets(a[i]);
        printf("Case #%d: %s\n", tt, solve().c_str());

    }
    return 0;
}
