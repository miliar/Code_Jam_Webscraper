#include <iostream>
#include <cmath>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <cctype>
#include <cstdlib>
#include <cstdio>
#include <cstring>
using namespace std;
#define size(c) (int)c.size()

typedef map<string, int> msi;

int C, R, X1, X2, Y1, Y2;
bool bact[128][128], cpbact[128][128];
int dx[] = {0, -1};
int dy[] = {-1, 0};
bool valid(int x, int y) {
    return x >= 0 && x < 128 && y >= 0 && y < 128;
}
void next() {
    for (int row = 0; row < 128; ++ row)
        for (int col = 0; col < 128; ++ col)
            cpbact[row][col] = bact[row][col];
    for (int row = 0; row < 128; ++ row)
        for (int col = 0; col < 128; ++ col) {
            if (cpbact[row][col]) {
                bool ok = false;
                for (int dir = 0; dir < 2; ++ dir) {
                    int nx = row + dx[dir];
                    int ny = col + dy[dir];
                    if (valid(nx, ny) && cpbact[nx][ny]) ok = true;
                }
                if (!ok) bact[row][col] = false;
            } else {
                bool ok = true;
                for (int dir = 0; dir < 2; ++ dir) {
                    int nx = row + dx[dir];
                    int ny = col + dy[dir];
                    if (!valid(nx, ny) || !cpbact[nx][ny]) ok = false;
                }
                if (ok) bact[row][col] = true;
            }
        }
}
bool end() {
    for (int row = 0; row < 128; ++ row)
        for (int col = 0; col < 128; ++ col)
            if (bact[row][col]) return false;
    return true;
}
int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    scanf("%d", &C);
    for (int t = 1; t <= C; ++t ) {
        scanf("%d", &R);
        for (int i = 0; i < 128; ++ i)
            for (int j = 0; j < 128; ++ j)
                bact[i][j] = false;
        for (int i = 0; i < R; ++ i) {
            scanf("%d%d%d%d", &X1, &Y1, &X2, &Y2);
            for (int row = X1; row <= X2; ++ row)
                for (int col = Y1; col <= Y2; ++ col)
                    bact[row][col] = true;
        }
        int ans = 0;
        while(!end()) {
            next();
            ++ ans;
        }
        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}
