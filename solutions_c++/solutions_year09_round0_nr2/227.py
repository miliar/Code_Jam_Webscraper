#include <stdio.h>
#include <cstring>
#define INF 0x3f3f3f3f

int h[110][10010], n, m;
int mark[110][10010], pre[110][10010];

int lv;
int dr[4] = {-1, 0, 0, 1};
int dc[4] = {0, -1, 1, 0};

void init()
{
    scanf("%d%d", &n, &m);
    for(int i=0; i<n; ++i)
    {
        for(int j=0; j<m; ++j) scanf("%d", &h[i][j]);
    }
}

void dfs(int r, int c)
{
    int r1 = -1, c1 = -1, Min = h[r][c];
    for(int k=0; k<4; ++k)
    {
        int rr = r + dr[k];
        int cc = c + dc[k];
        if(rr>=0 && rr<n && cc>=0 && cc<m && h[rr][cc] < Min)
        {
            r1 = rr;
            c1 = cc;
            Min = h[rr][cc];
        }
    }

    if(r1 != -1)
    {
        if(mark[r1][c1] != -1) mark[r][c] = mark[r1][c1];
        else
        {
            dfs(r1, c1);
            mark[r][c] = mark[r1][c1];
        }
        return;
    }
    else mark[r][c] = lv++;
}

void solve(int tc)
{
    memset(mark, -1, sizeof mark);

    lv = 0;
    for(int i=0; i<n; ++i)
    {
        for(int j=0; j<m; ++j)
        {
            if(mark[i][j] == -1) dfs(i, j);
        }
    }

    printf("Case #%d:\n", tc);
    for(int i=0; i<n; ++i)
    {
        for(int j=0; j<m-1; ++j) printf("%c ", 'a' + mark[i][j]);
        printf("%c\n", 'a' + mark[i][m-1]);
    }
}

int main()
{
    int t, k = 0;
    scanf("%d", &t);
    while(t--)
    {
        init();
        solve(++k);
    }
    return 0;
}

