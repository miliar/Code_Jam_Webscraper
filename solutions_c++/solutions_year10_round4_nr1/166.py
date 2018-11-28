#include <cstdio>
#include <cstring>

using namespace std;

#define MAX 164
#define SQR(a) ((a) * (a))

void input(void);
void solve(void);

int check(int m, int r, int c, int dr, int dc, int *tmp);

int n;
int S[MAX][MAX];
int G[MAX][MAX];
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
  memset(S, 0, sizeof(S));
     
  scanf("%d", &n);
  for(int i = 1; i <= n; i++) for(int j = 1; j <= i; j++) {
    int x;
    scanf("%d", &x);
    S[i - j][j - 1] = x;
  }
  for(int i = n - 1; i >= 1; i--) for(int j = 1; j <= i; j++) {
    int x;
    scanf("%d", &x);
    S[n - j][n - i + j - 1] = x;
  }
}

void solve(void)
{
  /*
  printf("\n");
  for(int i = 0; i < n; i++) {
    for(int j = 0; j  < n; j++) printf("%d ", S[i][j]);
    printf("\n");
  }
  */
  
  
  int m;
  int tmp[2 * MAX];
  for(m = n; ; m++) {
    int found = 0;
    for(int r = 0; r + n <= m; r++) for(int c = 0; c + n <= m; c++) {
      if(found) break;
      memset(G, -1, sizeof(G));
      for(int i = 0; i < n; i++) for(int j = 0; j < n; j++) G[i + r][j + c] = S[i][j];
      int good = 1;
      for(int i = 0; i < m; i++) {
        if(!check(m, i, 0, +1, +1, tmp)) { good = 0; break; }
        if(!check(m, i, 0, -1, +1, tmp)) { good = 0; break; }
      }
      if(!good) continue;
      for(int j = 0; j < m; j++) {
        if(!check(m, 0, j, +1, +1, tmp)) { good = 0; break; }
        if(!check(m, m - 1, j, -1, +1, tmp)) { good = 0; break; }
      }
      if(!good) continue;
      found = 1;
      break;
    }
    if(found) break;
  }
  
  printf("Case #%d: %d\n", case_cnt++, SQR(m) - SQR(n));
}

int check(int m, int r, int c, int dr, int dc, int *tmp)
{
  int len = 0;
  for( ; ; ) {
    if(r < 0 || r >= m || c < 0 || c >= m) break;
    tmp[len++] = G[r][c];
    r += dr;
    c += dc;
  }
  
  for(int i = 0; i < len; i++) {
    int j = len - i - 1;
    if(tmp[i] == -1 && tmp[j] == -1) continue;
    if(tmp[i] == -1 && tmp[j] != -1) { tmp[i] = tmp[j]; continue; }
    if(tmp[i] != -1 && tmp[j] == -1) { tmp[j] = tmp[i]; continue; }
    if(tmp[i] != tmp[j]) return 0;
  }
    
  return 1;
}


