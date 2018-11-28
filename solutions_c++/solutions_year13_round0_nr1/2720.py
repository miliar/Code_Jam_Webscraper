#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
using namespace std;
char dat[5][5];
void fuck()
{
    int cdot = 0;
    for (int i = 0; i < 4; i++)
        scanf(" %s", dat[i]);
    for (int i = 0; i < 4; i++)
    {
        int co = 0, cx = 0, ct = 0;
        for (int j = 0; j < 4; j++)
        {
            co += (int) dat[i][j] == 'O';
            cx += (int) dat[i][j] == 'X';
            ct += (int) dat[i][j] == 'T';
            cdot += (int) dat[i][j] == '.';
        }
        if (co == 4 || (co == 3 && ct == 1))
        {
            printf("O won\n");
            return;
        }
        if (cx == 4 || (cx == 3 && ct == 1))
        {
            printf("X won\n");
            return;
        }
    }
    for (int j = 0; j < 4; j++)
    {
        int co = 0, cx = 0, ct = 0;
        for (int i = 0; i < 4; i++)
        {
            co += (int) dat[i][j] == 'O';
            cx += (int) dat[i][j] == 'X';
            ct += (int) dat[i][j] == 'T';
        }
        if (co == 4 || (co == 3 && ct == 1))
        {
            printf("O won\n");
            return;
        }
        if (cx == 4 || (cx == 3 && ct == 1))
        {
            printf("X won\n");
            return;
        }
    }
    int co = 0, cx = 0, ct = 0;
    for (int i = 0; i < 4; i++)
    {
        co += (int) dat[i][i] == 'O';
        cx += (int) dat[i][i] == 'X';
        ct += (int) dat[i][i] == 'T';
    }
    if (co == 4 || (co == 3 && ct == 1))
    {
        printf("O won\n");
        return;
    }
    if (cx == 4 || (cx == 3 && ct == 1))
    {
        printf("X won\n");
        return;
    }
    co = 0, cx = 0, ct = 0;
    for (int i = 0; i < 4; i++)
    {
        co += (int) dat[i][3-i] == 'O';
        cx += (int) dat[i][3-i] == 'X';
        ct += (int) dat[i][3-i] == 'T';
    }
    if (co == 4 || (co == 3 && ct == 1))
    {
        printf("O won\n");
        return;
    }
    if (cx == 4 || (cx == 3 && ct == 1))
    {
        printf("X won\n");
        return;
    }
    printf("%s\n", cdot ? "Game has not completed" : "Draw");
}
int main(int argc, char const *argv[])
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; i++)
        printf("Case #%d: ", i), fuck();
    return 0;
}
