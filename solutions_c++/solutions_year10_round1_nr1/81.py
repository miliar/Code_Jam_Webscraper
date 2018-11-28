#include <cstdio>
#include <string>
#include <iostream>

using namespace std;

int cN, cT, i, j, n, k, pos;
bool red, blue;
string s, board[60], newBoard[60];
int mx[8] = {1, 1, 0, -1, -1, -1, 0, 1};
int my[8] = {0, 1, 1, 1, 0, -1, -1, -1};

inline bool ok(int x, int y) {
    return (0<=x && x<n && 0<=y && y<n);
}

bool check(char color) {
    int i, j, x, y, d, cnt;
    for (i = 0; i < n; ++i)
    for (j = 0; j < n; ++j) if (newBoard[i][j] == color) {
        color = newBoard[i][j];
        for (d = 0; d < 8; ++d) {
            x = i; y = j;
            cnt = 1;
            while (newBoard[x][y] == color) {
                if (ok(x+mx[d], y+my[d])) {
                    x+=mx[d]; y+=my[d];
                }
                else break;
                if (newBoard[x][y] == color) ++cnt;
            }
            if (cnt >= k) return true;
        }
    }
    return false;
}

int main() {
    cin >> cN;
    for (cT = 1; cT <= cN; ++cT) {
        cin >> n >> k;
        for (i = 0; i < n; ++i) cin >> board[i];
        s = "";
        for (i = 0; i < n; ++i) s += ".";
        for (i = 0; i < n; ++i) newBoard[i] = s;
        for (i = 0; i < n; ++i) {
            pos = n-1;
            for (j = n-1; j >= 0; j--) if (board[i][j] != '.') {
                newBoard[i][pos--] = board[i][j];
            }
        }
        red = check('R');
        blue = check('B');
        printf("Case #%d: ", cT);
        if (!red && !blue) puts("Neither");
        if (red && !blue) puts("Red");
        if (!red && blue) puts("Blue");
        if (red && blue) puts("Both");
    }
}
