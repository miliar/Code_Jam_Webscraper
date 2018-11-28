#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <set>
#include <string>

using namespace std;

const int maxn = 128;
char g[maxn][maxn];
const int dir[8][2] = {
    -1, 0, 1, 0, 0, 1, 0, -1,
    -1, -1, 1, -1, 1, 1, -1, 1
};

bool isvalid(int x, int y) {
    return x >= 0 && y >= 0 && x < 4 && y < 4;
}

void solved(int nT) {
    for (int i = 0; i < 4; ++i) {
        scanf("%s", g[i]);
    }
    int cnt0 = 0;
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            if (g[i][j] == '.') ++cnt0;
        }
    }
    printf("Case #%d: ", nT);
    for (int i = 0; i < 4; ++i) {
        for (int j = 0; j < 4; ++j) {
            if (g[i][j] == 'X' || g[i][j] == 'O') {
                
                for (int k = 0; k < 8; ++k) {
                    int tx = i, ty = j;
                    int cnt = 0, cnt1 = 0;
                    while (isvalid(tx, ty) && (g[tx][ty] == g[i][j] || g[tx][ty] == 'T')) {
                        if (g[tx][ty] == 'T') ++cnt1;
                        else ++cnt;
                        tx += dir[k][0];
                        ty += dir[k][1];
                    }
                    if (cnt == 4 || (cnt == 3 && cnt1 == 1)) {
                        printf("%c won\n", g[i][j]); return;
                    }
                }
            }
        }
    }
    if (cnt0) {
        puts("Game has not completed");
    } else {
        puts("Draw");
    }
}

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T = 1;
    scanf("%d", &T);
    for (int nT = 1; nT <= T; ++nT) {
        solved(nT);
    }
    return 0;
}