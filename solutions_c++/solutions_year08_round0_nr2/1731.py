#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include <algorithm>
#include <set>

using namespace std;

#define PROBLEM "b"
#define INFTY 0x3F3F3F3F

typedef long long i64;
typedef unsigned long long u64;

#define MAX 110

struct trip {
  int start;
  int end;
};

int n;

trip trips[2][MAX];

char a[MAX+MAX][MAX+MAX];

char used[MAX+MAX];
char was[MAX+MAX];
char pares[MAX+MAX];

int go(int v) {
  was[v]=1;
  for(int u=0;u<n;++u) {
    if(a[v][u]) {
      if(pares[u]<0 || (!was[pares[u]] && go(pares[u]))) {
        pares[u]=v;
        used[v]=1;
        return 1;
      }
    }
  }
  return 0;
}


int main() {
  freopen(PROBLEM".in","r",stdin);
  freopen(PROBLEM".out","w",stdout);
  int tst_num;
  scanf("%d",&tst_num);
  for(int tst=1;tst<=tst_num;++tst) {
    int T,NA,NB,i,j,k;
    scanf("%d%d%d",&T,&NA,&NB);
    for(i=0;i<NA;++i) {
      int h,m;
      scanf("%d:%d",&h,&m);
      trips[0][i].start=h*60+m;
      scanf("%d:%d",&h,&m);
      trips[0][i].end=h*60+m;
    }
    for(i=0;i<NB;++i) {
      int h,m;
      scanf("%d:%d",&h,&m);
      trips[1][i].start=h*60+m;
      scanf("%d:%d",&h,&m);
      trips[1][i].end=h*60+m;
    }
    n=NA+NB;

    memset(a,0,sizeof(a));
    for(i=0;i<NA;++i)
      for(j=0;j<NB;++j) {
        if(trips[0][i].end+T<=trips[1][j].start) {
          a[i][j+NA]=1;
        }
        if(trips[1][j].end+T<=trips[0][i].start) {
          a[j+NA][i]=1;
        }
      }
    memset(used,0,sizeof(used));
    memset(pares,0xFF,sizeof(pares));
    for(i=0;i<n;++i)
      if(!used[i]) {
        memset(was,0,sizeof(was));
        go(i);
      }
    int ans[2];
    ans[0]=ans[1]=0;
    for(i=0;i<n;++i) {
      if(pares[i]<0) {
        ++ans[i>=NA];
      }
    }
    printf("Case #%d: %d %d\n",tst,ans[0],ans[1]);
  }

  return 0;
}
