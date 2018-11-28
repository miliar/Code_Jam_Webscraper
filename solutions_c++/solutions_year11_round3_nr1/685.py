#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

int T, tc;

char a[100][100];
int r, c;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    cin >> T;
    int i, j;
    bool imp;
    for (tc = 1; tc <= T; tc++) {
        memset(a, 0, sizeof(a));
        cin >> r >> c;
        for (i = 0; i < r; i++) cin >> a[i];
        imp = false;
        for (i = 0; i < r; i++) {
            for (j = 0; j < c; j++) {
                if (a[i][j] == '#') {
                    if (a[i][j + 1] == '#'
                     && a[i + 1][j] == '#'
                     && a[i + 1][j + 1] == '#') {
                        a[i][j] = a[i + 1][j + 1] = '/';
                        a[i][j + 1] = a[i + 1][j] = '\\';
                    } else {
                        imp = true;
                        break;
                    }
                }
            }
        }
        cout << "Case #" << tc << ":" << endl;
        if (imp) {
            cout << "Impossible" << endl;
        } else {
            for (i = 0; i < r; i++) cout << a[i] << endl;
        }
    }
    return 0;
}
