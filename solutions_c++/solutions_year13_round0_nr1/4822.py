#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
using namespace std;

int testcase , T;
char data[5][5];

void init()
{
    int i , j;
    for (i = 1; i <= 4; i++)
    {
        for (j = 1; j <= 4; j++)
        {
            scanf("%c" , &data[i][j]);
        }
        scanf("\n");
    }
    scanf("\n");
}

inline bool check_win(int x , int type , int who)
{
    int i , j , k;
    char ch;
    if (who == 0) ch = 'O'; else ch = 'X';
    if (type == 1)
    {
        for (i = 1; i <= 4; i++)
        {
            if (data[x][i] != ch && data[x][i] != 'T') return 0;
        }
    }
    if (type == 2)
    {
        for (i = 1; i <= 4; i++)
        {
            if (data[i][x] != ch && data[i][x] != 'T') return 0;
        }
    }
    if (type == 3)
    {
        for (i = 1; i <= 4; i++)
        {
            if (x == 1) j = i; else j = 5 - i;
            if (data[i][j] != ch && data[i][j] != 'T') return 0;
        }
    }
    return 1;
}

void work()
{
    printf("Case #%d: " , testcase);
    for (int who = 0; who <= 1; who++)
    {
        bool win = 0;
        for (int i = 1; i <= 4; i++)
        {
            win |= check_win(i , 1 , who);
            win |= check_win(i , 2 , who);
            if (i <= 2) win |= check_win(i , 3 , who);
        }
        if (win)
        {
            char ch;
            if (who == 0) ch = 'O'; else ch = 'X';
            printf("%c won\n" , ch);
            return;
        }
    }
    for (int i = 1; i <= 4; i++)
    {
        for (int j = 1; j <= 4; j++)
        {
            if (data[i][j] == '.')
            {
                printf("Game has not completed\n");
                return;
            }
        }
    }
    printf("Draw\n");
}

int main()
{
    freopen("in.txt" , "r" , stdin);
    freopen("out.txt" , "w" , stdout);
    scanf("%d\n" , &T);
    for (testcase = 1; testcase <= T; testcase++)
    {
        init();
        work();
    }
    return 0;
}
