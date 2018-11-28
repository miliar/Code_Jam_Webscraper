#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>

using namespace std;

const int dx[] = {-1, 1, 0, 0, -1, 1, -1, 1};
const int dy[] = {0, 0, -1, 1, -1, -1, 1, 1};

char board[55][55];
char tmp[55][55];
int n, K;

bool out(int x, int y)
{
    if (x < 0 || x >= n || y < 0 || y >= n) return true;
    return false;
}
bool check(char re[][55], char col)
{
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < n; ++j) {
            if (re[i][j] != col) continue;
            for (int k = 0; k < 8; ++k) {
                int x = i, y = j;
                int cnt = 0;
                for (;;) {
                    if (out(x, y) || re[x][y] != col) break;
                    cnt++;
                    x = x + dx[k];
                    y = y + dy[k];
                }
                if (cnt >= K) return true;
            }
        }
    }
    return false;
}
void rol(char so[][55], char re[][55])
{
    for (int i = 0; i < n; ++i)
        for (int j = 0; j < n; ++j) {
            re[i][j] = so[n - j - 1][i];
        }
    for (int j = 0; j < n; ++j) {
        bool have = false;
        for (int i = 0; i < n - 1; ++i)
            if (re[i][j] != '.' && re[i + 1][j] == '.') {
                have = true;
                break;
            }
        if (!have) continue;
        for (int i = n - 2; i >= 0; --i) {
            if (re[i][j] != '.' && re[i + 1][j] == '.') {
                for (int k = i; k <= n - 2 && re[k][j] != '.' && re[k + 1][j] == '.'; ++k)
                    swap(re[k][j], re[k + 1][j]);
            }
        }
    }
}
int main()
{
    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ++ca) {
        scanf("%d%d", &n, &K);
        for (int i = 0; i < n; ++i)
            scanf("%s", tmp[i]);
        rol(tmp, board);
        bool rr = check(board, 'R');
        bool bb = check(board, 'B');
        if (rr && bb) {
            printf("Case #%d: Both\n", ca);
        } else if (rr) {
            printf("Case #%d: Red\n", ca);
        } else if (bb) {
            printf("Case #%d: Blue\n", ca);
        } else {
            printf("Case #%d: Neither\n", ca);
        }
    }

    return 0;
}
