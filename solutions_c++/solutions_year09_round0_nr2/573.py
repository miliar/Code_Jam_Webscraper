#include<iostream>
#include<cstring>
//#include<cstdio>
using namespace std;
int dx[4]={-1,0,0,1};
int dy[4]={0,-1,1,0};
int W,H,cnt;
char f[110][110];
int h[110][110];

int dfs(int x,int y){
      int i,tp,mini,k;
      if(f[x][y]) return f[x][y];
      mini=h[x][y];
      for(i=0;i<4;i++)
            if(x+dx[i]>=0 && x+dx[i]<H && 
               y+dy[i]>=0 && y+dy[i]<W &&
               mini>(tp=h[x+dx[i]][y+dy[i]])){
                  mini=tp;
                  k=i;
            }
      if(mini<h[x][y]) f[x][y]=dfs(x+dx[k],y+dy[k]);
      else f[x][y]=cnt++;
      return f[x][y];
}
int main(){
      int i,j,T,ca;
      //freopen("B-large.in","r",stdin);
      //freopen("B-large.out","w",stdout);
      scanf("%d",&T);
      for(ca=1;ca<=T;ca++){
            scanf("%d%d",&H,&W);
            for(i=0;i<H;i++)
                  for(j=0;j<W;j++) scanf("%d",&h[i][j]);
            memset(f,0,sizeof(f));
            cnt='a';
            for(i=0;i<H;i++)
                  for(j=0;j<W;j++)
                        if(!f[i][j]){
                              dfs(i,j);
                        }
            printf("Case #%d:\n",ca);
            for(i=0;i<H;i++){
                  for(j=0;j<W-1;j++) printf("%c ",f[i][j]);
                  printf("%c\n",f[i][W-1]);
            }
      }
      return 0;
}