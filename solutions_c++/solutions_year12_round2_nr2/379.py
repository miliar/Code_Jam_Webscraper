#include<cstdio>
#include<algorithm>
using namespace std;

#define maxN 102
#define INF 10000000

typedef struct v{
 int time;
 int fromx,fromy;
 bool done;
}V;

int T,N,M,H;
int F[maxN][maxN],C[maxN][maxN];
int nowx,nowy;

v ver[maxN][maxN];

int mintime(int x1,int y1,int x2,int y2,int t){
 if(C[x2][y2]<50+F[x2][y2] || C[x2][y2]<50+F[x1][y1] || C[x1][y1]<50+F[x2][y2]) return INF;
 if(t==0 && H+50<=C[x2][y2]){
  return 0;
 }
 int t2;
 t2 = max(0,H-t+50-C[x2][y2]);
//printf("(%d %d): %d,%d\n",x2,y2,t,t2);
 if(H-t-t2>=F[x1][y1]+20) return t+t2+10;
 else return t+t2+100;
}

int main(){
 int t,i,j,k;
 scanf("%d",&T);
 for(t=1;t<=T;t++){
  scanf("%d%d%d",&H,&N,&M);
  for(i=0;i<N;i++){
   for(j=0;j<M;j++){
    scanf("%d",&C[i][j]);
   }
  }
  for(i=0;i<N;i++){
   for(j=0;j<M;j++){
    scanf("%d",&F[i][j]);
    ver[i][j].time = INF;
    ver[i][j].done = 0;
   }
  }
  ver[0][0].time = 0;
  while(!ver[N-1][M-1].done){
   k = INF;
   for(i=0;i<N;i++){
    for(j=0;j<M;j++){
     if(!ver[i][j].done && ver[i][j].time<k){
      nowx=i;
      nowy=j;
      k=ver[i][j].time;
     }
    }
   }
//printf("(%d %d): %d\n",nowx,nowy,ver[nowx][nowy].time);
   ver[nowx][nowy].done = 1;
   if(nowx<N-1 && !ver[nowx+1][nowy].done){
    k = mintime(nowx,nowy,nowx+1,nowy,ver[nowx][nowy].time);
    if(k<ver[nowx+1][nowy].time){
     ver[nowx+1][nowy].time = k;
     ver[nowx+1][nowy].fromx = nowx;
     ver[nowx+1][nowy].fromy = nowy;
    }
   }
   if(nowx>0 && !ver[nowx-1][nowy].done){
    k = mintime(nowx,nowy,nowx-1,nowy,ver[nowx][nowy].time);
    if(k<ver[nowx-1][nowy].time){
     ver[nowx-1][nowy].time = k;
     ver[nowx-1][nowy].fromx = nowx;
     ver[nowx-1][nowy].fromy = nowy;
    }
   }
   if(nowy<M-1 && !ver[nowx][nowy+1].done){
    k = mintime(nowx,nowy,nowx,nowy+1,ver[nowx][nowy].time);
    if(k<ver[nowx][nowy+1].time){
     ver[nowx][nowy+1].time = k;
     ver[nowx][nowy+1].fromx = nowx;
     ver[nowx][nowy+1].fromy = nowy;
    }
   }
   if(nowy>0 && !ver[nowx][nowy-1].done){
    k = mintime(nowx,nowy,nowx,nowy-1,ver[nowx][nowy].time);
    if(k<ver[nowx][nowy-1].time){
     ver[nowx][nowy-1].time = k;
     ver[nowx][nowy-1].fromx = nowx;
     ver[nowx][nowy-1].fromy = nowy;
    }
   }
  }	//while
  printf("Case #%d: %lf\n",t,ver[N-1][M-1].time/10.0);
 }

 return 0;
}
