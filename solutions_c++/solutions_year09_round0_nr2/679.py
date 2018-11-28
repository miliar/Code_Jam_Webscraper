#include<iostream>
using namespace std;
int h,w;
int a[101][101];
int r[101][101];
int k;
int dir[4][2]={{-1,0},{0,-1},{0,1},{1,0}};
char p[30];
inline bool f(int i,int j){
     return i>=0&&i<h&&j>=0&&j<w;
     }
void dfs(int x,int y){
     int i,j;
     int px,py;
     int temp=10000000;
     int tx,ty;
     for(i=0;i<4;i++){
                      tx=x+dir[i][0];
                      ty=y+dir[i][1];
                      if(f(tx,ty)&&temp>a[tx][ty]){
                                                   temp=a[tx][ty];
                                                   px=tx;
                                                   py=ty;
                                                   }
                      }
     if(a[x][y]<=temp)r[x][y]=k++;
     else {
          if(r[px][py]==-1)dfs(px,py);
          r[x][y]=r[px][py];
          }
     }
void solve(){
     int i,j;
     k=0;
     for(i=0;i<h;i++){
                      for(j=0;j<w;j++){
                                       if(r[i][j]==-1)dfs(i,j);
                                       }
                      }
     for(i=0;i<k;i++)p[i]=' ';
     char t='a';
     for(i=0;i<h;i++){
                      for(j=0;j<w;j++){
                                       if(p[r[i][j]]==' ')p[r[i][j]]=t++;
                                       cout<<p[r[i][j]]<<" ";
                                       }
                      cout<<endl;
                      }
     }
int main(){
    int t;
    scanf("%d",&t);
    int count=1;
    while(t--){
               scanf("%d%d",&h,&w);
               int i,j;
               for(i=0;i<h;i++){
                                for(j=0;j<w;j++){
                                                 r[i][j]=-1;
                                                 scanf("%d",&a[i][j]);
                                                 }
                                }
               printf("Case #%d:\n",count);
               count++;
               solve();
               }
    return 0;
}
