#include <stdio.h>
#include <string.h>
#include <stdlib.h>

#include <algorithm>

#define PROBLEM "c"

typedef long long i64;
typedef unsigned long long u64;

#define MAX 100

char boa[MAX][MAX];
char edges[MAX*MAX][6];
int pwr[MAX*MAX];
char was[MAX*MAX];
int id[MAX*MAX];

int fs,ss;
int first[MAX*MAX],second[MAX*MAX];
int pares[MAX*MAX];
char vis[MAX*MAX];
char used[MAX*MAX];

int go(int v) {
  int u,i;
  if(vis[v]) return 0;
  vis[v]=1;
  for(i=0;i<pwr[first[v]];++i) {
    u=id[edges[first[v]][i]];
    if(pares[u]>=0) {
      if(go(pares[u])) {
        pares[u]=v;
        used[v]=1;
        return 1;
      };
    }
    else {
      pares[u]=v;
      used[v]=1;
      return 1;
    };
  };
  return 0;
}


int max_match() {
  memset(pares,0xFF,sizeof(pares));
  memset(used,0,sizeof(used));
  memset(vis,0,sizeof(vis));
  for(int i=0;i<fs;++i)
    if(!used[i])
      if(go(i))
        memset(vis,0,sizeof(vis));
  int res=0;
  for(int i=0;i<ss;++i)
    if(pares[i]>=0)
      ++res;
  return res;
}

void dfs(int x,int c) {
  if(!c) {
    first[fs++]=x;
    id[x]=fs-1;
  }
  else {
    second[ss++]=x;
    id[x]=ss-1;
  }
  was[x]=1;
  for(int k=0;k<pwr[x];++k)
    if(!was[edges[x][k]]) {
      dfs(edges[x][k],c^1);
    }
}

int calc(int x) {
  fs=ss=0;
  dfs(x,0);
  int k=max_match();
  int res=fs+ss-k;
  return res;
}

int del[6][2]={{-1,-1},{-1,1},{0,-1},{0,1},{1,-1},{1,1}};

int n,m;

int main() {
  freopen(PROBLEM".in","r",stdin);
  freopen(PROBLEM".out","w",stdout);
  int tst_num;
  scanf("%d",&tst_num);
  for(int tst=1;tst<=tst_num;++tst) {
    int i,j,k;
    scanf("%d%d",&n,&m);
    memset(boa,0,sizeof(boa));
    for(i=1;i<=n;++i)
      scanf("%s",&boa[i][1]);

    memset(pwr,0,sizeof(pwr));
    for(i=0;i<n;++i)
      for(j=0;j<m;++j)
        if(boa[i+1][j+1]=='.') {
          int x=i*m+j;
          for(k=0;k<6;++k) {
            int ii=i+del[k][0];
            int jj=j+del[k][1];
            if(boa[ii+1][jj+1]=='.') {
              int y=ii*m+jj;
              edges[x][pwr[x]++]=y;
            }
          }
        }
    memset(was,0,sizeof(was));
    memset(id,0xFF,sizeof(id));
    int ans=0;
    for(i=0;i<n;++i)
      for(j=0;j<m;++j)
        if(boa[i+1][j+1]=='.' && !was[i*m+j]) {
          ans+=calc(i*m+j);
        }
    printf("Case #%d: %d\n",tst,ans);
  }

  return 0;
}
