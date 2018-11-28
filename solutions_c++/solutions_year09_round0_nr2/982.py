#include <iostream>
#include <cstdio>
using namespace std;

int H,W;
int G[100][100], GG[100][100];

void fill(int y, int x, int id) {
    int mm, xx,yy;
    bool flag=true;

    while(flag) {
        flag=false;
        mm=-1;

        if(GG[y][x]) {
            for(int i=0;i<H;i++) for(int j=0;j<W;j++) if(GG[i][j]==id) GG[i][j]=GG[y][x];
            break;
        }

        GG[y][x] = id;
        if(y-1 >= 0 && G[y-1][x]<G[y][x] && G[y][x]-G[y-1][x] > mm) { mm=G[y][x]-G[y-1][x]; xx=x; yy=y-1; flag=true; }
        if(x-1 >= 0 && G[y][x-1]<G[y][x] && G[y][x]-G[y][x-1] > mm) { mm=G[y][x]-G[y][x-1]; xx=x-1; yy=y; flag=true; }
        if(x+1 < W && G[y][x+1]<G[y][x] && G[y][x]-G[y][x+1] > mm) { mm=G[y][x]-G[y][x+1]; xx=x+1; yy=y; flag=true; }
        if(y+1 < H && G[y+1][x]<G[y][x] && G[y][x]-G[y+1][x] > mm) { mm=G[y][x]-G[y+1][x]; xx=x; yy=y+1; flag=true; }

        x=xx; y=yy;
    }
}

void fill2(int y, int x, int id) {
    int t=GG[y][x];

    GG[y][x]=id;

    if(y-1 >= 0 && GG[y-1][x]==t) fill2(y-1,x, id);
    if(x-1 >= 0 && GG[y][x-1]==t) fill2(y,x-1, id);
    if(y+1 < H && GG[y+1][x]==t) fill2(y+1,x, id);
    if(x+1 < W && GG[y][x+1]==t) fill2(y,x+1, id);
}

int main() {
    int T;

    cin >> T;
    for(int n=1;n<=T;n++) {
        cin >> H >> W;

        for(int i=0;i<H;i++) for(int j=0;j<W;j++) { cin >> G[i][j]; GG[i][j]=0; }

        int id = -1;
        for(int altitudes=10000; altitudes>=0; altitudes--) {
            for(int i=0;i<H;i++) for(int j=0;j<W;j++) {
                if(GG[i][j]==0 && G[i][j]==altitudes) { fill(i,j, id); id--; }
            }
        }

        id=0;
        for(int i=0;i<H;i++) for(int j=0;j<W;j++) if(GG[i][j]<0) { fill2(i,j, id); id++; }
        
        printf("Case #%d:\n", n);
        for(int i=0;i<H;i++) {
            for(int j=0;j<W;j++) printf("%-2c", GG[i][j]+'a');
            puts("");
        }
    }

    return 0;
}

