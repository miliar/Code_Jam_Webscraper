#include <iostream>
#include <cstdio>
using namespace std;

const int maxn=100;
int n;
int t;
int na,nb;
int ansa, ansb;
int arr[300], dep[300]; 
int nx, ny, g[300][300], sy[300], cx[300], cy[300];

void init() {
  int t1,t2,t3,t4;
  scanf("%d\n", &t);
  scanf("%d %d\n", &na, &nb);
  for (int i=1; i<=na; ++i) {
    scanf("%d:%d %d:%d\n", &t1, &t2, &t3, &t4);
    arr[i] = t1*60+t2;
    dep[i] = t3*60+t4;
  }
  for (int i=1; i<=nb; ++i) {
    scanf("%d:%d %d:%d\n", &t1, &t2, &t3, &t4);
    arr[i+na] = t1*60+t2;
    dep[i+na] = t3*60+t4;
  }
  nx = ny = na + nb;
  /*
  for (int i=1; i<=nx; ++i) {
    cout<<arr[i]<<" "<<dep[i]<<endl;
  }
  */
  memset(g, 0, sizeof(g));
  for (int i=1; i<=na; ++i) {
    for (int j=1; j<=nb; ++j) {
      if (dep[i]+t<=arr[na+j]) g[i][na+j]=1;
      if (dep[na+j]+t<=arr[i]) g[na+j][i]=1;
    }
  }
  /*
  for (int i=1; i<=nx; ++i) {
    for (int j=1; j<=ny; ++j) cout<<g[i][j]<<" ";
    cout<<endl;
  }
  */
}

int path(int u) {
  for (int v=1; v<=ny; ++v) if (g[u][v] && !sy[v]) {
    sy[v] = 1;
    if (!cy[v] || path(cy[v])) {
      cx[u] = v; cy[v] = u; return 1;
    }
  }
  return 0;
}

void match() {
  int ret = 0;
  memset(cx, 0, sizeof(cx));
  memset(cy, 0, sizeof(cy));
  for (int i=1; i<=nx; ++i) if (!cx[i]) {
    memset(sy, 0, sizeof(sy));
    ret+=path(i);
  }
  /*
  for (int i=1; i<=nx; ++i) {
    cout<<cx[i]<<" ";
  }
  cout<<endl;*/
  //cout<<"finish matching"<<endl;
  ansa = na;
  ansb = nb;
  for (int i=1; i<=na; ++i) if (cx[i]>0) --ansb;
  for (int i=1; i<=nb; ++i) if (cx[na+i]>0) --ansa;
}

int main() {
  scanf("%d\n", &n);
  for (int kase = 1; kase <= n; ++kase) {
    init();
    //cout<<"ok1"<<endl;
    match();
    //cout<<"ok2"<<endl;
    printf("Case #%d: %d %d\n", kase, ansa, ansb);
  }
  return 0;
}
