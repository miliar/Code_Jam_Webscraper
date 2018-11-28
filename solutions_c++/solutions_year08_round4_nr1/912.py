#ifdef _MSC_VER
#pragma warning(disable:4018)
#pragma warning(disable:4267)
#pragma warning(disable:4786)
#pragma warning(disable:4800)
#pragma warning(disable:4996)
template<typename _Type>
int __builtin_popcount(_Type x) {
  static int count[256] = {
    0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4,
    1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
    1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
    2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
    1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
    2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
    2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
    3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
    1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5,
    2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
    2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
    3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
    2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6,
    3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
    3, 4, 4, 5, 4, 5, 5, 6, 4, 5, 5, 6, 5, 6, 6, 7,
    4, 5, 5, 6, 5, 6, 6, 7, 5, 6, 6, 7, 6, 7, 7, 8
  };
  int c = 0;
  while ( x ) {
    c += count[x & 0xFF];
    x >>= 8;
  }
  return c;
}
#endif
#include "string"
#include "bitset"
#include "vector"
#include "queue"
#include "stack"
#include "list"
#include "map"
#include "set"
#include "algorithm"
#include "functional"
#include "numeric"
#include "utility"
#include "sstream"
#include "iostream"
#include "complex"
#include "stdio.h"
#include "float.h"
#include "math.h"
#include "stdlib.h"
#include "assert.h"
#include "stdarg.h"
#include "string.h"
#include "time.h"
#include "ctype.h"
using namespace std;

#define SIZE(N, V) int N = static_cast<int>((V).size())
#define GSIZE(N, V) (N) = static_cast<int>((V).size())
#define ALL(V) (V).begin(), (V).end()
#define UNIQUE(C) {sort(ALL(C)); C.resize(unique(ALL(C)) - C.begin());}
#define DTOI(X) static_cast<int>((X) + ((X) < 0.0 ? -eps : eps))
#define DFORCE(X, Y) DTOI(Y((X) + eps))
#define CAST(X, Y) {stringstream ss; ss << (X); ss >> (Y);}
typedef long long i64;
const i64 oo = 0x3FFFFFFF3FFFFFFFLL;
const double eps = 5e-6;
inline bool isZero(double x) { return abs(x) < eps; }
inline bool areSame(double x, double y) { return abs(x - y) < eps; }

#define Input_int(N) int N; scanf("%d", &N)
#define Input_i64(N) i64 N; scanf("%lld", &N)
#define Input_double(N) double N; scanf("%lf", &N)
#define Input_string(N) string N; { char str[4096 * 2]; scanf("%s", &str); N = str; }
#define Input_line(N) string N; \
        { char str[4096 * 2]; fgets(srt, sizeof(str), stdin); int n = strlen(str); if ( str[n - 1] == '\n' ) str[n - 1] = 0; }

#define SONS(X, Y) int X##_a = 2 * (Y + 1) - 1, X##_b = 2 * (Y  + 1)

struct Node {
  bool leaf;
  int value, change;
};

int M, V;
int M2;
vector<Node> tree;

i64 memo[10000 + 10][2];

i64 f(int node, int target) {
  if ( target > 1 ) return 0;
  if ( tree[node].leaf ) return target == tree[node].value ? 0 : oo;
  i64& best = memo[node][target];
  if ( best >= 0 ) return best;
  SONS(son, node);
  i64 a0 = f(son_a, 0);
  i64 b0 = f(son_b, 0);
  i64 a1 = f(son_a, 1);
  i64 b1 = f(son_b, 1);
  
  best = oo;
  i64 res0, res1, res2, res3;
  if ( a1 != oo && b1 != oo ) res0 = a1 + b1;
  else res0 = oo;
  res1 = min(a0, b0);
  res2 = min(a1, b1);
  if ( a0 != oo && b0 != oo ) res3 = a0 + b0;
  else res3 = oo;

  int totry = 0;
  if ( tree[node].value ) {
    if ( target ) {
      best = res0;
      totry |= (1 << 2);
    } else {
      best = res1;
      totry |= (1 << 3);
    }
  } else {
    if ( target ) {
      best = res2;
      totry |= (1 << 0);
    } else {
      best = res3;
      totry |= (1 << 1);
    }
  }
  if ( tree[node].change ) {
    if ( totry & ( 1 << 0 ) ) {
      best = min(best, res0 + 1);
    }
    if ( totry & ( 1 << 1 ) ) {
      best = min(best, res1 + 1);
    }
    if ( totry & ( 1 << 2 ) ) {
      best = min(best, res2 + 1);
    }
    if ( totry & ( 1 << 3 ) ) {
      best = min(best, res3 + 1);
    }
  }
  return best;
}

//#define GENERATE
int main() {
#ifdef GENERATE
  freopen("xxx.in", "wt", stdout);
  M = 10000;
  M2 = (M - 1) / 2;
  const int K = 3;
  printf("%d\n", K);
  for ( int k = 0; k < K; ++k ) {
    printf("%d %d\n", M, rand() % 2);
    for ( int i = 0; i < M2; ++i ) {
      printf("%d %d\n", rand() % 2, rand() % 2);
    }
    for ( int i = M2; i < M; ++i ) {
      printf("%d\n", rand() % 2);
    }
  }
#endif
  freopen("xxx.in", "rt", stdin);
#ifndef _DEBUG
  freopen("xxx.out", "wt", stdout);
#endif
  clock_t time_begin = clock();
  int TCases; scanf("%d", &TCases);
  for ( int tcase = 1; tcase <= TCases; ++tcase ) {
    scanf("%d%d\n", &M, &V);
    M2 = (M - 1) / 2;
    tree.assign(M, Node());
    for ( int i = 0; i < M2; ++i ) {
      scanf("%d%d", &tree[i].value, &tree[i].change);
      tree[i].leaf = false;
    }    
    for ( int i = M2; i < M; ++i ) {
      scanf("%d", &tree[i].value);
      tree[i].leaf = true;
    }
    memset(memo, -1, sizeof(memo));
    i64 sol = f(0, V);
    if ( sol == oo ) printf("Case #%d: IMPOSSIBLE\n", tcase);
    else printf("Case #%d: %lld\n", tcase, sol);
  }
  clock_t time_end = clock();
  fprintf(stderr, "\ntime: %.2f secs (%d ticks)\n", double(time_end - time_begin) / CLOCKS_PER_SEC, time_end - time_begin);
  return 0;
}