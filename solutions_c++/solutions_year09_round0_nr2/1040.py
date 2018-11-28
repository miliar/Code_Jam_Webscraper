#include <iostream>
#define NMax 105
#define INF 10005

using namespace std;

FILE *fin = fopen("input.in", "rt");
FILE *fout = fopen("output.out", "wt");

int T, H, W;
int map[NMax][NMax], cc[NMax][NMax], ccn;

char letter[27];

int dx[] = {-1, 0, 0, +1};
int dy[] = {0, -1, +1, 0};

int flows(int fx, int fy, int tx, int ty)
{
    int lx = fx, ly = fy;
    for (int dir = 0; dir < 4; dir++)
    {
        if (map[lx][ly] > map[fx + dx[dir]][fy + dy[dir]])
        {
            lx = fx + dx[dir];
            ly = fy + dy[dir];
        }
    }

    if (map[lx][ly] > map[fx][fy])
        return 0;

    return (lx == tx && ly == ty);
}

void go(int x, int y)
{
    int dir;
    cc[x][y] = ccn;
    for (dir = 0; dir < 4; dir++)
        if (flows(x + dx[dir], y + dy[dir], x, y) && cc[x + dx[dir]][y + dy[dir]] == 0)
            go(x + dx[dir], y + dy[dir]);
}

int main()
{
    int i, j, test;
    fscanf(fin, "%d", &T);

    for (test = 1; test <= T; test++)
    {
        fscanf(fin, "%d %d", &H, &W);

        for (i = 1; i <= H; i++)
        for (j = 1; j <= W; j++)
        {
            fscanf(fin, "%d", &map[i][j]);
            cc[i][j] = 0;
        }

        for (i = 1; i <= W; i++)
        {
            map[0][i] = INF;
            map[H+1][i] = INF;
            cc[0][i] = INF;
            cc[H+1][i] = INF;
        }
        for (i = 1; i <= H; i++)
        {
            map[i][0] = INF;
            map[i][W+1] = INF;
            cc[i][0] = INF;
            cc[i][W+1] = INF;
        }

        ccn = 1;

        for (i = 1; i <= H; i++)
        for (j = 1; j <= W; j++)
        {
            if (map[i][j] <= map[i][j-1] &&
                map[i][j] <= map[i-1][j] &&
                map[i][j] <= map[i][j+1] &&
                map[i][j] <= map[i+1][j] && cc[i][j] == 0)
                {
                    //this is new sink
                    go(i, j);
                    ccn ++;
                }
        }

        char cletter = 'a';

        for (i = 1; i <= ccn; i++)
            letter[i] = 0;

        for (i = 1; i <= H; i++)
        for (j = 1; j <= W; j++)
        {
            if (letter[cc[i][j]] == 0)
            {
                letter[cc[i][j]] = cletter;
                cletter++;
            }
        }

        fprintf(fout, "Case #%d:\n", test);

/*
        for (i = 1; i <= H; i++)
        {
            for (j = 1; j <= W; j++)
                printf("%d ", cc[i][j]);
            printf("\n");
        }*/

        for (i = 1; i <= H; i++)
        {
            for (j = 1; j <= W; j++)
                fprintf(fout, "%c ", letter[cc[i][j]]);
            fprintf(fout, "\n");
        }
    }

    return 0;
}
