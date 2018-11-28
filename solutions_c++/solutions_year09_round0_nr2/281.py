#include <stdio.h>
#include <string.h>

#define MAX 110

int map[MAX][MAX];
int sink[MAX][MAX];
char basins[MAX][MAX];
int sinks;

int dir[4][2]={{-1,0},{0,-1},{0,1},{1,0}};

void dfs(int x,int y) {
  int min_alt=1000000000;
  int nx=0,ny=0;
  int is_sink=1;
  for(int k=0;k<4;++k) {
    int xx=x+dir[k][0];
    int yy=y+dir[k][1];
    if(map[xx][yy]<0 || map[xx][yy]>=map[x][y]) continue;
    if(map[xx][yy]<min_alt) {
      min_alt=map[xx][yy];
      nx=xx; ny=yy;
      is_sink=0;
    }
  }
  if(is_sink) {
    sink[x][y]=sinks++;
  }
  else {
    if(sink[nx][ny]<0)
      dfs(nx,ny);
    sink[x][y]=sink[nx][ny];
  }
}

int h,w;

inline void paint(int sink,char mark) {
  for(int i=1;i<=h;++i)
    for(int j=1;j<=w;++j)
      if(::sink[i][j]==sink) {
        basins[i][j]=mark;
      }
}

int main() {
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);
  int tests;
  scanf("%d",&tests);
  for(int test=1;test<=tests;++test) {
    scanf("%d%d",&h,&w);
    memset(map,0xFF,sizeof(map));
    for(int i=1;i<=h;++i)
      for(int j=1;j<=w;++j)
        scanf("%d",&map[i][j]);
    sinks=0;
    memset(sink,0xFF,sizeof(sink));
    for(int x=1;x<=h;++x)
      for(int y=1;y<=w;++y)
        if(sink[x][y]<0)
          dfs(x,y);
    memset(basins,0,sizeof(basins));
    char mark='a';
    for(int x=1;x<=h;++x)
      for(int y=1;y<=w;++y)
        if(!basins[x][y]) {
          paint(sink[x][y],mark++);
        }
    printf("Case #%d:\n",test);
    for(int i=1;i<=h;++i) {
      for(int j=1;j<=w;++j)
        printf("%c ",basins[i][j]);
      printf("\n");
    }
  }
  return 0;
}
