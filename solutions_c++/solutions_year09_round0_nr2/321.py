#include <cstdio>
#include <cstring>
#include <vector>
using namespace std;

const int MAX = 110;
const int INF = 0x3f3f3f3f;

int T;
int H, W;
int h[MAX][MAX];
vector< pair<int,int> > g[MAX][MAX];
char grid[MAX][MAX];

const int di[] = {-1, 0, 0, 1};
const int dj[] = {0, -1, 1, 0};
#define valid(i,j) (i >= 0 && i < H && j >= 0 && j < W)

void dfs(int i, int j, char ch) {
    if (grid[i][j] != '.') return;
    grid[i][j] = ch;
    for (int k = 0; k < g[i][j].size(); ++k) {
        dfs(g[i][j][k].first, g[i][j][k].second, ch);
    }
}

int main() {

    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        scanf("%d %d", &H, &W);
        for (int i = 0; i < H; ++i) {
            for (int j = 0; j < W; ++j) {
                scanf("%d", &h[i][j]);
                g[i][j].clear();
                grid[i][j] = '.';
            }
        }

        for (int i = 0; i < H; ++i) {
            for (int j = 0; j < W; ++j) {
                int vi = -1, vj = -1, vh = h[i][j];
                for (int d = 0; d < 4; ++d) {
                    int ii = i + di[d], jj = j + dj[d];
                    if (valid(ii,jj)) {
                        if (vh > h[ii][jj]) {
                            vi = ii;
                            vj = jj;
                            vh = h[ii][jj];
                        }
                    }
                }
                if (vi != -1) {
                    g[i][j].push_back(make_pair(vi,vj));
                    g[vi][vj].push_back(make_pair(i,j));
                }
            }
        }

        char ch = 'a';
        for (int i = 0; i < H; ++i) {
            for (int j = 0; j < W; ++j) {
                if (grid[i][j] == '.') {
                    dfs(i,j,ch);
                    ++ch;
                }
            }
        }

        printf("Case #%d:\n", t);
        for (int i = 0; i < H; ++i) {
            for (int j = 0; j < W; ++j) {
                if (j > 0) putchar(' ');
                printf("%c", grid[i][j]);
            }
            puts("");
        }
    }

    return 0;
}
