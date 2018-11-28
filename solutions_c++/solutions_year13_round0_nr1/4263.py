#include<cstdio>

int t=0,tot;
char board[10][10];

bool check(char c)
{
    for (int i=0;i<4;i++)
    {
        bool ok=1;
        for (int j=0;j<4;j++)
            ok&=(board[i][j]==c || board[i][j]=='T');
        if (ok) return 1;
        ok=1;
        for (int j=0;j<4;j++)
            ok&=(board[j][i]==c || board[j][i]=='T');
        if (ok) return 1;
    }
    bool ok1=1,ok2=1;
    for (int i=0;i<4;i++)
    {
        ok1&=(board[i][i]==c || board[i][i]=='T');
        ok2&=(board[i][3-i]==c || board[i][3-i]=='T');
    }
    return (ok1+ok2);
}

int main()
{
    for (scanf("%d",&tot);tot--;)
    {
        for (int i=0;i<4;i++) scanf("%s",board[i]);
        bool a=check('X');
        bool b=check('O');
        bool c=0;
        for (int i=0;i<4;i++)
        for (int j=0;j<4;j++)
        if (board[i][j]=='.')
            c=1;
        printf("Case #%d: ",++t);
        if (a) printf("X won\n");else
        if (b) printf("O won\n");else
        if (c) printf("Game has not completed\n");
        else printf("Draw\n");
    }
}
