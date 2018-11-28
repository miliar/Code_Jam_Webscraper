
#include <cstdio>
#include <cstring>

#define For(i, a, b) for (int i = a; i < b; i++)

int T;
int grid[2][300][300];

static void solve(int t)
{
    int R;
    scanf("%d", &R);

    memset(grid, 0, sizeof(grid));
    int alive = 0;

    For(i, 0, R)
    {
        int x1, y1, x2, y2;
        scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
        For(x, x1, x2+1)
        For(y, y1, y2+1)
        {
            grid[0][x][y] = 1;
//            printf("(%d,%d)\n", x, y);
        }
        alive = 1;
    }

    int time;
    for (time = 0; alive; time++)
    {
        alive = 0;
        int now = time%2;
        int next = !now;

//        For(y, 0, 10)
//        {
//            For(x, 0, 10)
//                printf("%d", grid[now][x][y]);
//            printf("\n");
//        }
//        printf("\n");

        For(x, 0, 300)
            grid[next][x][0] = grid[next][0][x] = 0;
        For(x, 0, 300)
        For(y, 0, 300)
        {
            if (grid[now][x][y])
                grid[next][x][y] = (grid[now][x-1][y] || grid[now][x][y-1]);
            else
                grid[next][x][y] = (grid[now][x-1][y] && grid[now][x][y-1]);
            if (grid[next][x][y])
                alive = 1;
        }
    }

    printf("Case #%d: %d\n", t, time);
}

int main()
{
    scanf("%d", &T);

    For(t, 0, T)
        solve(t+1);

    return 0;
}

