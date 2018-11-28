#include <stdio.h>

int n, m;
int data[100][100];
int used[100][100];
int x[100][100];
int y[100][100];

int xxx[26], yyy[26], ppp;

char getthechar (int xx, int yy)
{
    for (int i = 0; i < ppp; i ++)
        if (xxx[i] == x[xx][yy] && yyy[i] == y[xx][yy])
            return 'a' + i;
    xxx[ppp] = x[xx][yy];
    yyy[ppp] = y[xx][yy];
    ppp ++;
    
    return 'a' + ppp - 1;
}

void dfs (int xx, int yy)
{
    used[xx][yy] = 1;
    x[xx][yy] = xx;
    y[xx][yy] = yy;
    
    int height = data[xx][yy];
    
    if (xx - 1 >= 0 && data[xx - 1][yy] < height)
    {
        if (!used[xx - 1][yy])
            dfs (xx - 1, yy);
        x[xx][yy] = x[xx - 1][yy];
        y[xx][yy] = y[xx - 1][yy];
        height = data[xx - 1][yy];
    }

    if (yy - 1 >= 0 && data[xx][yy - 1] < height)
    {
        if (!used[xx][yy - 1])
            dfs (xx, yy - 1);
        x[xx][yy] = x[xx][yy - 1];
        y[xx][yy] = y[xx][yy - 1];
        height = data[xx][yy - 1];
    }

    if (yy + 1 < m && data[xx][yy + 1] < height)
    {
        if (!used[xx][yy + 1])
            dfs (xx, yy + 1);
        x[xx][yy] = x[xx][yy + 1];
        y[xx][yy] = y[xx][yy + 1];
        height = data[xx][yy + 1];
    }

    if (xx + 1 < n && data[xx + 1][yy] < height)
    {
        if (!used[xx + 1][yy])
            dfs (xx + 1, yy);
        x[xx][yy] = x[xx + 1][yy];
        y[xx][yy] = y[xx + 1][yy];
        height = data[xx + 1][yy];
    }
}

int main ()
{
    int t;
    
    scanf("%d", &t);
    for (int it = 1; it <= t; it ++)
    {
        scanf("%d%d", &n, &m);
        for (int i = 0; i < n; i ++)
            for (int j = 0; j < m; j ++)
                scanf("%d", data[i] + j);
        for (int i = 0; i < n; i ++)
            for (int j = 0; j < m; j ++)
                used[i][j] = 0;
        for (int i = 0; i < n; i ++)
            for (int j = 0; j < m; j ++)
                if (!used[i][j])
                    dfs(i, j);
        ppp = 0;
        printf("Case #%d:\n", it);
        for (int i = 0; i < n; i ++)
            for (int j = 0; j < m; j ++)
                printf("%c%c", getthechar(i, j), j < m - 1? ' ' : '\n');
    }

    return 0;
}
