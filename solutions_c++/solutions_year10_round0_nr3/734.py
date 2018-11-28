#include <cstdio>

int R, K, N;
int g[1000];

long long get_value(int& begin, int& cnt) {
  int chk[1000] = {0, };
  int i = 0;
  while (!chk[i]) {  
    chk[i] = 1;
    long long sum = 0;
    int t = 0;
    while (sum + g[i] <= K && t++ < N) {
      sum += g[i];
      i = ++i % N;
    }
  }
  long long v = 0;
  cnt = 0;
  begin = i;
  do {
    long long sum = 0;
    int t = 0;
    while(sum + g[i] <= K && t++ < N) {
      sum += g[i];
      i = ++i % N;
    }
    cnt++;
    v += sum;
  } while(i != begin);
  return v;
}

int main() {
  freopen("input.txt", "r", stdin);
  freopen("output.txt", "w", stdout);
  int cs;
  int r = 0;
  scanf("%d", &cs);
  while (cs--) {
    scanf("%d %d %d", &R, &K, &N);
    for (int i = 0; i < N; ++i) scanf("%d", &g[i]);
    int begin, cnt;
    long long v = get_value(begin, cnt);
    
    long long sol = 0;
    i = 0;
    while (R > 0) {
      if (i == begin && R >= cnt) {
        sol += (R / cnt) * v;
        R %= cnt;
      } else {
        long long sum = 0;
        int t = 0;
        while (sum + g[i] <= K && t++ < N) {
          sum += g[i];
          i = ++i % N;
        }
        R--;
        sol += sum;
      }
    }
    printf("Case #%d: %I64d\n", ++r, sol);
  }
  return 0;  
}