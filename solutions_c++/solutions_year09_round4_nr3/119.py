#include <cstdio>
#include <vector>
using namespace std;
int t,tt,n,k,I,i,j,p,r,a[110][30],b[110],u[110];
vector <int> g[110];
bool q;
void dfs(int i) {
  if (i==-1) { q=true; r++; return; }
  int j,k,p;
  u[i]=I;
  for (j=0; j<g[i].size(); j++) {
    k=g[i][j]; p=b[k]; b[k]=i;
    if (p==-1 || u[p]!=I) dfs(p);
    if (q) return;
    b[k]=p;
  }
}
int main() {
  freopen("Cl.in","r",stdin);
  freopen("Cl.out","w",stdout);
  scanf("%d",&t);
  for (tt=1; tt<=t; tt++) {
    scanf("%d%d",&n,&k); r=0;
    for (i=0; i<n; i++) for (j=0; j<k; j++) scanf("%d",&a[i][j]);
    for (i=0; i<n; i++) { g[i].clear(); u[i]=b[i]=-1; }
    for (i=0; i<n; i++) for (j=0; j<n; j++) if (a[i][0]<a[j][0]) {
      q=true;
      for (p=1; p<k; p++) if (a[i][p]>=a[j][p]) q=false;
      if (q) g[i].push_back(j);
    }
    for (i=0; i<n; i++) { q=false; I=i; dfs(i); }
    printf("Case #%d: %d\n",tt,n-r);
  }
  return 0;
}
