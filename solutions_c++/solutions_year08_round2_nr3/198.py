#include <cstdio>
#include <vector>

using namespace std;

#define MAX 5005

int n, m;
int killed[MAX];
int next[MAX];
int prev[MAX];
vector <int> used;

int main(void)
{
  int t;
  scanf("%d", &t);
  for(int case_cnt = 1; case_cnt <= t; case_cnt++) {
    scanf("%d %d", &n, &m);
    used.clear();
    for(int i = 0; i < m; i++) {
      int a;
      scanf("%d", &a);
      used.push_back(a);
    }
    for(int i = 1; i <= n; i++) {
      next[i] = (i == n) ? 1 : i + 1;
      prev[i] = (i == 1) ? n : i - 1;
    }
    for(int i = 1; i <= n; i++) killed[i] = -1;
    int step = 0;
    int cur  = 1;
    for(int i = 1; i <= n; i++) {
      for(int j = 0; j < step; j++) cur = next[cur];
      killed[cur] = i;
      prev[next[cur]] = prev[cur];
      next[prev[cur]] = next[cur];
      cur = next[cur];
      step++;
    }
    
    printf("Case #%d:", case_cnt);
    for(int i = 0; i < used.size(); i++) printf(" %d", killed[used[i]]);
    printf("\n");
  }
    
  return 0;
}


