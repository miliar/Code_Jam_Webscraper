#include<vector>
#include<queue>
#include<algorithm>
#include<map>
#include<set>
#include<sstream>
#include<iostream>
#include<cstdlib>
#include<cstdio>
#include<cmath>
using namespace std;
int n;
int m;
int e[5000];
bool x[5000];
int y[5000];
vector<vector<int> > g;
void addedge(int f,int t){
  if(t>=n && t<n+m){
    y[t]++;
  }
  g[f].push_back(t);
}
void solve(){
  scanf("%d",&n);
  scanf("%d",&m);
  for(int i=0;i<n+m;i++){
    x[i]=0;
  }
  for(int i=0;i<n;i++){
    y[i]=1;
  }
  y[n+m]=1;
  g.clear();
  g.resize(n+m,vector<int>());
  for(int i=0;i<m;i++){
    int t;
    scanf("%d",&t);
    int mt=-1;
    y[n+i]=0;
    for(int j=0;j<t;j++){
      int a,b;
      scanf("%d %d",&a,&b);
      a--;
      if(b==1){//malted
        mt=a;
        addedge(n+i,a);
      }else{
        addedge(a,n+i);
      }
    }
    if(mt<0){
      addedge(n+i,n+m);
    }
  }
  queue<int> q;
  for(int i=n;i<n+m;i++){
    if(!y[i]){
      q.push(i);
      x[i]=1;
    }
  }
  while(!q.empty()){
    int id=q.front();
    q.pop();
    if(id==n+m){
      puts("IMPOSSIBLE");
      return;
    }
    for(int j=g[id].size();j--;){
      int k=g[id][j];
      if(!--y[k]){
        q.push(k);
        x[k]=1;
      }
    }
  }
  for(int i=0;i<n;i++){
    printf("%d%c",x[i],i==n-1?'\n':' ');
  }
}
int main(){
  int n;
  scanf(" %d ",&n);
  for(int t=1;t<=n;t++){
    printf("Case #%d: ",t);
    solve();
  }
}
