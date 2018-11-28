#include <iostream>
#include <stdio.h>
#include <list>
using namespace std;
int turn[4][2] = {{-1,0},{0, -1},{0, 1},{1, 0}};


int main()
{
    int cell[110][110];
    int num[110][110];
    int *sink[110][110];
    int T, H, W;
    int i,j,k, t;


    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    scanf("%d", &T);

    for (i = 0; i < T; i ++)
    {

        scanf("%d %d", &H, &W);
        for ( j = 0; j < H; j ++)
            for (k = 0; k < W; k ++)
            {
                scanf("%d", &cell[j][k]);
                num[j][k] = j * W + k;
                sink[j][k] = & num[j][k];
            }
        for ( j = 0; j < H; j ++)
            for ( k = 0; k < W; k ++)
            {
                int lowest = cell[j][k];
                int idx = -1;
                for ( t = 0; t < 4; t ++)
                {
                    int tempx, tempy;
                    tempx = j + turn[t][0];
                    tempy = k + turn[t][1];
                    if ( tempx >=0 && tempx <H && tempy >=0 && tempy < W)
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
                    sink[j][k] = sink[j + turn[idx][0]][k + turn[idx][1]];
                }
            }

        for ( j = 0; j < H; j ++)
        {
            for ( k = 0; k < W; k ++)
            {
                printf("%d ", *sink[j][k]);
            }
            printf("\n");
        }
    }
    return 0;
}
