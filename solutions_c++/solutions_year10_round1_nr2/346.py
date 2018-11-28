#include <cstdio>
#include <algorithm>

using namespace std;

#define MAXN 300

int a[MAXN], D, I, M, N;
int memo[MAXN][MAXN][MAXN];

int best(int v, int i, int k) {
  if (i == N)
    return 0;

  if (memo[v][i][k] != -1)
    return memo[v][i][k];

  int res = D + best(v, i+1, 0);
  
  if (k < 255) {
    for (int vv = 0; vv <= 255; vv++)
      if ((v == 280 || abs(vv-v) <= M) // && abs(vv-a[i]) <= M
	  )
	res = min(res, I + best(vv, i, k+1));
  }
  
  for (int vv = 0; vv <= 255; vv++)
    if (v == 280 || abs(v-vv) <= M)
      res = min(res, abs(a[i]-vv) + best(vv, i+1, 0));

  return memo[v][i][k] = res;
}

int main() {
  int T, cases = 1;

  scanf(" %d", &T);
  while (T--) {
    scanf(" %d%d%d%d", &D, &I, &M, &N);
    for (int i = 0; i < N; i++)
      scanf(" %d", &a[i]);
    memset(memo, -1, sizeof(memo));
    printf("Case #%d: %d\n", cases++, best(280, 0, 0));
  }

  return 0;
}
