#include <iostream>
#include <stdio.h>
#include <list>
#include <map>
#include <set>
using namespace std;
int turn[4][2] = {{-1,0},{0, -1},{0, 1},{1, 0}};

int cell[110][110];
int num[110][110];
int visited[110][110];
int T, H, W;

int getRes(int x, int y)
{
    int t ;
    if (visited[x][y])
        return num[x][y];
    int lowest = cell[x][y];
    int idx = -1;
    int tempx, tempy;
    for ( t = 0; t < 4; t ++)
    {
        tempx = x + turn[t][0];
        tempy = y + turn[t][1];

        if (tempx <H && tempx >=0 && tempy < W && tempy >=0)
        {
            if ( cell[tempx][tempy] < lowest)
            {
                lowest = cell[tempx][tempy];
                idx = t;
            }
        }
    }
    if (idx != -1)
    {
        tempx = x + turn[idx][0];
        tempy = y + turn[idx][1];

        if (!visited[tempx][tempy])
        {
            num[tempx][tempy] = getRes(tempx, tempy);
            visited[tempx][tempy] = 1;
        }
        return num[tempx][tempy];
    }
    else
        return x * W + y;
}

int main()
{
    int *sink[110][110];

    int i,j,k, t;


    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    scanf("%d", &T);

    for (i = 0; i < T; i ++)
    {

        scanf("%d %d", &H, &W);
        for ( j = 0; j < H; j ++)
            for (k = 0; k < W; k ++)
            {
                scanf("%d", &cell[j][k]);
                visited[j][k] = 0;
            }
        for ( j = 0; j < H; j ++)
            for ( k = 0; k < W; k ++)
                num[j][k] = getRes(j,k);
        char seq = 'a';
        set <int> iset;
        map <int,char> imap;
        printf("Case #%d:\n", i+1);

        for ( j = 0; j < H; j ++)
        {
            for ( k = 0; k < W; k ++)
            {
                if (iset.find(num[j][k])==iset.end())
                {
                    imap[num[j][k]] = seq++;
                    iset.insert(num[j][k]);
                }
                printf("%c ", imap[num[j][k]]);
            }
            printf("\n");
        }
    }
    return 0;
}
