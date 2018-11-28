#include <stdio.h>
#include <string.h>

int r, c, f;
char data[50][50];

int dp[50][50][50];

void get_init_xy (int x, int y, int &xx, int &yl, int &yr)
{
    xx = x;
    yl = yr = y;
    
    while (xx < r - 1 && data[xx + 1][y] == '.')
        xx ++;
    if (xx - x > f)
    {
        xx = -1;
        return;
    }
    while (yl > 0 && data[xx][yl - 1] == '.' && (xx == r - 1 || data[xx + 1][yl - 1] == '#'))
        yl --;
    while (yr < c - 1 && data[xx][yr + 1] == '.' && (xx == r - 1 || data[xx + 1][yr + 1] == '#'))
        yr ++;
}

void refresh (int x, int y1, int y2, int d)
{
//    printf("refresh %d %d %d %d\n", x, y1, y2, d);
    if (dp[x][y1][y2] == -1 || d < dp[x][y1][y2])
        dp[x][y1][y2] = d;
}

int main ()
{
    int t, ct = 0;
    
    for (scanf ("%d", &t); t > 0; t --)
    {
        scanf("%d%d%d", &r, &c, &f);
        for (int i = 0; i < r; i ++)
            for (int j = 0; j < c; j ++)
            {
                do scanf("%c", data[i] + j);
                    while (data[i][j] <= ' ');
            }
        
        memset(dp, -1, sizeof(dp));
        int srow, lpos, rpos;
        get_init_xy(0, 0, srow, lpos, rpos);
        if (srow != -1)
            dp[srow][lpos][rpos] = 0;
        
        for (int i = 0; i < r - 1; i ++)
            for (int j = 0; j < c; j ++)
                for (int k = j; k < c; k ++)
                    if (dp[i][j][k] != -1)
                    {
//                        printf("doing %d %d %d\n", i, j, k);
                        //special case: leftmost pos is hole
                        if (i + 1 < r && data[i + 1][j] == '.')
                        {
                            int x2, yl, yr;
                            
                            get_init_xy(i, j, x2, yl, yr);
                            if (x2 != -1)
                            {
                                refresh(x2, yl, yr, dp[i][j][k]);
                            }
                            break;
                        }
                        //special case: rightmost pos is hole
                        if (i + 1 < r && data[i + 1][k] == '.')
                        {
                            int x2, yl, yr;
                            
                            get_init_xy(i, k, x2, yl, yr);
                            if (x2 != -1)
                            {
                                refresh(x2, yl, yr, dp[i][j][k]);
                            }
                            break;
                        }
                        // if there's left hole.
                        if (j - 1 >= 0 && data[i][j - 1] == '.')
                        {
                            int x2, yl, yr;
                            
                            get_init_xy(i, j - 1, x2, yl, yr);
                            if (x2 != -1)
                            {
                                refresh(x2, yl, yr, dp[i][j][k]);
                            }
                        }
                        // if there's right hole.
                        if (j + 1 < c && data[i][k + 1] == '.')
                        {
                            int x2, yl, yr;
                            
                            get_init_xy(i, k + 1, x2, yl, yr);
//                            printf("right hole %d %d: %d %d %d\n", i, j + 1, x2, yl, yr);
                            if (x2 != -1)
                            {
                                refresh(x2, yl, yr, dp[i][j][k]);
                            }
                        }
                        // make new holes !!! (to your left)
                        for (int h = j; h < k; h ++)
                        {
                            int x2, yl, yr;
                            
                            data[i + 1][h] = '.';
                            
                            get_init_xy(i, h, x2, yl, yr);
/*
                            printf("Hey! %d %d %d\n", x2, yl, yr);
                            for (int i = 0; i < r; i ++)
                            {
                                for (int j = 0; j < c; j ++)
                                    printf("%c", data[i][j]);
                                printf("\n");
                            }
*/
                            if (x2 == i + 1)
                            {
                                int cc = 1;
                                refresh(x2, yl, yr, dp[i][j][k] + 1);
                                for (int h2 = yl - 1; h2 >= 0; h2 --)
                                {
                                    if (data[i + 1][h2] == '#')
                                    {
                                        if (h2 < j - 1)
                                            break;
                                        if (!(h2 >= j && h2 <= k) && data[i][h2] == '#')
                                            break;
                                        cc ++;
                                    }
                                    refresh(x2, h2, yr, dp[i][j][k] + cc);
                                    if (i + 2 < r && data[i + 2][h2] == '.')
                                        break;
                                }
                            }
                            if (x2 > i + 1)
                            {
                                refresh(x2, yl, yr, dp[i][j][k] + 1);
                            }

                            data[i + 1][h] = '#';
                        }
                        // make new holes !!! (to your right)
                        for (int h = j + 1; h <= k; h ++)
                        {
                            int x2, yl, yr;
                            
                            data[i + 1][h] = '.';
                            
                            get_init_xy(i, h, x2, yl, yr);
                            if (x2 == i + 1)
                            {
                                int cc = 1;
                                refresh(x2, yl, yr, dp[i][j][k] + 1);
                                for (int h2 = yr + 1; h2 < c; h2 ++)
                                {
                                    if (data[i + 1][h2] == '#')
                                    {
                                        if (h2 > k + 1)
                                            break;
                                        if (!(h2 >= j && h2 <= k) && data[i][h2] == '#')
                                            break;
                                        cc ++;
                                    }
                                    refresh(x2, yl, h2, dp[i][j][k] + cc);
                                    if (i + 2 < r && data[i + 2][h2] == '.')
                                        break;
                                }
                            }
                            if (x2 > i + 1)
                            {
                                refresh(x2, yl, yr, dp[i][j][k] + 1);
                            }

                            data[i + 1][h] = '#';
                        }
                    }
        
        int answer = -1;
        for (int i = 0; i < c; i ++)
            for (int j = 0; j < c; j ++)
                if (dp[r - 1][i][j] != -1 && (answer == -1 || dp[r - 1][i][j] < answer))
                    answer = dp[r - 1][i][j];
        
        if (answer >= 0)
            printf("Case #%d: Yes %d\n", ++ct, answer);
        else
            printf("Case #%d: No\n", ++ct);
    }
    
    return 0;
}
/*
100
6 6 4
......
######
######
###.##
###.##
###.##
*/
