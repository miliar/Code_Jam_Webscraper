#include <cstdio>
#include <vector>
#include <utility>
#include <memory.h>
using namespace std;
const int dx[4]={-1,0,0,1};
const int dy[4]={0,-1,1,0};
int t,tt,i,j,k,x,y,xx,yy,n,m,a[110][110];
vector <pair <int, int> > g[110][110];
char b[110][110],c;
bool e;
void dfs(int x, int y) {
   if (b[x][y]!=0) return; else b[x][y]=c;
   for (int i=0; i<g[x][y].size(); i++) dfs(g[x][y][i].first,g[x][y][i].second);
}
int main() {
   freopen("Bl.in","r",stdin);
   freopen("Bl.out","w",stdout);
   scanf("%d",&t);
   for (tt=0; tt<t; tt++) {
      scanf("%d%d",&n,&m);
      memset(a,100,sizeof(a));
      for (i=1; i<=n; i++) for (j=1; j<=m; j++) {
         scanf("%d",&a[i][j]); g[i][j].clear();
      }
      for (i=1; i<=n; i++) for (j=1; j<=m; j++) {
         e=true;
         for (k=0; k<4; k++) {
            x=i+dx[k];
            y=j+dy[k];
            if (a[x][y]<a[i][j]) if (e || a[x][y]<a[xx][yy]) {
               xx=x; yy=y; e=false;
            }
         }
         if (!e) {
            g[i][j].push_back(make_pair(xx,yy));
            g[xx][yy].push_back(make_pair(i,j));
         }
      }
      memset(b,0,sizeof(b)); c='a';
      for (i=1; i<=n; i++) for (j=1; j<=m; j++) if (b[i][j]==0) { dfs(i,j); c++; }
      printf("Case #%d:\n",tt+1);
      for (i=1; i<=n; i++) {
         for (j=1; j<=m; j++) printf("%c ",b[i][j]);
         putchar('\n');
      }
   }
   return 0;
}
