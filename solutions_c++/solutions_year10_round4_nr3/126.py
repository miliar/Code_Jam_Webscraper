#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int grid[128][128];

int main()
{
    int T;
    scanf("%d", &T);

    for(int t = 1; t <= T; t++)
    {
        printf("Case #%d: ", t);

        int R;
        scanf("%d", &R);

        memset(grid, 0, sizeof(grid));

        int size = 0;
        for(int i = 0; i < R; i++)
        {
            int x1, y1, x2, y2;
            scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
            size = max(size, max(x2, y2));

            for(int x = x1; x <= x2; x++)
                for(int y = y1; y <= y2; y++)
                    grid[x][y] = 1;
        }

        int ans = 0;

        while(size)
        {
            int tmp[128][128] = {};
            int nsize = 0;

            for(int i = 1; i <= size; i++)
                for(int j = 1; j <= size; j++)
                    if(grid[i][j])
                    {
                        if(!grid[i - 1][j] && !grid[i][j - 1])
                            tmp[i][j] = 0;
                        else
                            tmp[i][j] = 1, nsize = max(nsize, max(i, j));
                    }
                    else
                    {
                        if(grid[i - 1][j] && grid[i][j - 1])
                            tmp[i][j] = 1, nsize = max(nsize, max(i, j));
                        else
                            tmp[i][j] = 0;
                    }
            memcpy(grid, tmp, sizeof(grid));

            size = nsize;
            ans++;
        }

        printf("%d\n", ans);

    }
    return 0;
}
