#pragma comment(linker, "/STACK:102400000,102400000")
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <queue>
using namespace std;

#define INF 0x3f3f3f3f
#define LL long long
#define eps 1e-8
#define lson (pos << 1)
#define rson (pos << 1 | 1)

template<class T> void checkMax(T &a, T b)
{
    a = max(a, b);
}
template<class T> void checkMin(T &a, T b)
{
    a = min(a, b);
}

char g[5][5];
int checkWin(char s)
{
    int i, j;
    for(i = 0; i < 4; i++)
    {
        for(j = 0; j < 4; j++)
            if(g[i][j] != s && g[i][j] != 'T')
                break;
        if(j == 4)  return 1;
        for(j = 0; j < 4; j++)
            if(g[j][i] != s && g[j][i] != 'T')
                break;
        if(j == 4)  return 1;
    }
    for(i = 0; i < 4; i++)
        if(g[i][i] != s && g[i][i] != 'T')
            break;
    if(i == 4)  return 1;
    for(i = 0; i < 4; i++)
        if(g[i][3 - i] != s && g[i][3 - i] != 'T')
            break;
    if(i == 4)  return 1;
    return 0;
}
int checkEnd()
{
    int i, j;
    for(i = 0; i < 4; i++)
        for(j = 0; j < 4; j++)
            if(g[i][j] == '.')
                return 0;
    return 1;
}
int main()
{
    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);
    int t, cas = 1, i, j;
    scanf("%d", &t);
    while(t--)
    {
        for(i = 0; i < 4; i++)
            scanf("%s", g[i]);
        printf("Case #%d: ", cas++);
        if(checkWin('X'))
            printf("X won\n");
        else if(checkWin('O'))
            printf("O won\n");
        else if(checkEnd())
            printf("Draw\n");
        else
            printf("Game has not completed\n");
    }
    return 0;
}
