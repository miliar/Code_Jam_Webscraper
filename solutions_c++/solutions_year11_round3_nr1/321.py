#include <iostream>
#include <iterator>
#include <vector>
using namespace std;

int R, C;

inline bool fix(vector<string> &g, int r, int c) {
    if (r < R-1 && c < C-1 && g[r][c+1] == '#' && g[r+1][c] == '#' &&
        g[r+1][c+1] == '#') {

        g[r][c]   = '/';  g[r][c+1]   = '\\';
        g[r+1][c] = '\\'; g[r+1][c+1] = '/';

        return true;
    }
    return false;
}

void solve(vector<string> &g) {
    bool ok = true;
    for (int i = 0; i < R; ++i) {
        for (int j = 0; j < C; ++j)
            if (g[i][j] == '#' && !fix(g, i, j)) {
                ok = false; break;
            }

        if (!ok) break;
    }

    if (!ok)
        cout << "Impossible" << endl;
    else
        copy(g.begin(), g.end(), ostream_iterator<string>(cout, "\n"));
}

int main() {
    int T;
    cin >> T;

    for (int i = 0; i < T; ++i) {
        vector<string> tiles;

        cin >> R >> C;
        for (int j = 0; j < R; ++j) {
            string s; cin >> s;
            tiles.push_back(s);
        }

        cout << "Case #" << i+1 << ":\n";
        solve(tiles);
    }

    return 0;
}
