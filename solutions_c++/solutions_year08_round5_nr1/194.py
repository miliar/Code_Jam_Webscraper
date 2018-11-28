#include <cstdio>
#include <cstring>
using namespace std;
const int dir[4][2]={0,1,1,0,0,-1,-1,0};

struct status {
   int x,y;  
}; 

bool g[250][250][4];
bool been[250][250];
bool is[250][250];
status q[100000];
int nx,ny,nd,sx,sy;

void go_step() {
    if (nd==0) {
        g[nx][ny][3]=true;
        g[nx-1][ny][1]=true;
    }
    if (nd==1) {
        g[nx][ny][2]=true;
        g[nx][ny-1][0]=true;        
    }
    if (nd==2) {
        g[nx][ny-1][3]=true;
        g[nx-1][ny-1][1]=true;
    }
    if (nd==3) {
        g[nx-1][ny][2]=true;
        g[nx-1][ny-1][0]=true;
    }                
    nx=nx+dir[nd][0];
    ny=ny+dir[nd][1];
    if (ny<sy || (ny==sy && nx<sx)) {
        sy=ny;
        sx=nx;
    }    
}    

void floodfill(int x,int y) {
    memset(been,0,sizeof(been));
    been[x][y]=true;
    is[x][y]=true;
    int h=0,t=1;
    q[1].x=x;q[1].y=y;
    while (h<t) {
        status now=q[++h];
        for (int d=0;d<=3;d++) {
            if (g[now.x][now.y][d]) continue;
            status tmp=now;
            tmp.x=tmp.x+dir[d][0];
            tmp.y=tmp.y+dir[d][1];            
            if (been[tmp.x][tmp.y]) continue;
            been[tmp.x][tmp.y]=true;
            is[tmp.x][tmp.y]=true;
            t++;
            q[t].x=tmp.x;q[t].y=tmp.y;
        }    
    }    
}    

bool go1(int x,int y) {
    bool no=true;
    for (int i=0;i<=x-1;i++) {
        if (is[i][y]) {
            no=false;
            break;
        }    
    }    
    if (no) return false;
    no=true;
    for (int i=x+1;i<=220;i++) {
        if (is[i][y]) {
            no=false;
            break;
        }    
    }    
    if (no) return false;
    return true;
}    

bool go2(int x,int y) {
    bool no=true;
    for (int i=0;i<=y-1;i++) {
        if (is[x][i]) {
            no=false;
            break;
        }    
    }    
    if (no) return false;
    no=true;
    for (int i=y+1;i<=220;i++) {
        if (is[x][i]) {
            no=false;
            break;
        }    
    }    
    if (no) return false;
    return true;
}    

int main() {
    char op[100];
    int n,t,cases;
    scanf("%d",&cases);
    for (int kase=1;kase<=cases;kase++) {
        nx=110;ny=110;nd=0;sx=1000;sy=1000;
        memset(g,0,sizeof(g));
        scanf("%d",&n);
        for (int i=1;i<=n;i++) {
            scanf("%s%d",op,&t);
            int len=strlen(op);
            for (;t>0;t--) {
                for (int j=0;j<len;j++) {
                    char ch=op[j];
                    if (ch=='F') {
                        go_step();
                    }
                    if (ch=='L') {
                        nd--;
                        if (nd<0) nd=3;
                    }
                    if (ch=='R') {
                        nd++;
                        if (nd>3) nd=0;
                    }
                }              
            }    
        }    
//        printf("Shit!");
        memset(q,0,sizeof(q));
        memset(is,0,sizeof(is));
//        printf("%d %d\n",sx,sy);                        
        floodfill(sx,sy);
//        printf("Shit!");
        int ans=0;
        for (int i=0;i<=220;i++)
           for (int j=0;j<=220;j++) {
//              if (!is[i][j]) printf("c %d %d\n",i,j);
              if ((!is[i][j]) && (go1(i,j) || go2(i,j))) ans++;
           }    
        printf("Case #%d: %d\n",kase,ans);
    }    
}    
