#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;
int n;
char ss[6][6];
bool test(char x)
{
    bool ok = true;
    for (int i = 0; i < 4; ++i)
    {
        ok = true;
        for (int j = 0; j < 4; ++j)
            if (ss[i][j] != x && ss[i][j] != 'T')
                ok = false;
        if (ok) return true;
    }
    for (int i = 0; i < 4; ++i)
    {
        ok = true;
        for (int j = 0; j < 4; ++j)
            if (ss[j][i] != x && ss[j][i] != 'T')
                ok = false;
        if (ok) return true;
    }
    ok = true;
    for (int i = 0; i < 4; ++i)
    {
        if (ss[i][i] != x && ss[i][i] != 'T')
            ok = false;
    }
    if (ok) return true;

    ok = true;
    for (int i = 0; i < 4; ++i)
    {
        if (ss[i][3 - i] != x && ss[i][3 - i] != 'T')
            ok = false;
    }
    if (ok) return true;
    return false;
}
void cal()
{
    bool hasDot = false;
    for (int i = 0; i < 4; ++i)
        for (int j = 0; j < 4; ++j)
            if (ss[i][j] == '.')
            {
                hasDot = true;
            }
    if (test('X'))
        printf("X won\n");
    else if (test('O'))
        printf("O won\n");
    else if (hasDot)
        printf("Game has not completed\n");
    else printf("Draw\n");
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A.out","w",stdout);
    scanf("%d",&n);
    for (int ca = 1; ca <= n; ++ca)
    {
        for (int i = 0; i < 4; ++i)
            scanf("%s",ss[i]);
        printf("Case #%d: ",ca);
        cal();
    }
    return 0;
}
