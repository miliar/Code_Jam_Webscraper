#include <iostream>
#include <cstdio>
using namespace std;

const char* msg[4] = {
    "X won",
    "O won",
    "Draw",
    "Game has not completed"
};

char s[5][10];
int x, y;

bool Check(char ch)
{
    s[x][y] = ch;

    bool ok = true;
    for (int i = 0; i < 4; ++i)
        ok &= (s[i][i] == ch);
    if (ok) return true;

    ok = true;
    for (int i = 0; i < 4; ++i)
        ok &= (s[i][3 - i] == ch);
    if (ok) return true;

    for (int i = 0; i < 4; ++i)
    {
        ok = true;
        for (int j = 0; j < 4; ++j)
            ok &= (s[i][j] == ch);
        if (ok) return true;
    }

    for (int j = 0; j < 4; ++j)
    {
        ok = true;
        for (int i = 0; i < 4; ++i)
            ok &= (s[i][j] == ch);
        if (ok) return true;
    }

    return false;
}

int main()
{
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("output.txt", "w", stdout);

    int nTests;
    scanf("%d", &nTests);
    for (int t = 1; t <= nTests; ++t)
    {
        int res = 2;
        for (int i = 0; i < 4; ++i)
        {
            scanf("%s", s[i]);
            for (int j = 0; j < 4; ++j)
            {
                if (s[i][j] == '.') res = 3;
                if (s[i][j] == 'T')
                    x = i, y = j;
            }
        }
        if (Check('X')) res = 0;
        if (Check('O')) res = 1;

        printf("Case #%d: %s", t, msg[res]);
        if (t < nTests) printf("\n");
    }
}