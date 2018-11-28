#include <cstdio>
#include <string>

using namespace std;

int T, H, W;
int mat[128][128];
int basin[128][128], basinCnt;
int dir[4][2] = { {-1, 0}, {0, -1}, {0, 1}, {1, 0} }; 
int basinInd[30];

int GetBasin(int x, int y)
{
    int& ret = basin[x][y];
    if (ret != -1)
        return ret;
    int smallInd = -1;
    int smallVal = 10000000;
    for (int d = 0; d < 4; ++d) {
        int xx = x + dir[d][0];
        int yy = y + dir[d][1];
        if (xx >= 0 && xx < H && yy >= 0 && yy < W && mat[xx][yy] < smallVal) {
            smallInd = d;
            smallVal = mat[xx][yy];
        }
    }
    return ret = GetBasin(x + dir[smallInd][0], y + dir[smallInd][1]);
}

int main()
{
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas) {
        scanf("%d %d", &H, &W);
        for (int i = 0; i < H; ++i) {
            for (int j = 0; j < W; ++j) {
                scanf("%d", &mat[i][j]);
                basin[i][j] = -1;
            }
        }
        basinCnt = 0;
        for (int i = 0; i < H; ++i) {
            for (int j = 0; j < W; ++j) {
                bool hasSmall = false;
                for (int d = 0; d < 4; ++d) {
                    int ii = i + dir[d][0];
                    int jj = j + dir[d][1];
                    if (ii >= 0 && ii < H && jj >= 0 && jj < W && mat[ii][jj] < mat[i][j]) {
                        hasSmall = true;
                        break;
                    }
                }
                if (!hasSmall)
                    basin[i][j] = basinCnt++;
                else 
                    basin[i][j] = -1;
            }
        }
        for (int i = 0; i < H; ++i) {
            for (int j = 0; j < W; ++j) if (basin[i][j] == -1) {
                basin[i][j] = GetBasin(i, j);
            }
        }
        basinCnt = 0;
        memset(basinInd, -1, sizeof(basinInd));
        printf("Case #%d:\n", cas);
        for (int i = 0; i < H; ++i) {
            for (int j = 0; j < W; ++j) {
                if (basinInd[ basin[i][j] ] == -1)
                    basinInd[ basin[i][j] ] = basinCnt++;
                putchar('a' + basinInd[ basin[i][j] ]);
                if (j == W-1)
                    puts("");
                else 
                    putchar(' ');
            }
        }
    }
    return 0;
}

