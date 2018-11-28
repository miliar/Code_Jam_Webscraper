#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <vector>
#include <utility>
using namespace std;

const int dir[4][2] = { { -1, 0 }, { 0, -1 }, { 0, 1 }, { 1, 0 } };
const int opdir[4] = { 3, 2, 1, 0 };
const int inf = 1000000000;
const int maxn = 128;
const int maxm = 128;
int cases, cas = 1, n, m;
int board[maxn][maxm], mark[maxn][maxm], path[maxn][maxm];
vector<pair<pair<int, int>, int> > pos;

bool isSinkOrFlow(int x, int y) {
    bool ok = true;
    int best = inf, bestdir = -1;
    for (int k = 0; k < 4; ++k) {
        int xx = x + dir[k][0], yy = y + dir[k][1];
        if (xx >= 0 && xx < n && yy >= 0 && yy < m && board[xx][yy] < board[x][y]) {
            ok = false;
            if (board[xx][yy] < best) {
                best = board[xx][yy];
                bestdir = k;
            }
        }
    }
    path[x][y] = bestdir;
    return ok;
}

void dfs(int x, int y, int num) {
    if (make_pair(x, y) < pos[num].first) {
        pos[num].first = make_pair(x, y);
    }
    mark[x][y] = num;
    for (int k = 0; k < 4; ++k) {
        int xx = x + dir[k][0], yy = y + dir[k][1];
        if (xx >= 0 && xx < n && yy >= 0 && yy < m && mark[xx][yy] < 0 && path[xx][yy] == opdir[k]) {
            dfs(xx, yy, num);
        }
    }
}

int main() {
    for (scanf("%d", &cases); cases--; ) {
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; ++i) for (int j = 0; j < m; ++j) {
            scanf("%d", &board[i][j]);
        }
        vector<pair<int, int> > sinks;
        for (int i = 0; i < n; ++i) for (int j = 0; j < m; ++j) if (isSinkOrFlow(i, j)) {
            sinks.push_back(make_pair(i, j));
        }
        pos.resize(sinks.size());
        for (unsigned i = 0; i < pos.size(); ++i) {
            pos[i] = make_pair(make_pair(maxn, maxm), i);
        }

        memset(mark, 0xff, sizeof(mark));
        for (unsigned i = 0; i < sinks.size(); ++i) {
            dfs(sinks[i].first, sinks[i].second, i);
        }
        sort(pos.begin(), pos.end());
        char name[32];
        for (unsigned i = 0; i < pos.size(); ++i) {
            name[pos[i].second] = i + 'a';
        }

        printf("Case #%d:\n", cas++);
        for (int i = 0; i < n; ++i) {
            printf("%c", name[mark[i][0]]);
            for (int j = 1; j < m; ++j) {
                printf(" %c", name[mark[i][j]]);
            }
            printf("\n");
        }
    }
    return 0;
}
