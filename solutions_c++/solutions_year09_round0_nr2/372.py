#include<iostream>
static int kk[4][2]={-1,0,0,-1,0,1,1,0};
char vis[110][110],bg;
int mp[110][110],n,m;
bool valid(int x,int y){
    if(x<0||x>=n||y<0||y>=m)return false;
    return true;
}
char dfs(int x,int y){
    //printf("%d %d %c\n",x,y,bg);
    //system("pause");
    
    if(vis[x][y]>0)return vis[x][y];
    int k,min_i=-1,mn=mp[x][y];
    for(k=0;k<4;++k){
        int nx=x+kk[k][0],ny=y+kk[k][1];
        if(valid(nx,ny)){
            if(mp[nx][ny]<mn){
                mn=mp[nx][ny];
                min_i=k;
            }
        }
    }
    if(min_i<0)return bg++;
    int nx=x+kk[min_i][0],ny=y+kk[min_i][1];
    return vis[nx][ny]=dfs(nx,ny);
}
int main(){
    freopen("B-large.out","w",stdout);
    int T,i,j;
    scanf("%d",&T);
    for(int Cas=1;Cas<=T;++Cas){
        scanf("%d%d",&n,&m);
        for(i=0;i<n;++i)for(j=0;j<m;++j)scanf("%d",&mp[i][j]);
        memset(vis,0,sizeof(vis));
        bg='a';
        for(i=0;i<n;++i){
            for(j=0;j<m;++j){
                if(vis[i][j]==0){
                    vis[i][j]=dfs(i,j);
                }
            }
        }
        printf("Case #%d: \n",Cas);
        for(i=0;i<n;++i){
            for(j=0;j<m;++j)printf("%c ",vis[i][j]);
            putchar(10);
        }
    }
    return 0;
}
