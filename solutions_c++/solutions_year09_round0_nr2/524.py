#include<stdio.h>
int map[100][100], ans[100][100];
int test, h, w;
int num_sink, dir[4][2] = {{-1, 0}, {0, -1}, {0, 1}, {1, 0}};
void my_clear()
{
    int i, j;
    for(i = 0; i < h; i ++)
        for(j = 0; j < w; j ++)
            ans[i][j] = -1;
}
void dfs(int ti, int tj)
{
    int k, x, y, low = map[ti][tj], tx, ty;
//    printf("(%d, %d) num_sink = %d\n", ti, tj, num_sink);
    for(k = 0; k < 4; k ++)
    {
        x = ti + dir[k][0];
        y = tj + dir[k][1];
        if(x >= 0 && y >= 0 && x < h && y < w && map[x][y] < low)
        {
            low = map[x][y];
            tx = x;
            ty = y;
        }
    }
    if(low == map[ti][tj])
    {
        ans[ti][tj] = num_sink;
        num_sink ++;
    }
    else
    {
        if(ans[tx][ty] == -1)
        {
            dfs(tx, ty);
            ans[ti][tj] = ans[tx][ty];            
        }
        else
            ans[ti][tj] = ans[tx][ty];
    }
}
void get_ans()
{
    num_sink = 0;
    int i, j, k, x, y;
    for(i = 0; i < h; i ++)
        for(j = 0; j < w; j ++)
            if(ans[i][j] == -1)
                dfs(i, j);
}
int main()
{
    int t, i, j;
    scanf("%d", &test);
    for(t = 1; t <= test; t ++)
    {
        scanf("%d%d", &h, &w);
        for(i = 0; i < h; i ++)
            for(j = 0; j < w; j ++)
                scanf("%d", map[i] + j);
        printf("Case #%d:\n", t);
        my_clear();
        get_ans();
        for(i = 0; i < h; i ++)
        {
            putchar('a' + ans[i][0]);
            for(j = 1; j < w; j ++)
            {
                putchar(' ');
                putchar('a' + ans[i][j]);
            }
            printf("\n");
        }
    }
    return 0;
}
