#include <cstdio>

int T;
int R, K, N;
long long g[1001];
long long sum[1001];
int next[1001];
long long profit[1001];

int main() {
  int i;
  scanf("%d", &T);
  for(int t = 1; t <= T; t++) {
    scanf("%d %d %d", &R, &K, &N);
    sum[0] = 0;
    for(i = 0; i < N; i++) {
      scanf("%lld", &g[i]);
      sum[i+1] = sum[i]+g[i];
    }
    if(sum[N] <= K) {
      printf("Case #%d: %lld\n", t, R*sum[N]);
      continue;
    }
    int start = 0, end = 0;
    long long load = 0;
    for(start = 0; start < N; start++) {
      while(load+g[end] <= K) {
        load += g[end];
        end = (end+1) % N;
      }
      next[start] = end;
      profit[start] = load;
//      fprintf(stderr, "[%d]: p%lld n%d\n", start, profit[start], next[start]);
      if(start != end) load -= g[start];
    }
    start = 0;
    long long result = 0;
    for(i = 0; i < R; i++) {
      result += profit[start];
      start = next[start];
    }
    printf("Case #%d: %lld\n", t, result);
  }
  return 0;
}

