#include <iostream>

using namespace std;

#define BORDER 20000

int map[105][105];
char region[105][105];
int direction[4][2] = {{0, -1}, {-1, 0}, {1, 0}, {0, 1}};
int LastID;

int updateMap(int x, int y, int Width, int Height)
{
    if( region[y][x]!=0 )
        return region[y][x];

    int alt = map[y][x];
    int i, min = -1;
    for(i=0; i<4; i++)
    {
        if( alt > map[y+direction[i][1]][x+direction[i][0]] )
        {
            alt = map[y+direction[i][1]][x+direction[i][0]];
            min = i;
        }
    }
    if( min==-1 )
    {
        region[y][x] = ++LastID;
    }
    else
    {
        region[y][x] = updateMap(x+direction[min][0], y+direction[min][1], Width, Height);
    }
    return region[y][x];
}

int main()
{
    int T, H, W;
    int a, b, c, h, w;
    scanf("%d", &T);
    for(a=1; a<=T; a++)
    {
        scanf("%d%d", &H, &W);
        LastID = 0;
        for(w=1; w<=W; w++)
        {
            map[0][w] = map[H+1][w] = BORDER;
        }
        for(h=1; h<=H; h++)
        {
            for(w=1; w<=W; w++)
            {
                scanf("%d", &map[h][w]);
                region[h][w] = 0;
            }
            map[h][0] = map[h][W+1] = BORDER;
        }
        for(h=1; h<=H; h++)
        {
            for(w=1; w<=W; w++)
            {
                if( region[h][w]==0 )
                {
                    updateMap(w, h, W, H);
                }
            }
        }
        printf("Case #%d:\n", a);
        for(h=1; h<=H; h++)
        {
            for(w=1; w<=W; w++)
            {
                printf("%c ", 'a'-1+region[h][w]);
            }
            printf("\n");
        }
    }
    return 0;
}
