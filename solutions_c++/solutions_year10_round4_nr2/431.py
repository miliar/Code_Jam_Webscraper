#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

#define INF 0x3f3f3f3f3fll

int n, P;

int cost[3000], M[3000];
long long memo[3000][3000];

long long go(int k, int c) {
  if (k >= n-1) {
    int i = k - n + 1;
    return c < P-M[i] ? INF : 0;
  }

  if (memo[k][c] != -1)
    return memo[k][c];

  memo[k][c] = min(go(2*k + 1, c+1) + go(2*k + 2, c+1) + cost[k],
		   go(2*k + 1, c) + go(2*k + 2, c));

  return memo[k][c];
}

int main() {
  int T, cases = 1;

  scanf(" %d", &T);
  while (T--) {
    scanf(" %d", &P);
    
    n = 1<<P;

    for (int i = 0; i < n; i++)
      scanf(" %d", &M[i]);
    
    for (int i = P-1; i >= 0; i--)
      for (int j = (1 << i) - 1; j < ((1<<i) - 1 + (1<<i)); j++)
	scanf(" %d", &cost[j]);

    memset(memo, -1, sizeof(memo));

    printf("Case #%d: %lld\n", cases++, go(0, 0));
  }

  return 0;
}
