#include <iostream>

using namespace std;

#define for_to(i,j,k) for (i=j; i<=k; ++i)

#define MAX 110

#define MAXV (MAX*MAX)

int i,j,k,u,v;
int n_tests,test;
int R,C,r,c,dir,min_r,min_c,adj,cnt;
int alt[MAX][MAX];
int g[MAXV][MAXV];
int deg[MAXV],id[MAXV];
int dr[] = {-1,0,0,+1};
int dc[] = {0,-1,+1,0};

int valid(int r,int c) {
  return 0 <= r && r < R && 0 <= c && c < C;
}

void dfs(int v) {
  int i,u;
  id[v] = cnt;
  for_to(i,0,deg[v]-1) {
    u = g[v][i];
    if (id[u] == -1)
      dfs(u);
  }
}

int main() {
  scanf("%d",&n_tests);
  for_to(test,1,n_tests) {
    scanf("%d %d",&R,&C);
    for_to(r,0,R-1) 
      for_to(c,0,C-1)
        scanf("%d",&alt[r][c]);
    for_to(v,0,R*C-1)
      deg[v] = 0;
    for_to(r,0,R-1) 
      for_to(c,0,C-1) {
        
        min_r = r;
        min_c = c;
        for_to(dir,0,3) {
          if (valid(r + dr[dir], c + dc[dir])) {
            if (alt[r + dr[dir]][c + dc[dir]] < alt[min_r][min_c]) {
              min_r = r + dr[dir];
              min_c = c + dc[dir];
            }
          }
        }
        if (min_r != r || min_c != c) {
          u = r*C + c;
          v = min_r * C + min_c;
          g[u][deg[u]++] = v;
          g[v][deg[v]++] = u;
        }
      }
    
    printf("Case #%d:\n",test);
    cnt = 0;
    for_to(v,0,R*C-1)
      id[v] = -1;
    for_to(r,0,R-1) {
      for_to(c,0,C-1) {
        v = r*C + c;
        if (id[v] == -1) {
          dfs(v);
          ++cnt;
        }
        printf("%c",'a'+id[v]);
        if (c != C-1) printf(" ");
      }
      printf("\n");
    }
      
  }
  return 0;
}