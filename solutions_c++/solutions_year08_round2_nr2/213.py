#include <cstdio>
#include <cstring>

using namespace std;

#define MAX 1005

void DFS(int x);
int gcd(int a, int b);
void init_S(void);

int n;
int S[MAX];
int U[MAX];
int G[MAX][MAX];

int main(void)
{
  init_S();
    
  int t;
  scanf("%d", &t);
  for(int case_cnt = 1; case_cnt <= t; case_cnt++) {
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);
    n = b - a + 1;
    memset(G, 0, sizeof(G));
    for(int i = a; i <= b; i++)
      for(int j = i + 1; j <= b; j++) {
        int x = gcd(i, j);
        if(x < 2 || S[x] < c) continue;
        G[i - a][j - a] = G[j - a][i - a] = 1;
      }
      
    memset(U, 0, sizeof(U));
    
    int ans = 0;
    for(int i = 0; i < n; i++) if(U[i] == 0) { DFS(i); ans++; }
    
    printf("Case #%d: %d\n", case_cnt, ans);
  }
    
  return 0;
}

void DFS(int x)
{
  U[x] = 1;
  for(int i = 0; i < n; i++) if(U[i] == 0 && G[x][i]) DFS(i);
}

int gcd(int a, int b)
{
  return !b ? a : gcd(b, a % b);
}

void init_S(void)
{
  for(int i = 0; i < MAX; i++) S[i] = i;
  for(int i = 2; i < MAX; i++)
    if(S[i] == i) for(int j = 2; i * j < MAX; j++) S[i * j] = i;
}


