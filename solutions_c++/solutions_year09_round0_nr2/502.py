#include <cstdio>
#include <cstring>

using namespace std;

#define INF 0x3f3f3f3f

char res[105][105];
int h[105][105];
int r,c;
char cur;

int dy[4]={-1,0,0,1};
int dx[4]={0,-1,1,0};

bool conn(int y0,int x0, int y1, int x1){
    if(h[y0][x0]<=h[y1][x1]) return false;
    
    int mmin=INF;
    for(int i=0;i<4;i++){
        int ny=y0+dy[i];
        int nx=x0+dx[i];
        if(ny>=0&&ny<r&&nx>=0&&nx<c)
            mmin<?=h[ny][nx];
    }
    for(int i=0;i<4;i++){
        int ny=y0+dy[i];
        int nx=x0+dx[i];
        if(ny>=0&&ny<r&&nx>=0&&nx<c&&h[ny][nx]==mmin){
            if(ny==y1&&nx==x1)return true;
            else return false;
        }
    }
    return false;
}

bool connected(int y0,int x0,int y1,int x1){
    return conn(y0,x0,y1,x1)||conn(y1,x1,y0,x0);
}

void dfs(int y,int x){
    res[y][x]=cur;
    //("%d %d %c\n",y,x,cur);
    for(int i=0;i<4;i++){
        int ny=y+dy[i];
        int nx=x+dx[i];
        if(ny>=0&&ny<r&&nx>=0&&nx<c&&!res[ny][nx]&&connected(y,x,ny,nx))
            dfs(ny,nx);
    }
}

int main(){
    int test; scanf("%d",&test);
    for(int t=1;t<=test;t++){
        printf("Case #%d:\n",t);
        scanf("%d %d",&r,&c);
        for(int i=0;i<r;i++)
        for(int j=0;j<c;j++)
            scanf("%d",&h[i][j]);
        
        cur='a';
        memset(res,0,sizeof(res));
        for(int i=0;i<r;i++)
        for(int j=0;j<c;j++)
            if(!res[i][j]){
                dfs(i,j);
                cur++;
            }
        
        for(int i=0;i<r;i++){
        for(int j=0;j<c;j++){
            printf("%c",res[i][j]);
            if(j!=c-1) printf(" ");
        }
        printf("\n");
        }
    }
}
