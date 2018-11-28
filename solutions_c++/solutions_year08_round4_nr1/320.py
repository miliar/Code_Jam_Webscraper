#include <cstdio>

using namespace std;

#define MAX 10005
#define INF 123456789

#define MINF(a, b) (((a) < (b)) ? (a) : (b))

void input(void);
void solve(void);

int n, m, r;
int A[MAX];
int B[MAX];
int F[MAX][2];
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
  scanf("%d %d", &n, &r);
  
  m = (n - 1) / 2;
  for(int i = 1; i <= m; i++) scanf("%d %d", &A[i], &B[i]);
  
  for(int i = m + 1; i <= n; i++) scanf("%d", &A[i]);
}

void solve(void)
{
  for(int i = m + 1; i <= n; i++) {
    F[i][0] = (A[i] == 0) ? 0 : INF;
    F[i][1] = (A[i] == 1) ? 0 : INF;
  }
  
  int cost;
  for(int i = m; i >= 1; i--) {
    F[i][0] = INF;
    // try and
    cost = (A[i] == 1) ? 0 : INF;
    if(B[i] == 1 && A[i] == 0) cost = 1;
    F[i][0] = MINF(F[2 * i][0], F[2 * i + 1][0]) + cost;
    // try or
    cost = (A[i] == 0) ? 0 : INF;
    if(B[i] == 1 && A[i] == 1) cost = 1;
    F[i][0] = MINF(F[i][0], F[2 * i][0] + F[2 * i + 1][0] + cost);
    
    F[i][1] = INF;
    // try and
    cost = (A[i] == 1) ? 0 : INF;
    if(B[i] == 1 && A[i] == 0) cost = 1;
    F[i][1] = F[2 * i][1] + F[2 * i + 1][1] + cost;
    // try or
    cost = (A[i] == 0) ? 0 : INF;
    if(B[i] == 1 && A[i] == 1) cost = 1;
    F[i][1] = MINF(F[i][1], MINF(F[2 * i][1], F[2 * i + 1][1]) + cost);
    
    F[i][0] = MINF(INF, F[i][0]);
    F[i][1] = MINF(INF, F[i][1]);
  }
  
  printf("Case #%d: ", case_cnt++);
  if(F[1][r] >= INF) printf("IMPOSSIBLE\n");
  else printf("%d\n", F[1][r]);
}  
    




