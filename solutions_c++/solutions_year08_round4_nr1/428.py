#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include <algorithm>

#define PROBLEM "a"

typedef long long i64;
typedef unsigned long long u64;

#define MAX 20010
#define INFTY 0x3F3F3F3F

char nodes[MAX];
char can[MAX];
int dp[MAX][2];
int n,m;

inline int min(int a,int b) {
  if(a<b) return a;
  return b;
}

void calc(int v) {
  if(v>m) {
    dp[v][nodes[v]]=0;
    return;
  }
  int l=v<<1;
  int r=l+1;
  calc(l);
  calc(r);
  if(nodes[v]) {
    dp[v][0]=min(dp[v][0],dp[l][0]+dp[r][0]);
    dp[v][0]=min(dp[v][0],dp[l][0]+dp[r][1]);
    dp[v][0]=min(dp[v][0],dp[l][1]+dp[r][0]);
    dp[v][1]=min(dp[v][1],dp[l][1]+dp[r][1]);
    if(can[v]) {
      dp[v][0]=min(dp[v][0],1+dp[l][0]+dp[r][0]);
      dp[v][1]=min(dp[v][1],1+dp[l][0]+dp[r][1]);
      dp[v][1]=min(dp[v][1],1+dp[l][1]+dp[r][0]);
      dp[v][1]=min(dp[v][1],1+dp[l][1]+dp[r][1]);
    }
  }
  else {
    dp[v][0]=min(dp[v][0],dp[l][0]+dp[r][0]);
    dp[v][1]=min(dp[v][1],dp[l][0]+dp[r][1]);
    dp[v][1]=min(dp[v][1],dp[l][1]+dp[r][0]);
    dp[v][1]=min(dp[v][1],dp[l][1]+dp[r][1]);
    if(can[v]) {
      dp[v][0]=min(dp[v][0],1+dp[l][0]+dp[r][0]);
      dp[v][0]=min(dp[v][0],1+dp[l][0]+dp[r][1]);
      dp[v][0]=min(dp[v][0],1+dp[l][1]+dp[r][0]);
      dp[v][1]=min(dp[v][1],1+dp[l][1]+dp[r][1]);
    }
  }
}

int main() {
  freopen(PROBLEM".in","r",stdin);
  freopen(PROBLEM".out","w",stdout);
  int tst_num;
  scanf("%d",&tst_num);
  for(int tst=1;tst<=tst_num;++tst) {
    int i,j,k,l,x;
    scanf("%d%d",&n,&x);
    m=((n-1)>>1);
    for(i=1;i<=m;++i) {
      int G,C;
      scanf("%d%d",&G,&C);
      nodes[i]=G;
      can[i]=C;
    }
    for(;i<=n;++i) {
      scanf("%d",&nodes[i]);
    }
    memset(dp,0x3F,sizeof(dp));
    calc(1);
    printf("Case #%d: ",tst);
    if(dp[1][x]<INFTY) printf("%d\n",dp[1][x]);
    else printf("IMPOSSIBLE\n");

  }

  return 0;
}
