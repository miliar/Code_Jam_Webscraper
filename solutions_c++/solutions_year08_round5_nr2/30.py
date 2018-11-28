#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <set>
#include <map>
#include <queue>
#include <vector>
using namespace std;

#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,a,b) for(int i=(a);i<=(b);++i)
#define FORD(i,a,b) for(int i=(a);i>=(b);--i)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define LET(i,c) typeof(c) i = (c)
#define MP make_pair
#define PB push_back
#define SORT(x) sort((x).begin(),(x).end())
#define ALL(x) (x).begin(),(x).end()
#define UNIQUE(x) remove(unique((x).begin(),(x).end()),(x).end())
#define CLEAR(x,v) memset((x),(v),sizeof((x)))
#define FORS(i,x) for(int i=0;i<(int)(x).size();i++)
#define X first
#define Y second
typedef long long ent;

int m,n;

int mapa[20][20];

int dx[]={1,0,-1,0};
int dy[]={0,1,0,-1};
char vis[17][17][17][17][17][17];

pair<int,int> shoot[20][20][4];

void go(){
 cin>>m>>n;
 int sx,sy,ex=0,ey=0;
 CLEAR(mapa,0);
 REP(i,m){
  string s;cin>>s;
  REP(j,n){
   if(s[j]=='#')mapa[i][j]=1;
   if(s[j]=='O'){sx=i;sy=j;}
   if(s[j]=='X'){ex=i;ey=j;}
  }
 }
 REP(i,m)REP(j,n)if(!mapa[i][j]){
  REP(d,4){
   int x=i;int y=j;
   int nx=x,ny=y;
   do{
    nx=x;ny=y;
    x=x+dx[d];
    y=y+dy[d];
   }while(x>=0 && y>=0 && x<m && y<n && !mapa[x][y]);
   shoot[i][j][d]=MP(nx,ny);
  }
 }
 /*
 REP(d,4){
  cout<<"direccion "<<d<<" "<<dx[d]<<" "<<dy[d]<<endl;
  REP(i,m){
   REP(j,n){
    if(!mapa[i][j])cout<<shoot[i][j][d].X<<","<<shoot[i][j][d].Y<<" ";
    else cout<<"#,# ";
   }
   cout<<endl;
  }
 }*/
 queue<int> q[300];
 q[0].push(sx);
 q[0].push(sy);
 q[0].push(16);
 q[0].push(16);
 q[0].push(16);
 q[0].push(16);
 q[0].push(0);
 CLEAR(vis,0);
 int res=-1;
 int disac=0;
 while(disac<300 && res==-1){
  if(q[disac].empty()){disac++;continue;}
  int x=q[disac].front();q[disac].pop();
  int y=q[disac].front();q[disac].pop();
  int ax=q[disac].front();q[disac].pop();
  int ay=q[disac].front();q[disac].pop();
  int bx=q[disac].front();q[disac].pop();
  int by=q[disac].front();q[disac].pop();
  int dis=q[disac].front();q[disac].pop();
//  cout<<x<<" "<<y<<" "<<ax<<" "<<ay<<" "<<bx<<" "<<by<<" "<<dis<<endl;
  vis[x][y][ax][ay][bx][by]=1;
// cout<<"muevo"<<endl;
  //muevo
  REP(d,4){
   int nx=x+dx[d];
   int ny=y+dy[d];
   if(nx>=0 && ny>=0 && nx<m && ny<n && !mapa[nx][ny]){
    if(!vis[nx][ny][ax][ay][bx][by]){
     if(nx==ex && ny==ey){
      res=dis+1;
     }
     vis[nx][ny][ax][ay][bx][by]=1;
     q[disac+1].push(nx);
     q[disac+1].push(ny);
     q[disac+1].push(ax);
     q[disac+1].push(ay);
     q[disac+1].push(bx);
     q[disac+1].push(by);
     q[disac+1].push(dis+1);
    }
   }
  }
 // cout<<"disparo"<<endl;
  //disparo
  REP(i,4){
   int cx=shoot[x][y][i].X;
   int cy=shoot[x][y][i].Y;
//   cout<<"cx,cy "<<cx<<","<<cy<<endl;
   if(1 || ((ax!=cx || ay!=cy) && (bx!=cx || by!=cy))){
    if(!vis[x][y][cx][cy][bx][by]){
     vis[x][y][cx][cy][bx][by]=1;
     q[disac].push(x);
     q[disac].push(y);
     q[disac].push(cx);
     q[disac].push(cy);
     q[disac].push(bx);
     q[disac].push(by);
     q[disac].push(dis);
    }
    if(!vis[x][y][ax][ay][cx][cy]){
     vis[x][y][ax][ay][cx][cy]=1;
     q[disac].push(x);
     q[disac].push(y);
     q[disac].push(ax);
     q[disac].push(ay);
     q[disac].push(cx);
     q[disac].push(cy);
     q[disac].push(dis);
    }
   }
  }
  //tunel
//  cout<<"tunel"<<endl;
  if(ax!=16 && ax==x && ay==y){
   if(!vis[bx][by][ax][ay][bx][by]){
    if(bx==ex && by==ey){
     res=dis+1;
    }
    vis[bx][by][ax][ay][bx][by]=1;
    q[disac+1].push(bx);
    q[disac+1].push(by);
    q[disac+1].push(ax);
    q[disac+1].push(ay);
    q[disac+1].push(bx);
    q[disac+1].push(by);
    q[disac+1].push(dis+1);
   }
  }
  if(bx!=16 && bx==x && by==y){
   if(!vis[ax][ay][ax][ay][bx][by]){
    if(ax==ex && ay==ey){
     res=dis+1;
    }
    vis[ax][ay][ax][ay][bx][by]=1;
    q[disac+1].push(ax);
    q[disac+1].push(ay);
    q[disac+1].push(ax);
    q[disac+1].push(ay);
    q[disac+1].push(bx);
    q[disac+1].push(by);
    q[disac+1].push(dis+1);
   }
  } 
 }
 if(res==-1)cout<<"THE CAKE IS A LIE"<<endl;
 else cout<<res<<endl;
}

int main(){
int nc;cin>>nc;int ic=1;
while(nc--){
 cout<<"Case #"<<ic++<<": ";
 go();
}
return 0;
}
