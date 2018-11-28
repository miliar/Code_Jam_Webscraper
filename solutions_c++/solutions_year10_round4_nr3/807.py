#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <cmath>
#include <cctype>
#define N 101
using namespace std;

typedef pair<int, int>pii;
typedef long long I64;

bool board[N][N];
inline bool legal(int x, int y)
{
    return x > 0 && x < N && y > 0 && y < N && board[x][y];
}
int px[N * N], py[N * N];

int main()
{
    freopen("C-small.in", "r", stdin);
    freopen("C-small.out", "w", stdout);
    int C = 0, T;
    scanf("%d", &T);
    while (T--)
    {
        int R, i, j, k;
        scanf("%d", &R);
        memset(board, false, sizeof(board));
        for (int i = 0; i < R; i++)
        {
            int x1, y1, x2, y2;
            scanf("%d %d %d %d", &y1, &x1, &y2, &x2);
            for (j = x1; j <= x2; j++)
                for (k = y1; k <= y2; k++)
                    board[j][k] = true;
        }
        int res = 0;
        while (true)
        {
            int n = 0;
            for (i = 1; i < N; i++)
            {
                for (j = 1; j < N; j++)
                {
                    int tmp = 0;
                    if (legal(i - 1, j))tmp++;
                    if (legal(i, j - 1))tmp++;
                    if (board[i][j] + tmp >= 2)
                        px[n] = i, py[n++] = j;
                }
            }
            memset(board, false, sizeof(board));
            res++;
            if (!n)break;
            for (i = 0; i < n; i++)
                board[px[i]][py[i]] = true;
        }
        printf("Case #%d: %d\n", ++C, res);
    }
    return 0;
}
