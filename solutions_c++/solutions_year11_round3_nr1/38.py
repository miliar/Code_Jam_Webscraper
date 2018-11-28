
#include <cstdio>
#include <cstring>
#include <algorithm>

#define For(i, a, b) for (int i = a; i < b; i++)

int T;

int R, C;
char grid[51][51];


static void solve(int t)
{
    scanf("%d %d", &R, &C);
    memset(grid, 0, sizeof(grid));

    For(i, 0, R) {
        scanf("\n");
        For (j, 0, C) {
            grid[i][j] = getchar();
        }
    }

    For(i, 0, R) {
        For (j, 0, C) {
            if (grid[i][j] != '#')
                continue;
            if (grid[i][j+1] != '#' || grid[i+1][j] != '#' || grid[i+1][j+1] != '#')
                goto imposs;
            grid[i][j] = '/';
            grid[i][j+1] = '\\';
            grid[i+1][j] = '\\';
            grid[i+1][j+1] = '/';
        }
    }

    printf("Case #%d:\n", t);
    For(i, 0, R) {
        For (j, 0, C) {
            printf("%c", grid[i][j]);
        }
        printf("\n");
    }
    return;

imposs:
    printf("Case #%d:\nImpossible\n", t);
}

int main()
{
    scanf("%d", &T);

    For(t, 0, T)
        solve(t+1);

    return 0;
}

