#include <cstdio>
#include <algorithm>
using namespace std;

char board[512][512];

int table1[512][512];
int table2[512][512];
int table0[512][512];
int table3[2][512][512];
int table4[2][512][512];

int get(int t[512][512], int x1, int y1, int x2, int y2)
{
    return t[x2][y2] - t[x1 - 1][y2] - t[x2][y1 - 1] + t[x1 - 1][y1 - 1];
}

int main()
{
    int T;
    scanf("%d", &T);

    for(int testnum = 1; testnum  <= T; testnum++)
    {
        int R, C, D;
        scanf("%d%d%d", &R, &C, &D);

        for(int i = 1; i <= R; i++)
            for(int j = 1; j <= C; j++)
            {
                scanf(" %c", &board[i][j]); 
                board[i][j] -= '0';

                table1[i][j] = i * board[i][j];
                table1[i][j] += table1[i - 1][j];
                table2[i][j] = j * board[i][j];
                table2[i][j] += table2[i][j - 1];

                table3[1][i][j] = 0;
                table4[1][i][j] = 0;
                table0[i][j] = board[i][j];
                table0[i][j] += table0[i][j - 1];
            }
        for(int i = 1; i <= R; i++)
            for(int j = 1; j <= C; j++)
                table0[i][j] += table0[i - 1][j];


        int ans = 0;
        for(int k = 2; k <= min(R, C); k++)
            for(int i = 1; i + k - 1 <= R; i++)
                for(int j = 1; j + k - 1 <= C; j++)
                {
                    int now = k & 1;
                    int pre = !now;
                    table3[now][i][j] = table3[pre][i][j] + 
                    get(table0, i + k - 1, j, i + k - 1, j + k - 1) * (k - 1)
                    + (table1[i + k - 2][j + k - 1] - table1[i - 1][j + k - 1]) - i * get(table0, i, j + k - 1, i + k - 2, j + k - 1);

                    table4[now][i][j] = table4[pre][i][j] + 
                     get(table0, i, j + k - 1, i + k - 1, j + k - 1) * (k - 1)
                    + (table2[i + k - 1][j + k - 2] - table2[i + k - 1][j - 1]) - j * get(table0, i + k - 1, j, i + k - 1, j + k - 2);

                   
                   int d1 = table3[now][i][j] - (board[i + k - 1][j] + board[i + k - 1][j + k - 1]) * (k - 1);
                   int d2 = table4[now][i][j] - (board[i][j + k - 1] + board[i + k - 1][j + k - 1]) * (k - 1);

                   int m = get(table0, i, j, i + k - 1, j + k - 1) - board[i][j] - board[i + k - 1][j] - board[i][j + k - 1] - board[i + k - 1][j + k - 1];
                   if(d1 == d2 && d1 * 2ll == (k - 1ll) * m)
                   {
                       ans = k;
                       }
                }
        printf("Case #%d: ", testnum);
        if(ans < 3)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n", ans);
    }
    return 0;
}
