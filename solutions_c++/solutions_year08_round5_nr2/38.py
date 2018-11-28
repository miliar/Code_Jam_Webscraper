#include<cstdio>
#include<deque>
#define L 16

using namespace std;

struct P{
    int x,y,x1,y1,x2,y2;
};

const int fx[4]={1,0,-1,0};
const int fy[4]={0,1,0,-1};

deque<P> Q;

struct{
    int x,y;
    void set(int xx,int yy){x=xx;y=yy;}
}connect[L][L][4];

P old,ne;
int I,T,r,c,i,j,d,x,y;
int ans,value;
int sx,sy,ex,ey;
int opt[L][L][L][L][L][L];
bool bt[L][L][L][L][L][L];
char map[L][L];

inline bool isok(int x,int y){ return x>=0 && x<r && y>=0 &&y<c && map[x][y]=='.';}

void Update(const P & a,const int k){
    if (!isok(a.x,a.y)) return;
    if (a.x==ex && a.y==ey) {ans<?=k;return;}
    if (opt[a.x][a.y][a.x1][a.y1][a.x2][a.y2]>k){
        opt[a.x][a.y][a.x1][a.y1][a.x2][a.y2]=k;
        if (!bt[a.x][a.y][a.x1][a.y1][a.x2][a.y2]){
            bt[a.x][a.y][a.x1][a.y1][a.x2][a.y2]=true;
            Q.push_back((P){a.x,a.y,a.x1,a.y1,a.x2,a.y2});
        }
    }
}
main(){
    for (I=1,scanf("%d",&T);I<=T;++I){
        scanf("%d%d\n",&r,&c);
        printf("Case #%d: ",I);
        for (i=0;i<r;++i) gets(map[i]);
        for (i=0;i<r;++i)
            for (j=0;j<c;++j)
                if (map[i][j]=='O'){
                    sx=i;
                    sy=j;
                    map[i][j]='.';
                }
                else if (map[i][j]=='X'){
                    ex=i;
                    ey=j;
                    map[i][j]='.';
                }
        for (i=0;i<r;++i)
            for (j=0;j<c;++j)
                for (d=0;d<4;++d){
                    x=i;y=j;
                    while (isok(x+fx[d],y+fy[d])) x+=fx[d],y+=fy[d];
                    connect[i][j][d].set(x,y);
                }
        Q.clear();
        Q.push_back((P){sx,sy,r,c,r,c});
        memset(bt,0,sizeof bt);
        memset(opt,0x3f,sizeof opt);
        opt[sx][sy][r][c][r][c]=0;
        ans=100000;
        while (!Q.empty()){
            old=Q.front();
            Q.pop_front();
            value=opt[old.x][old.y][old.x1][old.y1][old.x2][old.y2];
            bt[old.x][old.y][old.x1][old.y1][old.x2][old.y2]=false;
            if (value>=ans) continue;
            if (old.x1==old.x && old.y1==old.y){
                ne=old;
                ne.x=ne.x2;
                ne.y=ne.y2;
                Update(ne,value+1);
            }
            if (old.x2==old.x && old.y2==old.y){
                ne=old;
                ne.x=ne.x1;
                ne.y=ne.y1;
                Update(ne,value+1);
            }
            for (i=0;i<4;++i){
                ne=old;
                ne.x1=connect[ne.x][ne.y][i].x;
                ne.y1=connect[ne.x][ne.y][i].y;
                Update(ne,value);
                ne=old;
                ne.x2=connect[ne.x][ne.y][i].x;
                ne.y2=connect[ne.x][ne.y][i].y;
                Update(ne,value);
            }
            for (i=0;i<4;++i){
                ne=old;
                ne.x+=fx[i];
                ne.y+=fy[i];
                Update(ne,value+1);
            }
        }
        if (ans>10000) printf("THE CAKE IS A LIE\n");
        else printf("%d\n",ans);
    }
}
