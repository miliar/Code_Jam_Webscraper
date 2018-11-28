#include <cstdio>
#include <cassert>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <map>
#include <algorithm>
#include <vector>

#if 0
#define D(x...) fprintf(stderr, x)
#else
#define D(x...)
#endif

using namespace std;

typedef long long ll;

int solve() {
    int R;
    scanf("%d", &R);
    int grid[2][110][110];
    memset(grid, 0, sizeof(grid));
    int num_bact = 0;
    int minx = -1;
    int miny = -1;
    int maxx = -1;
    int maxy = -1;
    for (int i = 0; i < R; i++) {
        int x1, y1, x2, y2;
        scanf("%d%d%d%d\n", &x1, &y1, &x2, &y2);
        for (int x = x1; x <= x2; x++) {
            for (int y = y1; y <= y2; y++) {
                if (grid[0][x][y] == 0) {
                    grid[0][x][y] = 1;
                    num_bact++;
                    if (minx == -1 || x < minx) {
                        minx = x;
                    }
                    if (maxx == -1 || x > maxx) {
                        maxx = x;
                    }
                    if (miny == -1 || y < miny) {
                        miny = y;
                    }
                    if (maxy == -1 || y > maxy) {
                        maxy = y;
                    }
                }
            }
        }
    }

    int days = 0;
    int cur_grid = 0;
    while (num_bact > 0) {
        for (int x = minx; x <= maxx; x++) {
            for (int y = miny; y <= maxy; y++) {
                if (grid[cur_grid][x-1][y] && grid[cur_grid][x][y-1]) {
                    if (grid[cur_grid][x][y] == 0) {
                        num_bact++;
                    }
                    grid[cur_grid^1][x][y] = 1;
                } else if (!grid[cur_grid][x-1][y] && !grid[cur_grid][x][y-1]) {
                    if (grid[cur_grid][x][y] != 0) {
                        num_bact--;
                    }
                    grid[cur_grid^1][x][y] = 0;
                } else {
                    grid[cur_grid^1][x][y] = grid[cur_grid][x][y];
                }
            }
        }
        cur_grid ^= 1;
        days++;
#if 0
        for (int r = 1; r < 8; r++) {
            for (int c = 1; c < 8; c++) {
                printf("%d", grid[cur_grid][c][r]);
            }
            printf("\n");
        }
        printf("\n");
#endif
    }
    return days;
}

int main() {
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; i++) {
        printf("Case #%d: %d\n", i, solve());
    }
    return 0;
}
