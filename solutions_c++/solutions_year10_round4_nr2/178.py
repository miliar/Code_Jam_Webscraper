#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

#define MAX_P 12
#define POW2(a) ((1) << (a))
#define INF 1000000005

void input(void);
void solve(void);

int dp(int t, int cnt, int a, int b);

int p;
int M[POW2(MAX_P)];
int P[POW2(MAX_P)];
int F[POW2(MAX_P)][MAX_P];
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
  scanf("%d", &p);
  for(int i = 0; i < POW2(p); i++) scanf("%d", &M[i]);
  for(int i = p - 1; i >= 0; i--) for(int j = POW2(i); j < POW2(i + 1); j++) {
    scanf("%d", &P[j]);
  } 
}

void solve(void)
{
  memset(F, -1, sizeof(F));
  printf("Case #%d: %d\n", case_cnt++, dp(1, 0, 0, POW2(p) - 1));
}

int dp(int t, int cnt, int a, int b)
{
  //printf("t = %d cnt = %d a = %d b = %d\n", t, cnt, a, b); 
    
  if(a == b)          return (M[a] < cnt) ? +INF : 0;
  if(F[t][cnt] != -1) return F[t][cnt];
  
  int mid = (a + b) / 2;
  
  int r1 = dp(2 * t, cnt + 0, a, mid) + dp(2 * t + 1, cnt + 0, mid + 1, b) + P[t];
  int r2 = dp(2 * t, cnt + 1, a, mid) + dp(2 * t + 1, cnt + 1, mid + 1, b);
  
  return F[t][cnt] = min(+INF, min(r1, r2));
}


  

