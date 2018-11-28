#include <stdio.h>
#include <memory.h>

int n, m;

bool ok(int x, int y)
{
    return 0 <= x && x < n && 0 <= y && y < m;
}

int a[128][128];
int c[128][128];
char e[32][2];

int dx[4] = {-1, 0, 0, 1};
int dy[4] = {0, -1, 1, 0};

int b;

int dfs(int x, int y)
{
    if (c[x][y])
        return c[x][y];
    
    int k = -1;

    for (int d=0; d<4; d++)
        if (ok(x+dx[d], y+dy[d]) && (k == -1 || a[x+dx[d]][y+dy[d]] < a[x+dx[k]][y+dy[k]]))
            k = d;

    c[x][y] = k == -1 || a[x+dx[k]][y+dy[k]] >= a[x][y] ? ++b : dfs(x+dx[k], y+dy[k]);    
}

int main()
{
    int t;
    scanf("%d", &t);

    for (int tt=1; tt<=t; tt++)
    {
        memset(c, 0, sizeof(c));
        memset(e, 0, sizeof(e));
        b = 0;

        scanf("%d%d", &n, &m);

        for (int i=0; i<n; i++)
            for (int j=0; j<m; j++)
                scanf("%d", &a[i][j]);

        for (int i=0; i<n; i++)
            for (int j=0; j<m; j++)
                dfs(i, j);

        char s = 'a';

        printf("Case #%d:\n", tt);

        for (int i=0; i<n; i++)
        {
            for (int j=0; j<m; j++)
            {
                if (j)
                    printf(" ");
                if (!e[c[i][j]][0])
                    e[c[i][j]][0] = s++;
                printf(e[c[i][j]]);
            }
            puts("");
        }
    }
    return 0;
}


