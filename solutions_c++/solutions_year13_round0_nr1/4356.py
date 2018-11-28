#include <iostream>
#include <cstdio>
#include <string.h>
#include <algorithm>
#include <set>
#include <queue>
#include <stack>
#include <map>
#include <vector>
using namespace std;

int run;
char Map[4][4];

bool check(char c)
{
    int C = 0, T = 0;
    for (int i = 0; i < 4; i++)
    {
        if (Map[i][i] == c) C++;
        if (Map[i][i] == 'T') T++;
    }
    if (C == 3 && T == 1) return true;
    if (C == 4) return true;
    C = 0, T = 0;
    for (int i = 0; i < 4; i++)
    {
        if (Map[i][3-i] == c) C++;
        if (Map[i][3-i] == 'T') T++;
    }
    if (C == 3 && T == 1) return true;
    if (C == 4) return true;
    for (int i = 0; i < 4; i++)
    {
        C = 0, T = 0;
        for (int j = 0; j < 4; j++)
        {
            if (Map[i][j] == c) C++;
            if (Map[i][j] == 'T') T++;
        }
        if (C == 3 && T == 1) return true;
        if (C == 4) return true;
    }
    for (int j = 0; j < 4; j++)
    {
        C = 0, T = 0;
        for (int i = 0; i < 4; i++)
        {
            if (Map[i][j] == c) C++;
            if (Map[i][j] == 'T') T++;
        }
        if (C == 3 && T == 1) return true;
        if (C == 4) return true;
    }
    return false;
}

void solve()
{
    for (int i = 0; i < 4; i++) scanf("%s", Map[i]);
    printf("Case #%d: ", run);
    if (check('X'))
    {
        puts("X won");
        return;
    }
    if (check('O'))
    {
        puts("O won");
        return;
    }
    for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++)
            if (Map[i][j] == '.')
            {
                puts("Game has not completed");
                return;
            }
    puts("Draw");
}

int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int test;
    scanf("%d", &test);
    for (run = 1; run <= test; run++) solve();
    return 0;
}
