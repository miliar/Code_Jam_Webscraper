# include <iostream>
using namespace std;

int q[4][2]={{-1, 0},{0, -1},{0, 1},{1, 0}};
int h, w;
int v[100][100];
char ww[100][100], cc;

bool valid(int x, int y)
{
    return x>=0 && x<h && y>=0 && y<w;
}

char dfs(int x, int y)
{
    int m=-1, a, b, i, c, d;
    if (ww[x][y]!=0) {
        return ww[x][y];
    }
    for (i=0; i<4; i++) {
        a=x+q[i][0];
        b=y+q[i][1];
        if (valid(a, b) && v[x][y]>v[a][b]) {
            if (m==-1) {
                m=i;
            }
            else {
                c=x+q[m][0];
                d=y+q[m][1];
                if (v[a][b]<v[c][d]) {
                    m=i;
                }
            }
        }
    }
    if (m==-1) {
        ww[x][y]=cc++;
    }
    else {
        a=x+q[m][0];
        b=y+q[m][1];
        ww[x][y]=dfs(a, b);
    }
    return ww[x][y];
}

struct point
{
    int x;
    int y;
    int val;
};

int main()
{
    int t, i, j, tt=1;
    scanf("%d", &t);
    while(t--) {
        scanf("%d%d", &h, &w);
        memset(ww, 0, sizeof ww);
        for (i=0; i<h; i++) {
            for (j=0; j<w; j++) {
                scanf("%d", &v[i][j]);
            }
        }
        cc='a';
        for (i=0; i<h; i++) {
            for (j=0; j<w; j++) {
                dfs(i, j);
            }
        }
        printf("Case #%d:\n", tt++);
        for (i=0; i<h; i++) {
            for (j=0; j<w; j++) {
                putchar(ww[i][j]);
                if (j<w) {
                    putchar(' ');
                }
            }
            putchar('\n');
        }
    }
    return 0;
}
