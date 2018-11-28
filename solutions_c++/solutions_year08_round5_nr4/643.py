#include <iostream>
#include <algorithm>
#include <string>
#include <map>
#include <vector>
#include <cmath>
#define DEBUG(x) std::cerr << #x << " = " << x << '\n';
typedef long long int64;
int N, H, W, R;
bool rock[110][110];
int64 grid[110][110];

int main() {
    scanf("%d", &N);
    for (int n=1; n<=N; n++) {
        scanf("%d%d%d", &H, &W, &R);
        memset(rock, 0, sizeof(rock));
        for (int i=0; i<R; i++) {
            int y, x;
            scanf("%d%d", &y, &x);
            rock[y-1][x-1] = true;
        }
        memset(grid, 0, sizeof(grid));
        grid[0][0] = 1;
        for (int y=0; y<H; y++)
        for (int x=0; x<W; x++) {
            if (!grid[y][x] || rock[y][x]) continue;
            grid[y+2][x+1] += grid[y][x];
            grid[y+1][x+2] += grid[y][x];
        }
        printf("Case #%d: %d\n", n, grid[H-1][W-1] % 10007);
    }
}
