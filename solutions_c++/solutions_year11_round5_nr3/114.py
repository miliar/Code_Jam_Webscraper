#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <deque>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>

using namespace std;

const int dx[] = {0,1,1,1,0,-1,-1,-1};
const int dy[] = {1,1,0,-1,-1,-1,0,1};

const int mod = 1000003;
char re[10][10];
int dd[4][4][2];
int gg[4][4];
int R, C;
int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int ca = 1; ca <= T; ++ca) {
        scanf("%d%d", &R, &C);
        for (int i = 0; i < R; ++i)
            scanf("%s", re[i]);
        int ans = 0;
        for (int i = 0; i < R; ++i)
            for (int j = 0; j < C; ++j) {
                if (re[i][j] == '-') {
                    dd[i][j][0] = 0;
                    dd[i][j][1] = 4;
                } else if (re[i][j] == '|') {
                    dd[i][j][0] = 2;
                    dd[i][j][1] = 6;
                } else if (re[i][j] == '/') {
                    dd[i][j][0] = 3;
                    dd[i][j][1] = 7;
                } else {
                    dd[i][j][0] = 1;
                    dd[i][j][1] = 5;
                }
            }
        int m = R * C;
        for (int i = 0; i < (1 << m); ++i) {
            for (int j = 0; j < m; ++j) {
                int x = j / C, y = j % C;
                if (i & (1 << j)) {
                    gg[x][y] = dd[x][y][1];
                } else {
                    gg[x][y] = dd[x][y][0];
                }
            }
            bool have = false;
            for (int a = 0; a < R && !have; ++a)
                for (int b = 0; b < C && !have; ++b) {
                    int c = 0;
                    for (int k = 0; k < 8; ++k) {
                        int x = (R + a + dx[k]) % R, y = (C + b + dy[k]) % C;
                        int nx = (R + x + dx[gg[x][y]]) % R, ny = (C + y + dy[gg[x][y]]) % C;
                        if (nx == a && ny == b) {
                            c++;
                            if (c > 1) break;
                        }
                    }
                    if (c > 1) have = true;
                }
            if (!have) ans++;
        }
        printf("Case #%d: %d\n", ca, ans % mod);
    }
    return 0;
}
