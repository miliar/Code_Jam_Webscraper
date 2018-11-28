#include "assert.h"
#include "ctype.h"
#include "math.h"
#include "stdio.h"
#include "string.h"
#include "stdlib.h"
#include "time.h"
#include "algorithm"
#include "numeric"
#include "functional"
#include "bitset"
#include "vector"
#include "list"
#include "set"
#include "map"
#include "queue"
#include "stack"
#include "string"
#include "sstream"
using namespace std;

#ifndef ONLINE_JUDGE
#pragma warning(disable:4786)  // long identifiers
#pragma warning(disable:4996)  // deprecations
#endif

typedef long long i64;
#define all(x) (x).begin(), (x).end()

//////////////////////////////////////////////////////////////////////////////////////////

const int INFINITE = 1000000;
vector<string> engines;
vector<int> queries;
int memo[101][1001];

char* TruncLine(char* str) {
  const int length = (int)strlen(str);
  if (length > 0 && str[length - 1] == '\n')
    str[length - 1] = '\0';
  return str;
}

int f(int i, int j, int n, int m) {
  if (j >= m) return 0;
  int& best = memo[i][j];
  if (best != -1) return best;
  best = INFINITE;
  if (queries[j] != i) best = min(best, f(i, j + 1, n, m));
  for (int k = 0; k < n; ++k) if (queries[j] != k && i != k)
    best = min(best, f(k, j + 1, n, m) + 1);
  return best;
}

int main() {
#ifndef ONLINE_JUDGE
  freopen("data.in", "r", stdin);
  freopen("data.out", "w", stdout);
#endif
  static char buffer[1000000];
  const int T = atoi(fgets(buffer, sizeof(buffer), stdin));
  for (int Ti = 1; Ti <= T; ++Ti) {
    engines.clear(); queries.clear();
    const int n = atoi(fgets(buffer, sizeof(buffer), stdin));
    for (int k = 0; k < n; ++k)
      engines.push_back(TruncLine(fgets(buffer, sizeof(buffer), stdin)));
    const int m = atoi(fgets(buffer, sizeof(buffer), stdin));
    for (int k = 0; k < m; ++k) {
      const string query = TruncLine(fgets(buffer, sizeof(buffer), stdin));
      queries.push_back((int)(find(all(engines), query) - engines.begin()));
    }
    memset(memo, -1, sizeof(memo));
    int res = f(0, 0, n, m);
    for (int i = 1; i < n; ++i)
      res = min(res, f(i, 0, n, m));
    printf("Case #%d: %d\n", Ti, res);
  }
  return 0;
}
