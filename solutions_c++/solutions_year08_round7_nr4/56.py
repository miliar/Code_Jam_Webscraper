#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <utility>

using namespace std;

string a[16];
int rows, cols;
int dx[] = { -1, 0, 1, 1, 1, 0, -1, -1 };
int dy[] = { -1, -1, -1, 0, 1, 1, 1, 0 };

bool known[4][4][65536];
bool dp[4][4][65536];

inline int m(int i, int j) {
    int idx = i * cols + j;
    return 1 << idx;
}

bool go(int r, int c, int state) {
    if (known[r][c][state]) return dp[r][c][state];
    known[r][c][state] = true;
    for (int i = 0; i < 8; i++) {
        int rr = r + dy[i], cc = c + dx[i];
        if (rr < 0 || rr >= rows || cc < 0 || cc >= cols) continue;
        if (a[rr][cc] == '#') continue;
        if (state & m(rr, cc)) continue;

        if (!go(rr, cc, state | m(rr, cc))) return dp[r][c][state] = true;
    }
    return dp[r][c][state] = false;
}

int main() {
    int cases; cin >> cases;
    for (int t = 1; t <= cases; t++) {
        memset(known, false, sizeof(known));
        cin >> rows >> cols;
        for (int i = 0; i < rows; i++) cin >> a[i];

        int kr, kc;
        for (int i = 0; i < rows; i++) for (int j = 0; j < cols; j++) if (a[i][j] == 'K') { kr = i; kc = j; }

        int res = go(kr, kc, m(kr, kc));

        cout << "Case #" << t << ": " << (res ? "A" : "B") << endl;
    }
    return 0;
}

