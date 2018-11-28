#include <cstdio>

using namespace std;

#define ABS(a) (((a) < (0)) ? (-(a)) : (a))

void input(void);
void solve(void);

int n, m, A;
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
  scanf("%d %d %d", &n, &m, &A);
}

void solve(void)
{
  int x_0, y_0;
  int x_1, y_1;
  int x_2, y_2;
  int area;
  
  x_0 = 0;
  y_1 = 0;
  for(y_0 = 0; y_0 <= m; y_0++)
  for(x_1 = 0; x_1 <= n; x_1++) 
  for(x_2 = 0; x_2 <= n; x_2++)
  for(y_2 = 0; y_2 <= m; y_2++) {
    area = x_0 * y_1 - x_1 * y_0 +
           x_1 * y_2 - x_2 * y_1 +
           x_2 * y_0 - x_0 * y_2;
    area = ABS(area);
    if(area == A) {
      printf("Case #%d: %d %d %d %d %d %d\n", case_cnt++, x_0, y_0, x_1, y_1, x_2, y_2);
      return;
    }
  }
  printf("Case #%d: IMPOSSIBLE\n", case_cnt++);
}

