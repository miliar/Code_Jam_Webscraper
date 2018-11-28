#include <cstdio>
#include <cstring>

using namespace std;

#define MAX 128

#define index(i, j) ((i) * m + (j))

const int dx[] = { -1, 0, 0, +1 };
const int dy[] = { 0, -1, +1, 0 };

void input(void);
void solve(void);

void UF_init(void);
int  UF_find(int x);
int  UF_union(int x, int y);

int n, m;
int height[MAX][MAX];

int id[MAX * MAX];
int sz[MAX * MAX];
int color[MAX * MAX];

int case_cnt = 1;

int main(void)
{
  int t;
  scanf("%d", &t);
  while(t--) {
    input();
    solve();
  }
    
  return 0;
}

void input(void)
{
  scanf("%d %d", &n, &m);
  for(int i = 0; i < n; i++)
    for(int j = 0; j < m; j++) scanf("%d", &height[i][j]);
}

void solve(void)
{
  UF_init();
  for(int i = 0; i < n; i++)
    for(int j = 0; j < m; j++) {
      int xx = -1;
      int yy = -1;
      int best_height = height[i][j];
      for(int k = 0; k < 4; k++) {
        int x = i + dx[k];
        int y = j + dy[k];
        if(x < 0 || x >= n || y < 0 || y >= m) continue;
        if(height[x][y] >= best_height) continue;
        xx = x;
        yy = y;
        best_height = height[x][y];
      }
      if(xx == -1 && yy == -1) continue;
      UF_union(index(i, j), index(xx, yy));
    }
    
  int color_cnt = 0;
  memset(color, -1, sizeof(color));
  
  printf("Case #%d:\n", case_cnt++);
  for(int i = 0; i < n; i++) 
    for(int j = 0; j < m; j++) {
      int x = UF_find(index(i, j));
      if(color[x] == -1) color[x] = color_cnt++;
      printf("%c%c", color[x] + 'a', (j + 1 == m) ? '\n' : ' ');
    }
}

void UF_init(void)
{
  for(int i = 0; i < n * m; i++) {
    id[i] = i;
    sz[i] = 1;
  }
}

int UF_find(int x)
{
  for(x = id[x]; x != id[x]; x = id[x]) id[x] = id[id[x]];
  return x;
}

int UF_union(int x, int y)
{
  x = UF_find(x);
  y = UF_find(y);
  if(x == y) return 0;
  if(sz[x] > sz[y]) { sz[x] += sz[y]; id[y] = x; }
  else              { sz[y] += sz[x]; id[x] = y; }
  return 1;
}


