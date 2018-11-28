#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <set>
#include <deque>
#include <queue>

using namespace std;

const int N = 10;

char dp[N][N][1 << N][1 << N];
int a[N+3];
int rows, cols;

int go(int r, int c, int mask1, int mask2) {
    //cout << "go " << r << " " << c << " " << mask1 << " " << mask2 << endl;
    if (r == rows) return 0;
    if (c >= cols) return go(r+1, 0, mask2, a[r+2]);
    if (dp[r][c][mask1][mask2] >= 0) return dp[r][c][mask1][mask2];
    int best = go(r, c+1, mask1, mask2);
    if ((mask1 & (1 << c)) == 0) return dp[r][c][mask1][mask2] = best;
    int nextMask1 = mask1 & (~(1 << (c+1)));
    int nextMask2 = mask2 & (~(1 << (c+1)));
    if (c > 0) nextMask2 = nextMask2 & (~(1 << (c-1)));
    best >?= 1+go(r, c+2, nextMask1, nextMask2);
    return dp[r][c][mask1][mask2] = best;
}

int process() {
    memset(dp, 0xff, sizeof(dp));
    cin >> rows >> cols;
    for (int i = rows-1; i >= 0; i--) {
        string s;
        cin >> s;
        int res = 0;
        for (int j = 0, m = 1; j < cols; j++, m <<= 1) {
            if (s[j] == '.') res |= m;
        }
        a[i] = res;
    }

    return go(0, 0, a[0], a[1]);
}

int main() {
    int cases; cin >> cases;
    for (int t = 1; t <= cases; t++) {
        cout << "Case #" << t << ": " << process() << endl;
    }
    return 0;
}

