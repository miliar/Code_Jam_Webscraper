#include "cmath"
#include "cstdio"
#include "algorithm"
#include "map"
#include "numeric"
#include "queue"
#include "set"
#include "string"
#include "utility"
#include "vector"
using namespace std;
typedef long long i64;
const int INFINITE = 0x3f3f3f3f;

int m[1024], n;
int p[10][1024];
i64 memo[10][11][1 << 10];
bool mark[10][11][1 << 10];

i64 f(int round, int missed, int match) {
  if (round < 0) return missed <= m[match] ? 0 : INFINITE;
  i64& best = memo[round][missed][match];
  if (mark[round][missed][match]) return best;
  best = INFINITE, mark[round][missed][match] = true;
  const int c1 = 2 * match, c2 = 2 * match + 1;
  best = min(best, f(round - 1, missed + 1, c1) + f(round - 1, missed + 1, c2));
  best = min(best, f(round - 1, missed, c1) + f(round - 1, missed, c2) + p[round][match]);
  return best;
}
int main() {
  int T; scanf("%d", &T);
  for (int Ti = 1; Ti <= T; ++Ti) {
    fprintf(stderr, "Case #%d of %d...\n", Ti, T);
    scanf("%d", &n);
    for (int i = 0; i < (1 << n); ++i) scanf("%d", &m[i]);
    for (int i = 0; i < n; ++i)
      for (int k = 0; k < (1 << (n - 1 - i)); ++k)
        scanf("%d", &p[i][k]);
    memset(mark, false, sizeof(mark));
    printf("Case #%d: %lld\n", Ti, f(n - 1, 0, 0));
  }
  return 0;
}
