#include <cstdio>
#include <cstring>
#include <vector>

using namespace std;

#define MAX 1024

typedef __int64 LL;

void input(void);
void solve(void);

int next(int x);
int profit(int x);

int r, cap, n;
int G[MAX];
int T[MAX];
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
  scanf("%d %d %d", &r, &cap, &n);
  for(int i = 0; i < n; i++) scanf("%d", &G[i]);
}

void solve(void)
{
  vector <int> que;
  memset(T, -1, sizeof(T));
  
  int x = 0;
  int cur_time = 0;
  while(T[x] == -1) {
    T[x] = cur_time;
    cur_time++;
    que.push_back(x);
    x = next(x);
  }
  
  int prefix = T[x];
  int cycle_len = cur_time - T[x];
  
  if(r <= prefix) {
    LL res = 0;
    for(int i = 0; i < r; i++) res += profit(que[i]);
    printf("Case #%d: %I64d\n", case_cnt++, res);
  }
  else {
    LL res = 0;
    for(int i = 0; i < prefix; i++) res += profit(que[i]);
    LL cycle_profit = 0;
    for(int i = prefix; i < que.size(); i++) cycle_profit += profit(que[i]);
    res += cycle_profit * ((r - prefix) / cycle_len);
    int rem = (r - prefix) % cycle_len;
    for(int i = 0; i < rem; i++) res += profit(que[prefix + i]);
    printf("Case #%d: %I64d\n", case_cnt++, res);
  }  
}

int next(int x)
{
  int sum = 0;
  for(int i = 0; i < n; i++) {
    int y = (x + i) % n;
    sum += G[y];
    if(sum > cap) return y;
  }
  return x;
}

int profit(int x)
{
  int sum = 0;
  for(int i = 0; i < n; i++) {
    int y = (x + i) % n;
    if(sum + G[y] > cap) return sum;
    sum += G[y];
  }
  return sum;
}
