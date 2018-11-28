#include <stdio.h>
#include <ctype.h>

int map[102][102], h, w;
char basin, mapb[102][102];

char findSink(int, int);

int main()
{
    FILE *arq, *out;
    arq = fopen("watersheds.in","r");
    out = fopen("watersheds.out","w");

    for(int i = 0; i < 102; i++)
    {
        map[i][0] = 10001;
        map[0][i] = 10001;
    }
    int T;
    fscanf(arq,"%d",&T);
    for(int k = 1; k <=T; k++)
    {
        /*input*/
        fscanf(arq,"%d %d", &h, &w);
        for(int i = 1; i <= h; i++)
            for(int j = 1; j <= w; j++)
            {
                mapb[i][j] = 'X';
                fscanf(arq,"%d",&map[i][j]);
            }
        for(int i = 1; i <= h + 1; i++)
            map[i][w + 1] = 10001;
        for(int i = 1; i <= w + 1; i++)
            map[h + 1][i] = 10001;
        /*resolvendo o problema*/
        basin = 'a' - 1;
        for(int i = 1; i <= h; i++)
            for(int j = 1; j <= w; j++)
                if(mapb[i][j] == 'X')
                    mapb[i][j] = findSink(i,j);

        /*output*/
        fprintf(out,"Case #%d:\n",k);
        for(int i = 1; i <= h; i++)
        {
            for(int j = 1; j <= w; j++)
            {
                if(j==w)
                {
                    fprintf(out,"%c",mapb[i][j]);
                    break;
                }
                fprintf(out,"%c ",mapb[i][j]);
            }
            fprintf(out,"\n");
        }
    }
    fclose(arq);
    fclose(out);
    return 0;
}

char findSink(int row, int col)
{
    int rm = 0, cm = 0;

    if(map[row - 1][col + 0] < map[row + rm][col + cm])  { rm = -1; cm = 0;}
    if(map[row + 0][col - 1] < map[row + rm][col + cm])  { rm = 0; cm = -1;}
    if(map[row + 0][col + 1] < map[row + rm][col + cm])  { rm = 0; cm = 1;}
    if(map[row + 1][col + 0] < map[row + rm][col + cm])  { rm = 1; cm = 0;}

    if(rm == 0 && cm == 0)
    {
        basin++;
        return basin;
    }

    if(mapb[row + rm][col + cm] == 'X')
        mapb[row + rm][col + cm] = findSink(row + rm, col + cm);
    return mapb[row + rm][col + cm];
}
