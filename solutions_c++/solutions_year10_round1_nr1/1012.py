#include <stdio.h>
#include <memory.h>

char map[55][55];
char rotate[55][55];
int matrix[55][55][2][4];
int main()
{
    int t,tt;
    int n,k,i,j,col,row;
    int maxb,maxr;
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    scanf("%d",&t);

    for (tt = 1; tt <= t; tt ++)
    {
        scanf("%d%d",&n,&k);
        getchar();
        for (i = 0; i < 55; i ++)
        {
            for (j = 0; j < 55; j ++)
            {
                rotate[i][j] = 0;
            }
        }
        for (i = 0; i < n; i ++)
        {
            for (j = 0; j < n; j ++)
            {
                map[i][j] = getchar();
            }
            getchar();
        }
        col = 1;
        for (i = n - 1; i >= 0; i --)
        {
            row = n;
            for (j = n - 1; j >= 0; j --)
            {
                if (map[i][j] != 'B' && map[i][j] != 'R')
                    continue;
                rotate[row --][col] = map[i][j];
            }
            col ++;
        }

        memset(matrix,0,sizeof(matrix));
        maxb = maxr = 0;

        for (i = 1; i <= n; i ++)
        {
            for (j = 1; j <= n; j ++)
            {
                if (rotate[i][j] == 'B')
                {
                    matrix[i][j][0][0] = 1 + matrix[i - 1][j][0][0];
                    if (maxb < matrix[i][j][0][0])
                        maxb = matrix[i][j][0][0];
                    matrix[i][j][0][1] = 1 + matrix[i][j - 1][0][1];
                    if (maxb < matrix[i][j][0][1])
                        maxb = matrix[i][j][0][1];
                    matrix[i][j][0][2] = 1 + matrix[i - 1][j - 1][0][2];
                    if (maxb < matrix[i][j][0][2])
                        maxb = matrix[i][j][0][2];
                    matrix[i][j][0][3] = 1 + matrix[i - 1][j + 1][0][3];
                    if (maxb < matrix[i][j][0][3])
                        maxb = matrix[i][j][0][3];
                }
                if (rotate[i][j] == 'R')
                {
                    matrix[i][j][1][0] = 1 + matrix[i - 1][j][1][0];
                    if (maxr < matrix[i][j][1][0])
                        maxr = matrix[i][j][1][0];
                    matrix[i][j][1][1] = 1 + matrix[i][j - 1][1][1];
                    if (maxr < matrix[i][j][1][1])
                        maxr = matrix[i][j][1][1];
                    matrix[i][j][1][2] = 1 + matrix[i - 1][j - 1][1][2];
                    if (maxr < matrix[i][j][1][2])
                        maxr = matrix[i][j][1][2];
                    matrix[i][j][1][3] = 1 + matrix[i - 1][j + 1][1][3];
                    if (maxr < matrix[i][j][1][3])
                        maxr = matrix[i][j][1][3];
                }
            }
        }/*
        for (i = 1; i <= n; i ++)
        {
            for (j = 1; j <= n; j ++)
            {
                putchar(rotate[i][j]);
            }
            putchar('\n');
        }*/
        printf("Case #%d: ",tt);
        if (maxb >= k && maxr >= k)
            puts("Both");
        else if (maxb < k && maxr >= k)
            puts("Red");
        else if (maxb >= k && maxr < k)
            puts("Blue");
        else
            puts("Neither");
        //printf("%d %d\n",maxb,maxr);
    }
    return 0;
}
