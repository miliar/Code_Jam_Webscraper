#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;
const int INF = 1000000000;

int rx[]={0,-1,1,0};
int ry[]={-1,0,0,1};
int iler = 4;

const int M = 101;

int a[M][M];
int m, n;

inline bool isSink(int y, int x) {
  bool ret = true;
  if(x>1 && a[y][x-1]<a[y][x]) ret=false;
  if(x<n && a[y][x+1]<a[y][x]) ret=false;
  if(y>1 && a[y-1][x]<a[y][x]) ret=false;
  if(y<m && a[y+1][x]<a[y][x]) ret=false;
  return ret;
}

inline bool ins(int y, int x) {
  return 1<=x && x<=n && 1<=y && y<=m;
}

inline pair<int,int> find(int y, int x) {
  int val=INF;
  for(int i=0;i<iler;++i) {
    int nx=x+rx[i], ny=y+ry[i];
    if(!ins(ny,nx)) continue;
    val=min(val,a[ny][nx]);
  }
  for(int i=0;i<iler;++i) {
    int nx=x+rx[i], ny=y+ry[i];
    if(!ins(ny,nx)) continue;
    if(a[ny][nx]==val) return make_pair(ny,nx);
  }
}

bool vis[M][M];

char cur;

char result[M][M];

vector<int> krawx[M][M];
vector<int> krawy[M][M];

inline void dfs(int y,int x) {
  vis[y][x]=true;
  result[y][x]=cur;
  for(int i=0;i<krawx[y][x].size();++i) {
    int a=krawx[y][x][i], b=krawy[y][x][i];
    if(!vis[b][a]) dfs(b,a);
  }
}

int main() {
  int cases;
  scanf("%d", &cases);
  for(int z=1; z<=cases; ++z) {
    scanf("%d %d", &m, &n);
    for(int i=1;i<=m;++i)
      for(int j=1;j<=n;++j) {
        scanf("%d",&a[i][j]);
        krawx[i][j].clear();
        krawy[i][j].clear();
        vis[i][j]=false;
      }
    for(int i=1;i<=m;++i) {
      for(int j=1;j<=n;++j) {
        if(!isSink(i,j)) {
          pair<int,int> p=find(i,j);
          krawy[i][j].push_back(p.first);
          krawy[p.first][p.second].push_back(i);
          krawx[i][j].push_back(p.second);
          krawx[p.first][p.second].push_back(j);
        }
      }
    }
/*    for(int i=1;i<=m;++i) {
      for(int j=1;j<=n;++j) {
        printf("[%d][%d]: ",i,j);
        for(int k=0;k<krawx[i][j].size();++k)
          printf("[%d][%d] ",krawy[i][j][k], krawx[i][j][k]);
        printf("\n");
      }
    }*/
    cur='a'-1;
    for(int i=1;i<=m;++i) {
      for(int j=1;j<=n;++j) {
        if(!vis[i][j]) {
          ++cur;
          dfs(i,j);
        }
      }
    }
    printf("Case #%d:\n",z);
    for(int i=1;i<=m;++i) {
      for(int j=1;j<=n;++j)
        printf("%c ", result[i][j]);
      printf("\n");
    }
  }
  return 0;
}
