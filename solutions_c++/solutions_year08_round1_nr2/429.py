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

int main() {
  freopen("xxx.in", "rt", stdin);
#ifndef _DEBUG
  freopen("xxx.out", "wt", stdout);
#endif
  clock_t time_begin = clock();
  int TCases; scanf("%d", &TCases);
  for ( int tcase = 1; tcase <= TCases; ++tcase ) {
    int N, M; scanf("%d%d", &N, &M);
    typedef pair<int, int> PR;
    typedef vector<PR> VPR;
    typedef vector<VPR> VVPR;
    VVPR users;
    vector<int> Ts;
    for ( int i = 0; i < M; ++i ) {
      int T; scanf("%d", &T);
      Ts.push_back(T);
      VPR user;
      for ( int j = 0; j < T; ++j ) {
        int x, y; scanf("%d%d", &x, &y);
        user.push_back(PR(x - 1, y));
      }
      users.push_back(user);
    }
    int best = 5000;
    int state = 1 << N;
    for ( int mask = 0, n = (1 << N); mask < n; ++mask ) {
      bool ok = false;
      for ( int i = 0; i < M; ++i ) {
        ok = false;
        for ( int j = 0; j < Ts[i]; ++j ) {
          bool a = users[i][j].second != 0;
          bool b = ((1 << users[i][j].first) & mask) != 0;
          if ( a == b ) {
            ok = true; break;
          }
        }
        if ( !ok ) break;
      }
      if ( ok ) {
        int cost = __builtin_popcount(mask);
        if ( cost < best ) {
          best = cost;
          state = mask;
        }
      }
    }
    printf("Case #%d:", tcase);
    if ( best == 5000 ) printf(" IMPOSSIBLE");
    else for ( int i = 0; i < N; ++i ) printf(" %d", ((1 << i) & state) ? 1 : 0);
    printf("\n");
  }
  clock_t time_end = clock();
  fprintf(stderr, "\ntime: %.2f secs (%d ticks)\n", double(time_end - time_begin) / CLOCKS_PER_SEC, time_end - time_begin);
  return 0;
}