#include <stdio.h>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

#define MAX_W   (200)
#define MAX_H   (200)

int ways[MAX_H][MAX_W];
bool hasrock[MAX_H][MAX_W];
int W, H;

int main() {
    int NTc;
    scanf("%d", &NTc);
    int i, j, k, m, n;
    for (int tc = 0; tc < NTc; tc++) {
        printf("Case #%d: ", tc+1);
        memset(ways, 0, sizeof(ways));
        memset(hasrock, 0, sizeof(hasrock));
        scanf("%d %d %d", &H, &W, &j);
        for (i = 0; i < j; i++) {
            scanf("%d %d", &m, &n);
            hasrock[m-1][n-1] = true;
        }
        if (!hasrock[0][0]) ways[0][0] = 1;
        for (i = 0; i < H; i++) {
            for (j = 0; j < W; j++) {
                if (hasrock[i][j]) continue;
                if (i >= 2 && j >= 1) ways[i][j] += ways[i-2][j-1];
                if (i >= 1 && j >= 2) ways[i][j] += ways[i-1][j-2];
                ways[i][j] = ways[i][j] % 10007;
                
            }
        }
        printf("%d\n", ways[H-1][W-1]);
    }
    return 0;
}
