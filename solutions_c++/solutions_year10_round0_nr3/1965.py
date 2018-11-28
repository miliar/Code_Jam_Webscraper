#include <cstdio>
#include <cstring>

#define MAXN 1005

typedef long long llint;

int R, K, N;

int g[MAXN];
int next[MAXN];
llint cost[MAXN];
int was[MAXN];

llint solve() {
  memset(cost, 0, sizeof(cost));
  for( int from = 0; from < N; ++from ) {
    int to = from;
    for( int i = 0; i < N; ++i ) {
      to = (from+i)%N;
      if( cost[from]+g[to] > K )
        break;
      cost[from] += g[to];
    }
    next[from] = to;
  }
  
  int period = -1;

  memset(was, -1, sizeof(was));
  int cycle_start = -1;
  llint sol = 0;
  int ind = 0;
  for( int i = 0; i < R; ++i ) {
    if( i > 0 && was[ind] != -1 ) {
      cycle_start = ind;
      period = i - was[ind];
      break; 
    }
    was[ind] = i;
    ind = next[ind];
  }

  if( cycle_start == -1 ) {
    ind = 0;
    for( int i = 0; i < R; ++i ) {
      sol += cost[ind];
      ind = next[ind];
    }
    return sol;
  } 


  for( ind = 0; ind != cycle_start; ind = next[ind] )
    sol += cost[ind];

  R -= was[cycle_start];

  int cycles = R/period;
  llint cycle_sum = 0;
  ind = cycle_start;
  for( int i = 0; i < period; ++i ) {
    cycle_sum += cost[ind];
    ind = next[ind];
  }
  sol += cycles * cycle_sum;
  R -= cycles * period;

  ind = cycle_start;
  for( int i = 0; i < R; ++i ) {
    sol += cost[ind];
    ind = next[ind];
  }
  
  return sol;
}

int main() {

  int n_tc;
  scanf("%d", &n_tc);

  for( int tc = 0; tc < n_tc; ++tc  ) {
    scanf("%d%d%d", &R, &K, &N);
    for( int i = 0; i < N; ++i ) 
      scanf("%d", &g[i]);
    printf("Case #%d: %lld\n", tc+1, solve());
  }

  return 0;
}
