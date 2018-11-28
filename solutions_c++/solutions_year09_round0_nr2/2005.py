#include<stdio.h>
#include<vector>
using namespace std;
char an[110][110];
int map[110][110],used[110][110],bfs[10010];
int dx[4]={-1,0,0,1};
int dy[4]={0,-1,1,0};
int D(int x,int y,int W){return x*W+y;}
vector<int>M[10010];
void Bfs(int x,int H,char c,int t){
    int i,j,k;
    an[x/H][x%H]=c;
    used[x/H][x%H]=t;
    bfs[0]=x;
    for(i=0,j=1;i<j;i++){
        for(k=0;k<M[bfs[i]].size();k++){
            if(used[M[bfs[i]][k]/H][M[bfs[i]][k]%H]!=t){
                used[M[bfs[i]][k]/H][M[bfs[i]][k]%H]=t;
                an[M[bfs[i]][k]/H][M[bfs[i]][k]%H]=c;
                bfs[j++]=M[bfs[i]][k];
            }
        }
    }
}
main(){
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int T,t,i,j,k,flow,mi,H,W;
    char c;
    scanf("%d",&T);
    for(t=1;t<=T;t++){
        scanf("%d %d",&H,&W);
        for(i=0;i<H;i++)
            for(j=0;j<W;j++)scanf("%d",&map[i][j]);
        for(i=0;i<H*W;i++)M[i].clear();
        for(i=0;i<H;i++)
            for(j=0;j<W;j++){
                flow=-1;
                mi=map[i][j];
                for(k=0;k<4;k++){
                    if(i+dx[k]==H||i+dx[k]<0)continue;
                    if(j+dy[k]==W||j+dy[k]<0)continue;
                    if(map[i+dx[k]][j+dy[k]]<mi){
                        mi=map[i+dx[k]][j+dy[k]];
                        flow=k;
                    }
                }
                if(flow>=0){
                    M[D(i,j,W)].push_back(D(i+dx[flow],j+dy[flow],W));
                    M[D(i+dx[flow],j+dy[flow],W)].push_back(D(i,j,W));
                }
            }
        c='a';
        for(i=0;i<H;i++)
            for(j=0;j<W;j++)
                if(used[i][j]!=t)
                    Bfs(D(i,j,W),W,c++,t);
        printf("Case #%d:\n",t);
        for(i=0;i<H;i++,puts(""))
            for(j=0;j<W;j++){
                if(j)printf(" ");
                printf("%c",an[i][j]);
            }
    }
}
