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
    i64 n, A, B, C, D, x0, y0, M;
    scanf("%lld%lld%lld%lld%lld%lld%lld%lld", &n, &A, &B, &C, &D, &x0, &y0, &M);
    vector<i64> X(1, x0);
    vector<i64> Y(1, y0);
    for ( int i = 1; i < n; ++i ) {
      X.push_back((A * X[i - 1] + B) % M);
      Y.push_back((C * Y[i - 1] + D) % M);
    }
    i64 sol = 0;
    for ( int i = 0; i < n; ++i ) {
      for ( int j = i + 1; j < n; ++j ) {
        for ( int k = j + 1; k < n; ++k ) {
          i64 num1 = X[i] + X[j] + X[k];
          i64 num2 = Y[i] + Y[j] + Y[k];
          if ( num1 % 3 || num2 % 3 ) continue;
          ++sol;
        }
      }
    }
    printf("Case #%d: %lld\n", tcase, sol);
  }
  clock_t time_end = clock();
  fprintf(stderr, "\ntime: %.2f secs (%d ticks)\n", double(time_end - time_begin) / CLOCKS_PER_SEC, time_end - time_begin);
  return 0;
}