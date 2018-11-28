#include <cstdio>
#include <cstring>
using namespace std;

int a[110][110];
bool g[110][110];
int la[110];
int na,C,n,t;
int match[110];
bool vis[110];

bool check(int k1,int k2) {
  for (int i=1;i<=t;i++) 
    if (a[k1][i]<=a[k2][i]) return false;
  return true;
}

bool found(int k) {
  for (int i=1;i<=n;i++) {
    if (g[k][i] && !vis[i]) {
      vis[i]=true;
      int tmp=match[i];
      match[i]=k;
      if (tmp==0 || found(tmp)) return true;
      match[i]=tmp;
    }
  }
  return false;
}

int main() {
  scanf("%d",&C);
  for (int c=1;c<=C;c++) {
    scanf("%d%d",&n,&t);
    for (int i=1;i<=n;i++) 
      for (int j=1;j<=t;j++)
	scanf("%d",&a[i][j]);
    memset(g,0,sizeof(g));
    for (int i=1;i<=n;i++)
      for (int j=1;j<=n;j++) {
	if (check(j,i)) {
	  g[i][j]=true;
	  //	  printf("%d %d\n",i,j);
	}
      }
    memset(match,0,sizeof(match));
    int ans=0;
    for (int i=1;i<=n;i++) {
      memset(vis,0,sizeof(vis));
      if (found(i)) ans++;
    }
    printf("Case #%d: %d\n",c,n-ans);
  }
}
