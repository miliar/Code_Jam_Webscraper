#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <set>
#include <deque>
#include <queue>

using namespace std;

const int N = 100;

int a[N][N];
int H, W, R;

int dy[] = { 1, 2 };
int dx[] = { 2, 1 };

int go(int r, int c) {
    if (r == H && c == W) return 1;
    if (r < 0 || r >= H || c < 0 || c >= W) return 0;
    if (a[r][c] >= 0) return a[r][c];
    int ways = 0;
    for (int i = 0; i < 2; i++) {
        ways += go(r + dy[i], c + dx[i]);
        ways %= 10007;
    }
    return a[r][c] = ways;
}

int process() {
    memset(a, 0xff, sizeof(a));
    cin >> H >> W >> R; H--; W--;
    for (int i = 0; i < R; i++) {
        int r, c; cin >> r >> c; r--; c--;
        a[r][c] = 0;
    }
    return go(0, 0);
}

int main() {
    int cases; cin >> cases;
    for (int t = 1; t <= cases; t++) {
        cout << "Case #" << t << ": " << process() << endl;
    }
    return 0;
}

