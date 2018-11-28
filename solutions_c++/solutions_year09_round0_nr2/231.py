#include <iostream>
#include <sstream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>

using namespace std;

const int dx[] = {-1, 0, 0, 1};
const int dy[] = {0, -1, 1, 0};
int H, W;
int hh[101][101];
char lab[101][101];
bool visit[101][101];
char now;
bool out(int x, int y)
{
    if (x < 0 || x >= H || y < 0 || y >= W) return true;
    return false;
}
char dfs(int x, int y)
{
    if (visit[x][y]) {
        return lab[x][y];
    }
    visit[x][y] = true;
    bool go = false;
    int nx, ny;
    int h = hh[x][y];
    for (int i = 0; i < 4; ++i) {
        int ax = x + dx[i];
        int ay = y + dy[i];
        if (out(ax, ay)) continue;
        if (hh[ax][ay] < h) {
            go = true;
            nx = ax;
            ny = ay;
            h = hh[ax][ay];
        }
    }
    if (go) {
        return lab[x][y] = dfs(nx, ny);
    }
    return lab[x][y] = now++;
}
int main()
{
    //freopen("B-large.in", "r", stdin);
    //freopen("B-large.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        scanf("%d%d", &H, &W);
        for (int i = 0; i < H; ++i)
            for (int j = 0; j < W; ++j)
                scanf("%d", &hh[i][j]);
        now = 'a';
        memset(visit, false, sizeof(visit));
        for (int i = 0; i < H; ++i)
            for (int j = 0; j < W; ++j) {
                if (visit[i][j]) continue;
                lab[i][j] = dfs(i, j);
            }
        printf("Case #%d:\n", t);
        for (int i = 0; i < H; ++i) {
            printf("%c", lab[i][0]);
            for (int j = 1; j < W; ++j) {
                printf(" %c", lab[i][j]);
            }
            printf("\n");
        }
    }
    return 0;
}
