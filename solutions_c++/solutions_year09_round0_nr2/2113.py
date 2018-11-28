#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int map[101][101];
int memo[101][101];
int basins[10002];
int last;
int H, W;

static int moves[4][2] = { {-1, 0} , {0, -1} , {0, 1} , {1, 0} };

int DP(int i, int j) {
   // printf("%d %d\n", i, j);
    if(memo[i][j]!=-1) return memo[i][j];
    pair<int, int> best(1000000, 1000);
    for(int k=0; k<4; ++k) {
        int ni = i + moves[k][0];
        int nj = j + moves[k][1];
        if(ni < 0 || ni >= H) continue;
        if(nj < 0 || nj >= W) continue;
        pair<int, int> cur(map[ni][nj], k);
        best = min(best, cur);
    }
   // printf("b.f = %d, b.s = %d\n", best.first, best.second);
    if(best.first >= map[i][j]) {
        if(basins[i*W + j] == -1)
            basins[i*W + j] = last++;
        memo[i][j] = basins[i*W + j];
    } else {
        memo[i][j] = DP(i + moves[best.second][0], j + moves[best.second][1]);
    }
    return memo[i][j];
}

void answer() {
    memset(memo, -1, sizeof(memo));
    memset(basins, -1, sizeof(basins));
    last = 0;
    for(int i=0; i<H; ++i) {
        for(int j=0; j<W; ++j) {
            DP(i, j);
        }
    }
    for(int i=0; i<H; ++i) {
        for(int j=0; j<W; ++j) {
            printf("%c ", memo[i][j] + 'a');
        }
        printf("\n");
    }
    fflush(stdout);
}

int main() {
    
    #ifndef ONLINE_JUDGE
        freopen("B-large.in", "r", stdin);
        freopen("B-large.out", "w", stdout);
    #endif
    
    int T; scanf("%d", &T);
    for(int ic=0; ic<T; ++ic) {
        scanf("%d %d", &H, &W);
        for(int i=0; i<H; ++i) for(int j=0; j<W; ++j) scanf("%d", &map[i][j]);
        printf("Case #%d:\n", ic+1);
        answer();
    }
    
    return 0;
}
