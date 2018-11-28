#include <iostream>
using namespace std;

char square[4][5];

bool judgeWin(char ch)
{
    int result;

    //row
    for (int i = 0; i  < 4; ++i)
    {
        result = 1;
        for (int j = 0; j < 4; ++j)
        {
            if (square[i][j] != ch && square[i][j] != 'T')
            {
                result = 0;
                break;
            }
        }
        if (result == 1)
            return true;
    }

    //col
    for (int i = 0; i < 4; ++i)
    {
        result = 1;
        for (int j = 0; j < 4; ++j)
        {
            if (square[j][i] != ch && square[i][j] != 'T')
            {
                result = 0;
                break;
            }
        }
        if (result == 1)
            return true;
    }

    //diamond
    result = 1;
    for (int i = 0; i < 4; ++i)
    {
        if (square[i][i] != ch && square[i][i] != 'T')
        {
            result = 0;
            break;
        }
    }

    if (result == 1)
        return true;

    result = 1;
    for (int i = 0; i < 4; ++i)
    {
        if (square[i][3-i] != ch && square[i][3-i] != 'T')
        {
            result = 0;
            break;
        }
    }

    if (result == 1)
        return true;

    return false;
}

bool hasEmpty()
{
    for (int i = 0; i < 4; ++i)
    {
        for (int j = 0; j < 4; ++j)
        {
            if (square[i][j] == '.')
            {
                return true;
            }
        }
    }
    return false;
}

int main ()
{
    int kase, ncase = 0;

    freopen("A.in", "r", stdin);
    freopen("A.out", "w", stdout);

    scanf("%d", &kase);
    while (kase--)
    {
        for (int i = 0; i < 4; ++i)
        {
            scanf("%s", &square[i]);
        }

        if (judgeWin('X'))
        {
            printf("Case #%d: X won\n", ++ncase);
        }
        else if (judgeWin('O'))
        {
            printf("Case #%d: O won\n", ++ncase);
        }
        else if (hasEmpty())
        {
            printf("Case #%d: Game has not completed\n", ++ncase);
        }
        else
        {
            printf("Case #%d: Draw\n", ++ncase);
        }
    }

    return 0;
}
