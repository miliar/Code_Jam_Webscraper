#include <cstdio>
#include <iostream>
#include <cstring>
#include <vector>
#include <cmath>
using namespace std;

char g[6][6];

bool check(char ch)
{
    for (int i = 0; i < 4; i++)
    {
        bool flag = true;
        for (int j = 0; j < 4; j++)
            if ((g[i][j] != ch) &&(g[i][j] != 'T'))
                flag = false;
        if (flag)
            return true;
    }
    for (int i = 0; i < 4; i++)
    {
        bool flag = true;
        for (int j = 0; j < 4; j++)
            if ((g[j][i] != ch)&&(g[j][i] != 'T'))
                flag = false;
        if (flag)
            return true;
    }
    bool flag = true;
    for (int i = 0; i < 4; i++)
        if ((g[i][i] != ch) &&(g[i][i] != 'T'))
            flag = false;
    if (flag)
        return true;
    flag = true;
    for (int i = 0; i < 4; i++)
        if ((g[i][3 - i] != ch) && (g[i][3 - i] != 'T'))
            flag = false;
    return flag;
}

int main()
{
//    freopen("D:\\A-large.in","r",stdin);
//    freopen("D:\\large-data.out","w",stdout);
    int cas, t = 0;
    scanf("%d", &cas);
    while (cas--)
    {
        for (int i = 0; i < 4; i++)
            scanf("%s", &g[i]);
        bool xwin, ywin, flag;
        xwin = ywin = flag = false;
        xwin = check('X');
        ywin = check('O');
        for (int i = 0; i < 4; i++)
            for (int j = 0; j < 4; j++)
                if (g[i][j] == '.')
                    flag = true;
        printf("Case #%d: ",++t);
        if (xwin)printf("X won\n");
        else if (ywin)printf("O won\n");
        else if (flag)printf("Game has not completed\n");
        else printf("Draw\n");
    }
    return 0;
}