#include <iostream>
#include <cstring>
#include <algorithm>
using namespace std;

const int N = 110;

bool maps[N][N][2];
bool f;

void init()
{
    int n;
    cin>>n;

    memset(maps, 0, sizeof(maps));
    f = 0;

    for(int i = 1; i <= n; i++)
    {
        int X1, Y1, X2, Y2;
        cin>>X1>>Y1>>X2>>Y2;
        swap(X1, Y1);
        swap(X2, Y2);

        for(int i = X1; i <= X2; i++)
        {
            for(int j = Y1; j <= Y2; j++)
            {
                maps[i][j][f] = 1;
            }
        }
    }
}

const int M = 100;

bool ok()
{
    /*for(int i = 1; i <= M; i++)
    {
        for(int j = 1; j <= M; j++)
        {
            printf("%d ", maps[i][j][f]);
        }
        printf("\n");
    }
    printf("\n");*/

    for(int i = 1; i <= M; i++)
    {
        for(int j = 1; j <= M; j++)
        {
            if(maps[i][j][f]) return 0;
        }
    }
    return 1;
}

void modle()
{
    for(int i = 1; i <= M; i++)
    {
        for(int j = 1; j <= M; j++)
        {
            maps[i][j][f^1] = maps[i][j][f];
            if(maps[i][j][f])
            {
                if(!maps[i-1][j][f] && !maps[i][j-1][f]) maps[i][j][f^1] = 0;
            }
            else
            {
                if(maps[i-1][j][f] && maps[i][j-1][f]) maps[i][j][f^1] = 1;
            }
        }
    }
}

void solve(int tcase)
{
    int res = 0;
    while(1)
    {
        if(ok()) break;
        res++;
        modle();
        f ^= 1;
    }
    printf("Case #%d: %d\n", tcase, res);
}

int main()
{
    freopen("in", "r", stdin);
    freopen("out", "w", stdout);
    int T;
    cin>>T;

    for(int i = 1; i <= T; i++)
    {
        init();
        solve(i);
    }
}