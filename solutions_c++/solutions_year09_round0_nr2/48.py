#include <cstdio>

int dx[4] = {-1, 0, 0, 1};
int dy[4] = {0, -1, 1, 0};
int t, h, w;
int height[110][110];
int marked[110][110];
int to[110][110];
int ncolor;
int color[110][110];
int lettercolor[100];
char colorletter[100];
int fila[20000][2];
int size;
int pos;

int ff(int posx, int posy)
{
    int i;
    int px, py;
    int nx, ny;
    pos = 0;
    size = 1;
    fila[0][0] = posx;
    fila[0][1] = posy;
    color[posx][posy] = ncolor;
    while (pos<size)
    {
        px = fila[pos][0];
        py = fila[pos][1];
        //printf("(%d %d)\n", px, py);
        if (to[px][py] != -1)
        {
            nx = px + dx[to[px][py]];
            ny = py + dy[to[px][py]];
            if (color[nx][ny] == -1)
            {
                fila[size][0] = nx;
                fila[size][1] = ny;
                //printf("add (%d %d)\n", nx, ny);
                color[nx][ny] = ncolor;
                size++;
            }
        }
        for (i=0; i<4; i++)
        {
            nx = px - dx[i];
            ny = py - dy[i];
            if (nx < 0 || nx >= h) continue;
            if (ny < 0 || ny >= w) continue;
            if (to[nx][ny] != i) continue;
            if (color[nx][ny] != -1) continue;
            fila[size][0] = nx;
            fila[size][1] = ny;
            //printf("add (%d %d)\n", nx, ny);
            color[nx][ny] = ncolor;
            size++;
        }
        pos++;
    }
    return 0;
}

int main()
{
    int i, j, k;
    
    scanf("%d\n", &t);
    
    for (int teste=0; teste<t; teste++)
    {
        scanf("%d %d", &h, &w);
        for(i=0; i<h; i++)
        {
            for (j=0; j<w; j++)
            {
                scanf("%d", &height[i][j]);
            }
        }
        ncolor = 0;
        for (i=0; i<h; i++)
        {
            for (j=0; j<w; j++)
            {
                color[i][j] = -1;
            }
        }
        for (i=0; i<h; i++)
        {
            for (j=0; j<w; j++)
            {
                int best = -1;
                int hbest = height[i][j];
                for (k=0; k<4; k++)
                {
                    int nx = i + dx[k];
                    int ny = j + dy[k];
                    if (nx < 0 || nx >= h) continue;
                    if (ny < 0 || ny >= w) continue;
                    if (hbest > height[nx][ny])
                    {
                        best = k;
                        hbest = height[nx][ny];
                    }
                }
                to[i][j] = best;
            }
        }
        for (i=0; i<h; i++)
        {
            for (j=0; j<w; j++)
            {
                if (color[i][j] == -1)
                {
                    ff(i, j);
                    ncolor++;
                }
            }
        }
        for (i=0; i<ncolor; i++)
        {
            colorletter[i] = 0;
        }
        int lcount = 0;
        for (i=0; i<h; i++)
        {
            for (j=0; j<w; j++)
            {
                if (colorletter[color[i][j]] == 0)
                {
                    colorletter[color[i][j]] = lcount + 'a';
                    lcount++;
                }
            }
        }
        
        printf("Case #%d:\n", teste+1);
        for (i=0; i<h; i++)
        {
            for (j=0; j<w; j++)
            {
                printf("%c ", colorletter[color[i][j]]);
            }
            printf("\n");
        }
    }
    return 0;
}
