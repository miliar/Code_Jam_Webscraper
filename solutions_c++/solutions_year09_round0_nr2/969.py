#include <stdio.h>
#include <memory.h>

const int maxx = 105;

int N;
int H,W;

int m[maxx][maxx];
char r[maxx][maxx];
int fl[maxx][maxx];

int d[4][2] = { {-1,0}, {0,-1}, {0,1}, {1,0} };

int flow(int x, int y) {
    int mini = -1;
    for(int i=0;i<4;i++) {
        int xx = x+d[i][0], yy = y+d[i][1];
        if(0<=xx && xx<H && 0<=yy && yy<W) {
            if(m[x][y] > m[xx][yy]) {
                if(mini<0 || m[xx][yy]<m[x+d[mini][0]][y+d[mini][1]]) {
                    mini = i;
                }
            }
        }
    }
    return mini;
}

void mark(int x, int y, char c) {
    //if(! (0<=x && x<H && 0<=y && y<W)) return;
    if(r[x][y]>0) return;
    r[x][y] = c;
    if(fl[x][y]>=0) {
        mark(x+d[fl[x][y]][0], y+d[fl[x][y]][1], c);
    }
    for(int i=0;i<4;i++) {
        int xx = x+d[i][0],  yy=y+d[i][1];
        if(0<=xx && xx<H && 0<=yy && yy<W) {
            int dir = fl[xx][yy];
            if(dir >=0 && x==xx+d[dir][0] && y==yy+d[dir][1]) {
                mark(xx, yy, c);
            }
        }
    }
}

int main() {
    scanf("%d",&N);
    for(int ca=1;ca<=N;ca++) {
        scanf("%d%d",&H,&W);
        for(int i=0;i<H;i++) {
            for(int j=0;j<W;j++) {
                scanf("%d",&m[i][j]);
            }
        }
        for(int i=0;i<H;i++) {
            for(int j=0;j<W;j++) {
                fl[i][j] = flow(i,j);
                //printf("%d%c",fl[i][j], (j==W-1?'\n':' '));
            }
        }
        memset(r,0,sizeof(r));
        char c= 'a';
        for(int i=0;i<H;i++) {
            for(int j=0;j<W;j++) {
                if(r[i][j]==0) {
                    mark(i,j,c);
                    c++;
                }
            }
        }
        printf("Case #%d:\n", ca);
        for(int i=0;i<H;i++) {
            for(int j=0;j<W;j++) {
                printf("%c%c",r[i][j], (j==W-1?'\n':' '));
            }
        }
    }
    return 0;
}

