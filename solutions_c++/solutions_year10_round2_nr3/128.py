#include <cstdio>
#include <cstring>

using namespace std;

#define MAX 512
#define MOD 100003

typedef long long LL;

void init_C(void);
int dp(int n, int m);

int C[MAX][MAX];
int F[MAX][MAX];
int case_cnt = 1;

int main(void)
{
  init_C();
  memset(F, -1, sizeof(F));
    
  int t;
  scanf("%d", &t);
  while(t--) {
    int n;
    scanf("%d", &n);
    int res = 0;
    for(int i = 1; i < n; i++) {
      res += dp(n, i);
      res %= MOD;
    }
    printf("Case #%d: %d\n", case_cnt++, res);
  }  
    
  return 0;
}

void init_C(void)
{
  for(int i = 0; i < MAX; i++) C[i][0] = 1;
  for(int j = 1; j < MAX; j++) C[0][j] = 0;
  for(int i = 1; i < MAX; i++) for(int j = 1; j < MAX; j++)
    C[i][j] = (C[i - 1][j - 1] + C[i - 1][j]) % MOD;
}

int dp(int n, int m)
{
  if(m >= n)        return 0;
  if(m == 1)        return 1;
  if(F[n][m] != -1) return F[n][m];
  
  int sum = 0;
  for(int i = 0; m - i - 1 >= 1; i++) {
    sum += (int) (((LL) C[n - m - 1][i] * dp(m, m - i - 1)) % MOD);
    sum %= MOD;
  }
  
  return F[n][m] = sum;
}

