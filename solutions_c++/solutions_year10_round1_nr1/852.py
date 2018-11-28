#include<stdio.h>

int T, n, k;
char s[60][60], g[60][60];

void trans()
{
    int i, j, tn = n - 1;
    for(i = 0; i < n; i ++)
        for(j = 0; j < n; j ++)
            g[i][j] = s[tn - j][i];
}

void print(char tmp[][60])
{
    int i, j;
    for(i = 0; i < n; i ++)
    {
        for(j = 0; j < n; j ++)
            putchar(tmp[i][j]);
        printf("\n");
    }
    printf("\n");
}

void dispose()
{
    int col, tn = n - 1, r, row;
    for(col = 0; col < n; col ++)
    {
        for(row = tn; row >= 0; row --)
        {
            if(g[row][col] == '.')
                for(r = row - 1; r >= 0; r --)
                {
                    if(g[r][col] != '.')
                    {
                        g[row][col] = g[r][col];
                        g[r][col] = '.';
                        break;
                    }
                }
        }
    }
}

bool red, blue;
void get_ans()
{
    int i, j, t;
    int x, y, h, dir[4][2] = {{1, 0}, {0, 1}, {1, 1}, {1, -1}};
    red = false;
    blue = false;
    for(i = 0; i < n; i ++)
        for(j = 0; j < n; j ++)
        {
            if(g[i][j] == '.')
                continue;
            for(h = 0; h < 4; h ++)
            {
                for(t = 0; t < k; t ++)
                {
                    x = i + t * dir[h][0];
                    y = j + t * dir[h][1];
                    if(x < 0 || x >= n || y < 0 || y >= n || g[x][y] != g[i][j])
                        break;
                }
                if(t == k)
                {
//                    printf("i = %d j = %d t = %d k = %d %c\n", i, j, t, k, g[i][j]);
                    if(g[i][j] == 'R')
                        red = true;
                    else
                        blue = true;
                    break;
                }
            }
        }
}
int main()
{
    scanf("%d", &T);
    int i;
    for(int t = 1; t <= T; t ++)
    {
        scanf("%d%d", &n, &k);
        for(i = 0; i < n; i ++)
            scanf("%s", s[i]);
        trans();
        dispose();
        get_ans();
        printf("Case #%d: ", t);
        if(red && !blue)
            printf("Red\n");
        if(blue && !red)
            printf("Blue\n");
        if(red && blue)
            printf("Both\n");
        if(!red && !blue)
            printf("Neither\n");
    }
    return 0;
} 
