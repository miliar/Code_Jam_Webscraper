#include <stdio.h>
#include <stdlib.h>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

#define oo 0x7f7f7f7f

int mapa[128][128];
char saida[128][128];
int memo[128][128][2];
int T,W,H;

void faz(int h, int w)
{
    if (memo[h][w][0] > -1)
        return;

    int v[4];
    int dx[] = {0,-1,1,0};
    int dy[] = {-1,0,0,1};
    for(int i = 0; i < 4; i++)
        v[i] = (h+dy[i] >= 0 && h+dy[i] < H && w+dx[i] >= 0 && w+dx[i] < W) ? mapa[h+dy[i]][w+dx[i]] : +oo;

    int k = -1;
    for(int i = 0; i < 4; i++)
        if (v[i] < mapa[h][w] && (k == -1 || v[i] < v[k]))
            k = i;
    if (k > -1)
    {
        faz(h+dy[k],w+dx[k]);
        memo[h][w][0] = memo[h+dy[k]][w+dx[k]][0];
        memo[h][w][1] = memo[h+dy[k]][w+dx[k]][1];
    }
    else
    {
        memo[h][w][0] = h;
        memo[h][w][1] = w;
    }
}

int main(void)
{
    scanf("%d",&T);
    for(int i = 0; i < T; i++)
    {
        scanf("%d %d",&H,&W);
        memset(saida,0,sizeof(saida));
        for(int h = 0; h < H; h++)
            for(int w = 0; w < W; w++)
                scanf("%d",&mapa[h][w]);

        memset(memo,-1,sizeof(memo));

        for(int h = 0; h < H; h++)
            for(int w = 0; w < W; w++)
                faz(h,w);

        char ch = 'a';
        for(int h = 0; h < H; h++)
            for(int w = 0; w < W; w++)
                if (saida[memo[h][w][0]][memo[h][w][1]] == 0)
                    saida[memo[h][w][0]][memo[h][w][1]] = ch++;

        printf("Case #%d:\n",i+1);
        for(int h = 0; h < H; h++,printf("\n"))
            for(int w = 0; w < W; w++)
                printf("%c ",saida[memo[h][w][0]][memo[h][w][1]]);
                //printf("(%d %d)",memo[h][w][0],memo[h][w][1]);
    }
    

    return(0);
}

