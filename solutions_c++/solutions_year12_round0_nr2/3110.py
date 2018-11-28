#define FOR(q,n) for(int q=0; q<n; q++)
#include <algorithm>
#include <stdio.h>
// mod 0
// 0 0 0
// -1 0 1 *

// mod 1
// 0 0 1
// -1 1 1 *

// mod 2
// 0 0 2 *
// 0 1 1

int test_no_surprise(int value, int limit) {
  //printf("test no surprise %d %d\n", value, limit);
  int avg = value / 3;
  int mod = value % 3;
  if (mod == 0) {
    if (avg < 0) return -1000000;
    return avg >= limit;
  } else if (mod == 1) {
    if (avg < 0) return -1000000;
    return avg + 1 >= limit;
  } else {
    return avg + 1 >= limit;
  }
}

int test_surprise(int value, int limit) {
  int avg = value / 3;
  int mod = value % 3;
  if (mod == 0) {
    if (avg < 1) return -10000000;
    return avg + 1 >= limit;
  } else if (mod == 1) {
    if (avg < 1) return -10000000;
    return avg + 1 >= limit;
  } else {
    return avg + 2 >= limit;
  }
}

void solve(int _case) {
  int res=0;
  int n,s;
  const int MAX=200;
  int data[MAX];
  int p;
  scanf("%d %d %d", &n, &s, &p);
  FOR(i, n) scanf("%d", &data[i]);

  int best[MAX][MAX];

  FOR(q, MAX) FOR(w, MAX) best[q][w]=-100000;

  FOR(i, n + 1) {
    if (i==0) {
      best[0][0] = 0;
      continue;
    }
    
    best[i][0] = best[i-1][0] + test_no_surprise(data[i-1], p);
    FOR(j, s + 1) if (j) {
      // best[i][j] is the best solution for first i googlers
      // while using exactly j surprises
      best[i][j] = std::max(
            best[i-1][j] + test_no_surprise(data[i-1], p),
            best[i-1][j-1] + test_surprise(data[i-1],p)
          );
    }
  }

  printf("Case #%d: %d\n", _case, best[n][s]);
}

int main() {
  int t;
  int n;
  scanf("%d", &n);
  for (t=0; t<n; t++) {
    solve(t+1);
  }
}
