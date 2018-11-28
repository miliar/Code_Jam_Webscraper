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
#include "iostream"
using namespace std;

#ifndef ONLINE_JUDGE
#pragma warning(disable:4786)  // long identifiers
#pragma warning(disable:4996)  // deprecations
#endif

typedef long long i64;

//////////////////////////////////////////////////////////////////////////////////////////

const i64 INFINITE = 0x3f3f3f3f3f3fLL;
enum {INTERNAL = 0, LEAF = 1};
enum {OR = 0, AND = 1};
int gate[20000];
int changeable[20000];
int type[20000];
int nodeCount = 0;
i64 memo[20000][2];

i64 f(int node, int value) {
  if (type[node] == LEAF) return value == gate[node] ? 0 : INFINITE;
  i64& best = memo[node][value];
  if (best != -1) return best;
  const int child1 = 2 * node, child2 = child1 + 1;
  best = INFINITE;
  if (gate[node] == AND || changeable[node]) {
    const int cost = gate[node] == AND ? 0 : 1;
    if (value == 1) best = min(best, f(child1, 1) + f(child2, 1) + cost);
    else best = min(best, min(f(child1, 0), f(child2, 0)) + cost);
  }
  if (gate[node] == OR || changeable[node]) {
    const int cost = gate[node] == OR ? 0 : 1;
    if (value == 0) best = min(best, f(child1, 0) + f(child2, 0) + cost);
    else best = min(best, min(f(child1, 1), f(child2, 1)) + cost);
  }
  return best;
}

int main() {
#ifndef ONLINE_JUDGE
  freopen("data.in", "r", stdin);
  freopen("data.out", "w", stdout);
#endif
  int T; scanf("%d", &T);
  for (int Ti = 1; Ti <= T; ++Ti) {
    nodeCount = 1;
    int M, V; scanf("%d %d", &M, &V);
    for (int i = 1; i <= (M - 1) / 2; ++i) {
      const int node = nodeCount++;
      scanf("%d %d", &gate[node], &changeable[node]);
      type[node] = INTERNAL;
    }
    for (int i = 1; i <= (M + 1) / 2; ++i) {
      const int node = nodeCount++;
      scanf("%d", &gate[node]);
      type[node] = LEAF;
    }
    memset(memo, -1, sizeof(memo));
    const i64 res = f(1, V);
    if (res < INFINITE) printf("Case #%d: %lld\n", Ti, res);
    else printf("Case #%d: IMPOSSIBLE\n", Ti);
  }
  return 0;
}
