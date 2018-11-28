#include <stdio.h>
#include <iostream>
using namespace std;

int t ,n = 4;
char a[10][10];

bool check(char c)
{
    int k;

    for (int i = 0;i < n;++i)
    {
        k = 0;
        for (int j = 0;j < n;++j)
            if (a[i][j] == c|| a[i][j] == 'T') k++;
        if (k == 4) return true;
        k = 0;
        for (int j = 0;j < n;++j)
            if (a[j][i] == c || a[j][i] == 'T') k++;
        if (k == 4) return true;
    }
    k= 0;
    for (int i = 0;i < n;++i)
        if (a[i][i] == c || a[i][i] == 'T') k++;
    if (k == 4) return true;
    k= 0;
    for (int i = 0;i < n;++i)
        if (a[i][n-1-i] ==  c || a[i][n-1-i] == 'T') k++;
    if (k == 4) return true;
    return false;
}

bool empty()
{
    for (int i = 0;i < n;++i)
        for (int j = 0;j < n;++j)
            if (a[i][j] == '.') return true;
    return false;
}

int main()
{
    freopen("2.in","r",stdin);
    freopen("1.out","w",stdout);
    scanf("%d%*c",&t);
    for (int w = 1; w <= t; ++w)
    {
        printf("Case #%d: ",w);
        for (int i = 0;i < n;++i)
        {
            for (int j = 0;j < n;++j) scanf("%c",&a[i][j]);
            scanf("%*c");
        }
        scanf("%*c");
        if (check('X')) printf("X won\n");
        else if (check('O')) printf("O won\n");
             else if (!empty()) printf("Draw\n");
                  else printf("Game has not completed\n");
    }

    return 0;
}
