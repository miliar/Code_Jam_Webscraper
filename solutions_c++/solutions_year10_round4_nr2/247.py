#include<stdio.h>
#include<string>
#include<stdlib.h>
#include<iostream>
#include<string.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
typedef long long LL;
const double EPS = 1e-8;
const int INF = (1<<29);

int a[2000],f[5000][20],n,m,w[5000];

int run(int d,int p,int miss){
  if (f[p][miss]!=-1) return f[p][miss];
  int x=p-(1<<m)+1;
  if (d==m){
//    printf(">> %d %d\n",p,x);
    if (miss>a[x]) return f[p][miss]=INF;
    return f[p][miss]=0;
  }
  int y1=p*2+1, y2=p*2+2;

  int aa1 = run(d+1,y1,miss+1);
  int aa2 = run(d+1,y2,miss+1);
  int ans=INF;
  if (aa1!=INF && aa2!=INF) ans=aa1+aa2;
  int bb1 = run(d+1,y1,miss);
  int bb2 = run(d+1,y2,miss);
  if (bb1!=INF && bb2!=INF) ans=min(bb1+bb2+w[p], ans);

//  int ans = min(run(d+1,y1,miss+1)+run(d+1,y2,miss+1), 
 //               run(d+1,y1,miss)+run(d+1,y2,miss)+w[p]);;
  return f[0][miss]=ans;
}

int main(){
  int ca; scanf("%d",&ca);
  for (int tt=1; tt<=ca; tt++){
    scanf("%d",&m);
    n = 1<<m;
    int ans=INF;
    for (int i=0; i<n; i++) scanf("%d",&a[i]);
    for (int i=m-1; i>=0; i--){
      for (int j=0; j<(1<<i); j++){
        scanf("%d",&w[(1<<i)+j-1]);
      }
    }
    memset(f,-1,sizeof(f));
    ans = min(ans,run(0,0,0));
    printf("Case #%d: %d\n",tt,ans);
  }
  return 0;
}
