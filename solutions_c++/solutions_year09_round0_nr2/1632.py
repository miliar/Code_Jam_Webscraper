#include <cstdio>
#include <algorithm>
#include <string>
#include <vector>
#include <iostream>
using namespace std;

const int maxn=105;
const int fx[4]={-1,0,0,1};
const int fy[4]={0,-1,1,0};
typedef struct {
  int h,t;
} node;
node a[10];
char ans[maxn][maxn];
int n,m,map[maxn][maxn],d[30];
int testcase,test,i,j;
char cnt;

bool operator < (const node &n1,const node &n2) {
  return n1.h<n2.h || n1.h==n2.h && n1.t<n2.t;
}
int dfs(int x,int y) {
  if (ans[x][y]>0) return ans[x][y];
  int p=0;
  for (int j=0; j<4; ++j)
    if (!(x+fx[j]<1 || x+fx[j]>n || y+fy[j]<1 || y+fy[j]>m)) {
      ++p;
      a[p].h=map[x+fx[j]][y+fy[j]];
      a[p].t=j;
    }
  sort(a+1,a+1+p);
  if (a[1].h<map[x][y]) ans[x][y]=dfs(x+fx[a[1].t],y+fy[a[1].t]);
  return ans[x][y];
}
int main() {
  freopen("poj.in","r",stdin);
  freopen("poj.out","w",stdout);
  scanf("%d",&testcase);
  for (test=1; test<=testcase; ++test) {
    printf("Case #%d:\n",test);
    scanf("%d%d",&n,&m);
    memset(map,10,sizeof(map));
    for (i=1; i<=n; ++i)
      for (j=1; j<=m; ++j)
        scanf("%d",&map[i][j]);
    memset(ans,0,sizeof(ans));
    cnt=1;
    for (i=1; i<=n; ++i)
      for (j=1; j<=m; ++j)
        if ((map[i-1][j]>=map[i][j]) &&
            (map[i+1][j]>=map[i][j]) &&
            (map[i][j-1]>=map[i][j]) &&
            (map[i][j+1]>=map[i][j])) {
              ans[i][j]=cnt;
              ++cnt;
            }
    for (i=1; i<=n; ++i)
      for (j=1; j<=m; ++j)
        ans[i][j]=dfs(i,j);
    memset(d,0,sizeof(d));
    cnt='a'-1;
    for (i=1; i<=n; ++i)
      for (j=1; j<=m; ++j)
        if (d[ans[i][j]]==0) d[ans[i][j]]=++cnt;
    for (i=1; i<=n; ++i) {
      for (j=1; j<m; ++j)
        printf("%c ",(char)d[ans[i][j]]);
      printf("%c\n",(char)d[ans[i][m]]);
    }
  }
  return 0;
}
              
                      
