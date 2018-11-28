#include <cstdio>
#include <cstring>

using namespace std;

#define MAX 512
#define MOD 10000

const char *pattern = "welcome to code jam";

int dp(int a, int b);

int n, m;
char text[MAX];
int F[MAX][32];

char buf[MAX];

int main(void)
{
  int t;
  gets(buf);
  sscanf(buf, "%d", &t);
  for(int case_cnt = 1; case_cnt <= t; case_cnt++) {
    gets(text);
    n = strlen(text);
    m = strlen(pattern);
    memset(F, -1, sizeof(F));
    printf("Case #%d: %.4d\n", case_cnt, dp(0, 0));
  }
    
  return 0;
}

int dp(int a, int b)
{
  if(b == m)        return 1;
  if(a == n)        return 0;
  if(F[a][b] != -1) return F[a][b];
  
  return F[a][b] = (dp(a + 1, b) + (text[a] == pattern[b] ? dp(a + 1, b + 1) : 0)) % MOD;
}


