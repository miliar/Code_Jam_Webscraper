#include <iostream>
#include <string>
#include <stdio.h>
#include <memory.h>

using namespace std;

const int offx[] = {-1, 0, 0,+1};
const int offy[] = { 0,-1,+1, 0};

int row, col;
int a[100][100];
int bx[100][100], by[100][100];

int qcnt, qx[10000], qy[10000];
char res_color, res[100][100];

void input()
{
    scanf("%d %d", &row, &col);
    for (int i=0; i<row; i++) for (int j=0; j<col; j++) 
        scanf("%d", &a[i][j]);
}

void find_sink(int x, int y)
{
    int u, v, su, sv, mm;
 
    //
    qcnt = 0;
    while (true)
    {
        //
        qx[qcnt] = x; qy[qcnt] = y; qcnt++;
        if (bx[x][y] != -1) break;

        //
        mm = 1000000;
        for (int k=0; k<4; k++)
        {
            u = x+offx[k]; v = y+offy[k];
            if (!(u>=0 && v>=0 && u<row && v<col)) continue;

            if (mm > a[u][v]) { mm = a[u][v]; su = u; sv = v; }
        }

        if (mm >= a[x][y])  break;
        x = su; y = sv;
    }
    
    //
    int sx, sy;
    x = qx[qcnt-1], y = qy[qcnt-1];
    if (bx[x][y] == -1) { sx = x; sy = y; } else { sx = bx[x][y]; sy = by[x][y]; }
    for (int i=0; i<qcnt; i++) { bx[ qx[i] ][ qy[i] ] = sx; by[ qx[i] ][ qy[i] ] = sy; }
}

void label(int x, int y)
{
    for (int i=0; i<row; i++) for (int j=0; j<col; j++) if (bx[i][j]==bx[x][y] && by[i][j]==by[x][y])
        res[i][j] = res_color;
    res_color++;
}


void process()
{
    //
    memset(bx, -1, sizeof(bx));
    for (int i=0; i<row; i++) for (int j=0; j<col; j++) if (bx[i][j]==-1)
        find_sink(i, j);
    //for (int i=0; i<row; i++) { for (int j=0; j<col; j++) printf("(%d %d) ", bx[i][j], by[i][j]); printf("\n"); }

    //
    res_color = 'a';
    memset(res, ' ', sizeof(res));
    for (int i=0; i<row; i++) for (int j=0; j<col; j++) if (res[i][j] == ' ')
        label(i, j);
}

void output(int test)
{
    printf("Case #%d:\n", test);
    for (int i=0; i<row; i++) for (int j=0; j<col; j++)
    {
        printf("%c%c", res[i][j], (j==col-1 ? '\n' : ' '));
    }
}

int main()
{
    //
    int numtest;
    scanf("%d", &numtest);

    //
    for (int i=0; i<numtest; i++)
    {
        input();
        process();
        output(i+1);
    }
    return 0;
}
