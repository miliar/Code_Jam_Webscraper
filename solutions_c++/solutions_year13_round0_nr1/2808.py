#include <iostream>
#include <cstring>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <queue>
#include <vector>
using namespace std;

const int Maxn = 5;
char board[Maxn][Maxn];
bool over()
{
    for(int i = 0; i < 4; ++i)
        for (int j = 0; j < 4; ++j)
            if (board[i][j] == '.') return false;
    return true;
}
bool equal(char x, char y)
{
    if (x == '.' || y == '.') return false;
    if (x == y || x == 'T' || y == 'T') return true;
    return false;
}
bool checkRowX()
{
    for (int i = 0; i < 4; ++i)
    {
        int j;
        for ( j = 0; j < 4; ++j)
        {
            if (!equal('X', board[i][j])) break;
        }
        if (j == 4) return true;
    }
    return false;
}
bool checkRowO()
{
    for (int i = 0; i < 4; ++i)
    {
        int j;
        for ( j = 0; j < 4; ++j)
        {
            if (!equal('O', board[i][j])) break;
        }
        if (j == 4) return true;
    }
    return false;
}
bool checkColX()
{
    for (int i = 0; i < 4; ++i)
    {
        int j;
        for ( j = 0; j < 4; ++j)
        {
            if (!equal('X', board[j][i])) break;
        }
        if (j == 4) return true;
    }
    return false;
}
bool checkColO()
{
    for (int i = 0; i < 4; ++i)
    {
        int j;
        for ( j = 0; j < 4; ++j)
        {
            if (!equal('O', board[j][i])) break;
        }
        if (j == 4) return true;
    }
    return false;
}
bool checkTrX()
{

    int i;
    for (i = 0; i < 4; ++i)
    {
        if (equal('X', board[i][i]) == false) break;
    }
    if(i == 4) return true;
    for (i = 0; i < 4; ++i)
        if (!equal('X',board[i][3 - i])) break;
    if (i == 4) return true;
    return false;
}
bool checkTrO()
{

    int i;
    for (i = 0; i < 4; ++i)
    {
        if (equal('O', board[i][i]) == false) break;
    }
    if(i == 4) return true;
    for (i = 0; i < 4; ++i)
        if (!equal('O',board[i][3 - i])) break;
    if (i == 4) return true;
    return false;
}
int solve()
{
    if (checkRowX()) return 1;
    if (checkRowO()) return 2;
    if (checkColX()) return 1;
    if (checkColO())return 2;
    if (checkTrX())return 1;
    if (checkTrO()) return 2;
    return 0;
}
int main()
{
   // freopen("in.txt", "r", stdin);
  //  freopen("small.in", "r", stdin);
  //  freopen("small.out", "w", stdout);
    freopen("large.in", "r", stdin);
    freopen("large.out", "w", stdout);
    int T;scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas)
    {
        printf("Case #%d: ", cas);
        for (int i = 0; i < 4; ++i)
        {
            scanf("%s", board[i]);
        }


        int res = solve();
        if (res == 0)
        {
            if (over())
        {
            printf("Draw\n");
            continue;
        }
            printf("Game has not completed");
        }else if(res == 1) printf("X won");
        else printf("O won");
        puts("");

    }


    return 0;
}
