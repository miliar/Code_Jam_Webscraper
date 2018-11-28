#include <algorithm>
#include <cstdio>
using namespace std;

const int N = 102;
const int INF = 1<<20;

int dx[]={0,1,-1,0};
int dy[]={1,0,0,-1};

int h,w;
int a[N][N];
char id[N][N];

int ey[N][N],ex[N][N];

void load() {
    scanf("%d%d",&h,&w);
    for(int i=0;i<h;i++)
        for(int j=0;j<w;j++) scanf("%d",&a[j+1][i+1]);
}

void make_e() {
    for(int x=1;x<=w;x++)
        for(int y=1;y<=h;y++) {
            ex[x][y]=x; ey[x][y]=y;
            int best = INF;
            for(int i=0;i<4;i++) best=min(best,a[x+dx[i]][y+dy[i]]);
            if (best>=a[x][y]) continue;
            for(int i=0;i<4;i++) if (a[x+dx[i]][y+dy[i]]<=a[ex[x][y]][ey[x][y]]) {
                ex[x][y]=x+dx[i]; ey[x][y]=y+dy[i];
            }
        }
/*    for(int y=1;y<=h;y++) {
        for(int x=1;x<=w;x++) printf("(%2d;%2d)  ",ex[x][y],ey[x][y]);
        printf("\n");
    }//*/
}

void visit(int x, int y, char c) {
    if (x<1||y<1||x>w||y>h) return;
    if (id[x][y]) return;
    id[x][y]=c;
    visit(ex[x][y],ey[x][y],c);
    for(int i=0;i<4;i++)
        if (ex[x+dx[i]][y+dy[i]]==x && ey[x+dx[i]][y+dy[i]]==y) 
            visit(x+dx[i],y+dy[i],c);
}

void cas() {
    load();
    make_e();
    for(int x=1;x<=w;x++) for(int y=1;y<=h;y++) id[x][y]=0;
    char c = 'a';
    for(int y=1;y<=h;y++) for(int x=1;x<=w;x++)
        if (!id[x][y]) visit(x,y,c++);
    for(int y=1;y<=h;y++) {
        for(int x=1;x<=w;x++) printf("%c ",id[x][y]);
        printf("\n");
    }
}

int main() {
       int j; scanf("%d",&j);
    for(int cn=1;cn<=j;cn++) {
    for(int i=0;i<N;i++) for(int j=0;j<N;j++) a[i][j]=INF;

        printf("Case #%d:\n",cn);
        cas();
    }
    return 0;
}




