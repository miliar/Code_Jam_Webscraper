#include <stdio.h>
#include <string>
#include <string.h>

using namespace std;

char board[5][5];

bool win(char x)
{
    int i, j, num;
    for (i = 0; i < 4; i++)
    {
        num = 0;
        for (j = 0; j < 4; j++)
            if (board[i][j] == x || board[i][j] == 'T') num++;
        if (num == 4) return true;
    }

    for (j = 0; j < 4; j++)
    {
        num = 0;
        for (i = 0; i < 4; i++)
            if (board[i][j] == x || board[i][j] == 'T') num++;
        if (num == 4) return true;
    }

    num = 0;
    for (i = 0; i < 4; i++)
        if (board[i][i] == x || board[i][i] == 'T') num++;
    if (num == 4) return true;

    num = 0;
    for (i = 0; i < 4; i++)
        if (board[i][3 - i] == x || board[i][3 - i] == 'T') num++;
    if (num == 4) return true;
    return false;
}

bool completed()
{
    int i, j;
    for (i = 0; i < 4; i++)
        for (j = 0; j < 4; j++)
            if (board[i][j] =='.') return false;
    return true;
}


int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int cas = 1; cas <= T; cas++)
    {
        for (int i = 0 ; i < 4 ; i++)
            scanf("%s", board[i]);
        string ans;
        if (win('X')) ans = "X won";
        else if (win('O')) ans = "O won";
            else if (completed()) ans = "Draw";
                else ans = "Game has not completed";
        printf("Case #%d: %s\n", cas, ans.c_str());
    }
    return 0;
}
