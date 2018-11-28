#include <iostream>
#include <vector>
#include <algorithm>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cmath>
#include <string>
#include <map>
#include <set>
#include <bitset>
#include <iomanip>
using namespace std;

#define mem(a,b) (memset(a,b,sizeof(a)));
#define two(x) ((1)<<(x))
#define REP(x) for(int i=0;i<x;i++)
#define IREP(i,x) for(int i=0;i<x;i++)
#define SIZE(x) ((int)(x).size())
#define MP(x,y) make_pair(x,y)
#define rint(x) scanf("%d",&x)
#define rdbl(x) scanf("%lf",&x)
#define OUT(x) (cout << #x << " = " << x << endl)
typedef pair<int,int> PI;
typedef long long LL;
typedef vector<int> VI;
typedef vector<vector<int> > VII;
template<class T>T sqr(T a){return a*a;}
template<class T>T gcd(T a,T b){return b==0?a:gcd(b,a%b);}
template<class T>inline bool checkmax(T&a,const T&b){return a<b?a=b,1:0;}
template<class T>inline bool checkmin(T&a,const T&b){return a>b?a=b,1:0;}
template<class T> void checkmod(T& a,T m){ a=(a%m+m)%m;}
template<class T>T dis(T x1,T y1,T x2,T y2){return sqrt(sqr(x1-x2)+sqr(y1-y2));}
int lowbit(int x){return x&(-x);}
template<class T>void printbit(T a){cout<<bitset<17>(a)<<endl;}

int dx[]={-1,0,0,1};
int dy[]={0,-1,1,0};

const int VMAX=200;
int G[VMAX][VMAX];
int rcnt,ccnt;
char A[VMAX][VMAX];
int color[VMAX][VMAX];
char mark;
const int WHITE=0;
const int GRAY=1;

int valid(int x,int y){
       if(x>=0 && x<rcnt && y>=0 && y<ccnt)return 1;
       return 0;
}

void dfs(int x,int y){
       color[x][y]=GRAY;
       int nx=-1,ny=-1;
       int val=G[x][y];
       for(int d=0;d<4;d++){
              int xx=x+dx[d];
              int yy=y+dy[d];
              if(valid(xx,yy)==0)continue;
              if(checkmin(val,G[xx][yy])){
                     nx=xx;ny=yy;
              }
       }
       if(nx==-1 && ny==-1){
              A[x][y]=mark++;
       }else if(color[nx][ny]==GRAY){
              A[x][y]=A[nx][ny];
       }else if(color[nx][ny]==WHITE){
              dfs(nx,ny);
              A[x][y]=A[nx][ny];
       }
}

void dfs(){
       mark='a';
       for(int x=0;x<rcnt;x++){
              for(int y=0;y<ccnt;y++){
                     if(color[x][y]==WHITE){
                            dfs(x,y);
                     }
              }
       }
}

void init(){
       mem(G,0);
       mem(A,0);
       mem(color,0);
}

void input(){
       scanf("%d",&rcnt);
       scanf("%d",&ccnt);
       for(int i=0;i<rcnt;i++){
              for(int j=0;j<ccnt;j++){
                     scanf("%d",&G[i][j]);
              }
       }
}

void output(){
       static int t=0;
       t++;
       printf("Case #%d:",t);puts("");//debug
       for(int i=0;i<rcnt;i++){
              for(int j=0;j<ccnt;j++){
                     if(j!=0)printf(" ");
                     printf("%c",A[i][j]);
              }
              puts("");//debug
       }
}

int main(){
//       freopen("in.txt","r",stdin);
//       freopen("B-small.in","r",stdin);
//       freopen("out.txt","w",stdout);
       int go;
       scanf("%d",&go);
       while(go--){
              init();
              input();
              dfs();
              output();
       }
	return 0;
}
