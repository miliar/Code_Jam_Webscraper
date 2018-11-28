#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <math.h>
#include <vector>
#include <string>
#include <queue>
#include <iostream>
#define INF 1<<28
using namespace std;

bool fless(double a,double b){ return b-a>1e-6; }
bool fequal(double a,double b){ return fabs(b-a)<=1e-6; }

int main(){
  int tt; scanf("%d",&tt);
  for (int ti=1;ti<=tt;ti++){
    int ans = 0;
    int D,I,m,n;
    scanf("%d%d%d%d",&D,&I,&m,&n);
    int a[n];
    int d[n][256];
    bool vis[n][256];
    memset(vis,0,sizeof(vis));
    for (int i=0;i<n;i++){
      scanf("%d",&a[i]);
    }
    for (int i=0;i<n;i++){
      for (int j=0;j<256;j++){
        d[i][j]=INF;
      }
    }
    d[0][a[0]] = 0;
    priority_queue<pair<int,int> >q;
    for (int i=0;i<256;i++){
      d[0][i] = abs(i-a[0]);
      q.push(make_pair(-d[0][i], i));
    }
    for (int i=1;i<n;i++){
      if (d[i][a[i]] > D*i){
        d[i][a[i]] = d[i][a[i]] = D*i;
        q.push(make_pair(-d[i][a[i]], i*256+a[i]));
      }
    }
    
    while (!q.empty()){
      int x = q.top().second/256, y = q.top().second%256;
      q.pop();
      if (vis[x][y])continue;
      vis[x][y] = true;
      //printf("%d %d: %d\n",x,y,d[x][y]);
      if (x==n-1){
        ans = d[x][y];
        break;
      }
      for (int i=-m;i<=m;i++){
        int p = y+i;
        if (p<0 || p>=256)continue;
        //printf("p %d\n",p);
        //insert p after x
        if (d[x][p]>d[x][y]+I){
          d[x][p]=d[x][y]+I;
          q.push(make_pair(-d[x][p], x*256+p));
          //printf("insert %d %d\n",x,p);
        }
        //change x+1 to p
        if (d[x+1][p]>d[x][y]+abs(p-a[x+1])){
          d[x+1][p]=d[x][y]+abs(p-a[x+1]);
          q.push(make_pair(-d[x+1][p], (x+1)*256+p));
          //printf("change %d %d\n",x+1,p);
        }
      }
      //delete x+1
      if (x<n-1 && d[x+1][y] > d[x][y]+D){
        d[x+1][y] = d[x][y]+D;
        q.push(make_pair(-d[x+1][y], ((x+1)*256)+y));
        //printf("delete %d %d\n",x+1,y);
      }
      //extend
      if (x<n-1 && abs(y-a[x+1])<=m){
        d[x+1][a[x+1]] = d[x][y];
        q.push(make_pair(-d[x+1][a[x+1]], (x+1)*256+a[x+1]));
        //printf("extend %d %d\n",x+1,a[x+1]);
      }
    }

    
    printf("Case #%d: %d\n",ti, ans);
  }
  return 0;
}
