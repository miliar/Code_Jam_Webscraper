#include <iostream>
#include <cstring>
#include <algorithm>
#include <cstdio>
#include <queue>
#include <vector>
#include <cctype>
#include <string>

#define FOR(i, a, b) for(int i = a;i < b;++i)
using namespace std;

const int MAXN = 10005;
int T, M, N;

char Map[4][4];

bool check(char c)
{
    char G[4][4];
    memcpy(G, Map, sizeof(Map));
    for(int i = 0;i < 4;++i) for(int j = 0;j < 4;++j)   if(G[i][j] == 'T')  G[i][j] = c;
    for(int i = 0;i < 4;++i)
    {
        if(G[i][0] == c && G[i][1] == c && G[i][2] == c && G[i][3] == c)    return true;
        if(G[0][i] == c && G[1][i] == c && G[2][i] == c && G[3][i] == c)    return true;
    }
    if(G[0][0] == c && G[1][1] == c && G[2][2] == c && G[3][3] == c)    return true;
    if(G[0][3] == c && G[1][2] == c && G[2][1] == c && G[3][0] == c)    return true;
    return false;
}

int cas;
int main()
{
    scanf("%d", &T);
    for(int t = 1;t <= T;++t)
    {
        printf("Case #%d: ", t);
        for(int i = 0;i < 4;++i)
        {
            scanf("%s", Map[i]);
        }
        if(check('X'))  printf("X won\n");
        else if(check('O')) printf("O won\n");
        else
        {
            bool notComplete = false;
            for(int i = 0;i < 4;++i)
                for(int j = 0;j < 4;++j)
                    if(Map[i][j] == '.')
                        notComplete = true;
            if(notComplete) 
                printf("Game has not completed\n");
            else printf("Draw\n");
        }
    }
}

