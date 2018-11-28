#include <cstdio>
#include <cstring>

int dirs[4][2] = {{-1,0},{0,-1},{0,1},{1,0}};

const int MAX = 128;

int n, m;
int hei[MAX][MAX];
char ans[MAX][MAX];
int nxt[MAX][MAX];

inline int good(int x, int y){
  return ((x>=0) && (x<n) && (y>=0) && (y<m));
}

void gen_nxt(){
  int i, j, dir;
  for (i=0; i<n; i++){
    for (j=0; j<m; j++){
      int cmin = hei[i][j];
      nxt[i][j] = -1;
      for (dir=0; dir<4; dir++){
        int ni = i + dirs[dir][0];
        int nj = j + dirs[dir][1];
        if (good(ni,nj) && hei[ni][nj] < cmin){
          cmin = hei[ni][nj];
          nxt[i][j] = dir;
        }
      }
      //printf("%d ", nxt[i][j]);
    }
  }
}

void dfs(int x, int y, char c){
  ans[x][y] = c;
  int dir;
  for (dir=0; dir<4; dir++){
    int nx = x - dirs[dir][0];
    int ny = y - dirs[dir][1];
    if (good(nx,ny) && nxt[nx][ny]==dir && !ans[nx][ny]){
      dfs(nx, ny, c);
    }
  }
  if (nxt[x][y]==-1) return;
  int nx = x + dirs[nxt[x][y]][0];
  int ny = y + dirs[nxt[x][y]][1];
  if (!ans[nx][ny]){
    dfs(nx, ny, c);
  }
}

int main(){
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int tn, t;
  scanf("%d", &tn);
  for (t=1; t<=tn; t++){
    scanf("%d%d", &n, &m);
    int i, j;
    for (i=0; i<n; i++){
      for (j=0; j<m; j++){
        scanf("%d", &hei[i][j]);
      }
    }
    gen_nxt();
    memset(ans, 0, sizeof(ans));
    char clet = 'a';
    for (i=0; i<n; i++){
      for (j=0; j<m; j++){
        if (!ans[i][j]){
          dfs(i, j, clet);
          clet++;
        }
      } 
    }
    printf("Case #%d:\n", t);
    for (i=0; i<n; i++){
      for (j=0; j<m; j++){
        printf("%c", ans[i][j]);
        if (j<m-1) printf(" ");
      }
      printf("\n");
    }
  }
  return 0;
}
