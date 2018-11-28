#include <iostream>
#include <vector>

using namespace std;

int R, C;
char    mat[60][60];

void
solve() {
    int     r, c;

    for (r=0;r<R;++r) {
        for (c=0;c<C;++c) {
            if (mat[r][c] == '#') {
                if ((c == C-1)
                ||  (r == R-1)
                ||  (mat[r][c+1] != '#')
                ||  (mat[r+1][c] != '#')
                ||  (mat[r+1][c+1] != '#'))
                {
                    cout << "Impossible" << endl;
                    return;
                }

                mat[r][c] = '/';
                mat[r][c+1] = '\\';
                mat[r+1][c] = '\\';
                mat[r+1][c+1] = '/';
            }
        }
    }

    for (r=0;r<R;++r)
            cout << mat[r] << endl;
}

int main() {
    int     T, i, j;

    cin >> T;
    for (i=0;i<T;++i) {
        cin >> R >> C;
        for (j=0;j<R;++j) cin >> mat[j];
        cout << "Case #" << (i+1) << ":" << endl;
        solve();
    }
    return 0;
}
