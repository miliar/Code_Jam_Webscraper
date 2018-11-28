#include <iostream>
using namespace std;

#define N 100

const int ix[] = {-1, 0, 0, 1};
const int iy[] = {0, -1, 1, 0};

int n, m;
int a[N][N];
char cn, s[N][N];

void dfs(int i, int j)
{
    int x, y, mx, my, k;
    mx = my = -1;
    for (k = 0; k < 4; ++k)
    {
        x = i + ix[k];
        y = j + iy[k];
        if (x >= 0 && x < n && y >= 0 && y < m && a[i][j] > a[x][y])
            if (mx == -1 || a[x][y] < a[mx][my])
            { mx = x; my = y; }
    }
    if (mx == -1)
        s[i][j] = cn++;
    else
    {
        if (s[mx][my] == ' ')
            dfs(mx, my);
        s[i][j] = s[mx][my];
    }
}

int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);
    int t, cas;
    scanf("%d", &cas);
    for (t = 1; t <= cas; ++t)
    {
        int i, j;
        scanf("%d %d", &n, &m);
        for (i = 0; i < n; ++i)
            for (j = 0; j < m; ++j)
                scanf("%d", &a[i][j]);
        cn = 'a';
        for (i = 0; i < n; ++i)
            for (j = 0; j < m; ++j)
                s[i][j] = ' ';
        for (i = 0; i < n; ++i)
            for (j = 0; j < m; ++j)
                if (s[i][j] == ' ')
                    dfs(i, j);
        printf("Case #%d:\n", t);
        for (i = 0; i < n; ++i)
        {
            for (j = 0; j < m-1; ++j)
                printf("%c ", s[i][j]);
            printf("%c\n", s[i][m-1]);
        }
    }
    return 0;
}
