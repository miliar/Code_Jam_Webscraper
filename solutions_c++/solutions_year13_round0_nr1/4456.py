#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

const int n = 4;

char s[10][10];

bool judgeX(char c)
{
    return (c == 'X' || c == 'T');
}

bool judgeO(char c)
{
    return (c == 'O' || c == 'T');
}

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int t;
    int cc = 0;
    scanf("%d",&t);
    while (t--)
    {
        for (int i=1;i<=n;i++)
        {
            scanf("%s",&s[i][1]);
        }

        bool flag1 = false;
        for (int i=1;i<=n;i++)
        {
            int cnt = 0;
            for (int j=1;j<=n;j++) if (judgeX(s[i][j])) cnt++;
            if (cnt == 4) flag1 = true;
        }


        for (int j=1;j<=n;j++)
        {
            int cnt = 0;
            for (int i=1;i<=n;i++) if (judgeX(s[i][j])) cnt++;
            if (cnt == 4) flag1 = true;
        }



        if (judgeX(s[1][1]) && judgeX(s[2][2]) && judgeX(s[3][3]) && judgeX(s[4][4])) flag1 = true;

        if (judgeX(s[4][1]) && judgeX(s[3][2]) && judgeX(s[2][3]) && judgeX(s[1][4])) flag1 = true;


        bool flag2 = false;
        for (int i=1;i<=n;i++)
        {
            int cnt = 0;
            for (int j=1;j<=n;j++) if (judgeO(s[i][j])) cnt++;
            if (cnt == 4) flag2 = true;
        }


        for (int j=1;j<=n;j++)
        {
            int cnt = 0;
            for (int i=1;i<=n;i++) if (judgeO(s[i][j])) cnt++;
            if (cnt == 4) flag2 = true;
        }



        if (judgeO(s[1][1]) && judgeO(s[2][2]) && judgeO(s[3][3]) && judgeO(s[4][4])) flag2 = true;

        if (judgeO(s[4][1]) && judgeO(s[3][2]) && judgeO(s[2][3]) && judgeO(s[1][4])) flag2 = true;

        printf("Case #%d: ",++cc);
        if (flag1) puts("X won");
        else if (flag2) puts("O won");
        else
        {
            bool flag = false;
            for (int i=1;i<=n;i++)
                for (int j=1;j<=n;j++)
                    if (s[i][j] == '.') flag = true;
            if (!flag) puts("Draw");
            else puts("Game has not completed");
        }


    }
    return 0;
}
