#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std;
typedef pair<int,int> p2;
p2 p[110][110];
p2 find(int x,int y){/*cout<<x<<","<<y<<": "<<p[x][y].first<<","<<p[x][y].second<<endl;*/if(p[x][y]==p2(x,y))return p[x][y];return p[x][y]=find(p[x][y].first,p[x][y].second);}
void join(int x0,int y0,int x1,int y1){
  p2 a=find(x0,y0),b=find(x1,y1);
  if(a!=b)p[a.first][a.second]=b; 
}
int z[110][110];
char r[110][110];
main(){
  int t,H,W;cin>>t;for(int tt=1;tt<=t;tt++){
    cin>>H>>W;
    for(int i=0;i<H;i++)for(int j=0;j<W;j++)cin>>z[i][j],p[i][j]=p2(i,j);
    int dx[4]={-1,0,0,1},dy[4]={0,-1,1,0};
    for(int i=0;i<H;i++)for(int j=0;j<W;j++){
      int best=-1;
      for(int k=0;k<4;k++)if(i+dx[k]>=0&&i+dx[k]<H&&j+dy[k]>=0&&j+dy[k]<W&&z[i][j]>z[i+dx[k]][j+dy[k]]&&(best==-1||z[i+dx[k]][j+dy[k]]<z[i+dx[best]][j+dy[best]]))best=k;
      if(best==-1)continue;
      join(i,j,i+dx[best],j+dy[best]);
    }
    memset(r,0,sizeof(r));
    char next='a';
    cout<<"Case #"<<tt<<":"<<endl;
    for(int i=0;i<H;i++)for(int j=0;j<W;j++){
      p2 a=find(i,j);
      if(!r[a.first][a.second])r[a.first][a.second]=next++;
      printf("%c%c",r[a.first][a.second],j+1<W?' ':'\n');
    }    
  }  
}
