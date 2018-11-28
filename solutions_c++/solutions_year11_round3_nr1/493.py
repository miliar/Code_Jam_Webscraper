// A CZM1.0
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<cstring>
#include<vector>
#include<stack>
#include<queue>
#include<algorithm>
using namespace std;

#define PI acos(-1.0)
#define eps 1e-5
#define oo 0x3f3f3f3f
const static int maxN = 50;
typedef long long INT64;

char grid[maxN][maxN+1];

int dir[4][2] = {0,0, 0,1, 1,0, 1,1};

bool change(int& R, int& C, int x, int y)
{
    int i;
    int tx, ty;
    for (i = 0; i < 4; i++)
    {
        tx = x + dir[i][0];
        ty = y + dir[i][1];
        if (tx >= 0 && tx < R && ty >= 0 && ty < C && grid[tx][ty] == '#')
        {
        }
        else
        {
            return false;
        }
    }
    for (i = 0; i < 4; i++)
    {
        tx = x + dir[i][0];
        ty = y + dir[i][1];
        grid[tx][ty] = (i == 0 || i == 3 ? '/' : '\\');
    }
    return true;
}

bool Can(int& R, int& C)
{
    int i, j, k;
    for (i = 0; i < R; i++)
    {
        for (j = 0; j < C; j++)
        {
            if (grid[i][j] == '#')
            {
                if (change(R, C, i, j))
                {
                }
                else
                {
                    return false;
                }
            }
        }
    }
    return true;
}

int main()
{
    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);
    int T;
    int cas = 1;
    int R, C;
    int i;
    scanf("%d", &T);
    while (T--)
    {
        scanf("%d%d", &R, &C);
        for (i = 0; i < R; i++)
        {
            scanf("%s", grid[i]);
        }
        printf("Case #%d:\n", cas++);
        if (Can(R, C))
        {
            for (i = 0; i < R; i++)
            {
                printf("%s\n", grid[i]);
            }
        }
        else
        {
            printf("Impossible\n");
        }
    }
    return 0;
}
