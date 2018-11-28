#include <iostream>
#include <cstdio>
using namespace std;
char s[5][100];
bool t[5][100];
bool check()
{
    for (int i=0;i<4;i++)
    {
        bool flag = true;
        for (int j=0;j<4;j++)
            if (!t[i][j]) flag = false;
        if (flag) return true;
    }
    for (int j=0;j<4;j++)
    {
        bool flag = true;
        for (int i=0;i<4;i++)
            if (!t[i][j]) flag = false;
        if (flag) return true;
    }
    bool flag = true;
    for (int i=0;i<4;i++)
        if (!t[i][i]) flag = false;
    if (flag) return true;
    flag = true;
    for (int i=0;i<4;i++)
        if (!t[3-i][i]) flag = false;
    if (flag) return true;
    return false;
}
void deal()
{
    bool flag = false;
    for (int i=0;i<4;i++)
        for (int j=0;j<4;j++)
        {
            if (s[i][j]=='X' || s[i][j]=='T') t[i][j] = true;
            else t[i][j] = false;
        }
    if (check())
    {
        printf("X won\n");
        return;
    }
    for (int i=0;i<4;i++)
        for (int j=0;j<4;j++)
        {
            if (s[i][j]=='O' || s[i][j]=='T') t[i][j] = true;
            else t[i][j] = false;
        }
    if (check())
    {
        printf("O won\n");
        return;
    }
    for (int i=0;i<4;i++)
        for (int j=0;j<4;j++)
        {
            if (s[i][j]=='.') flag = true;
        }
    if (flag) printf("Game has not completed\n");
    else printf("Draw\n");
}
int main()
{
    freopen("a.in","r",stdin);
    freopen("a.out","w",stdout);
    int T;
    scanf("%d\n",&T);
    int cas = 0;
    while (T--)
    {
        for (int i=0;i<4;i++) gets(s[i]);
        scanf("\n");
        printf("Case #%d: ",++cas);
        deal();
    }
    return  0;
}
