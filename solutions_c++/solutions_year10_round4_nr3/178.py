#include <cstdio>
#include <cstring>

using namespace std;

#define MAX 256

void input(void);
void solve(void);

int B[MAX][MAX];
int T[MAX][MAX];
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
  int n;
  scanf("%d", &n);
  memset(B, 0, sizeof(B));
  for(int i = 0; i < n; i++) {
    int x1, y1, x2, y2;
    scanf("%d %d %d %d", &x1, &y1, &x2, &y2);
    for(int x = x1; x <= x2; x++)
      for(int y = y1; y <= y2; y++) B[x][y] = 1;
  }
}

void solve(void)
{
  int t = 0;
  for( ; ; ) {
    /*
    printf("\n");
    for(int i = 0; i < 10; i++) {
      for(int j = 0; j < 10; j++) printf("%d", B[j][i]);
      printf("\n");
    }*/
       
    t++;
    int found = 0;
    memset(T, 0, sizeof(T));
    for(int i = 0; i < MAX; i++) for(int j = 0; j < MAX; j++) {
      if(i > 0 && j > 0 && B[i][j - 1] && B[i - 1][j]) { T[i][j] = 1; found = 1; continue; }
      if(i > 0 && B[i][j] && B[i - 1][j]) { T[i][j] = 1; found = 1; continue; }
      if(j > 0 && B[i][j] && B[i][j - 1]) { T[i][j] = 1; found = 1; continue; }
    }
    for(int i = 0; i < MAX; i++) for(int j = 0; j < MAX; j++) B[i][j] = T[i][j];
    if(!found) break;
  }
  
  printf("Case #%d: %d\n", case_cnt++, t);
}



