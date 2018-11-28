#ifdef _MSC_VER
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
#include "utility"
#include "string"
#include "limits"
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

// BEGIN CUT HERE
//Znippet tag
// END CUT HERE

void dprintf(char* format, ...) {
  fprintf(stderr, "DEBUG: ");
  va_list argp; va_start(argp, format);
  vfprintf(stderr, format, argp); va_end(argp);
  fprintf(stderr, "\n");
}

#define SIZE(N, V) int N = static_cast<int>((V).size())
#define GSIZE(N, V) (N) = static_cast<int>((V).size())
#define ALL(V) (V).begin(), (V).end()
#define UNIQUE(C) {sort(ALL(C)); C.resize(unique(ALL(C)) - C.begin());}
#define CAST(X, Y) {stringstream ss; ss << (X); ss >> (Y);}

template<typename _Type>
_Type oo() { return numeric_limits<_Type>::has_infinity ? numeric_limits<_Type>::infinity() : (numeric_limits<_Type>::max() / 2); }
template<typename _Type>
bool oo(_Type x) { return x >= oo<_Type>(); }
const double eps = 1e-9;
typedef long long i64;

static char stringReader[2097152];

int N;
bool ok(const vector<int>& vals) {
  for ( int i = 0; i < N; ++i ) if ( vals[i] > i )
    return false;
  return true;
}

i64 bs(vector<int>& vals) {
  i64 s = 0;
  for ( int i = 0; !ok(vals) && i < N; ++i ) {
    int j = i;
    for ( ; true; ++j ) {
      if ( vals[j] <= i ) break;
    }
    for ( int k = j; k > i; --k ) {
      swap(vals[k - 1], vals[k]);
      ++s;
    }
  }
  return s;
}

#define ATTEMPT "xxx"
//#define ATTEMPT "small-A.0"
//#define ATTEMPT "small-A.1"
//#define ATTEMPT "small-A.2"
//#define ATTEMPT "small-A.3"
//define ATTEMPT "large-A"
int main() {
/*
  freopen("xxx.in", "wt", stdout);
  printf("60\n");
  for ( int i = 0; i < 60; ++i ) {
    printf("40\n");
    string a(40, '1');
    for ( int k = 0; k < 40; ++k ) { for ( int j = 0; j < k; ++j ) {
      a[40 - j - 1] = '0';
    }
    printf("%s\n", a.c_str());
    }
  }
  return 0;
  */

  freopen("xxx.in", "rt", stdin);
#ifndef _DEBUG
  dprintf("Using output file "ATTEMPT".out");
  system("copy "ATTEMPT".out "ATTEMPT".out.bak");
  freopen(ATTEMPT".out", "wt", stdout);
#endif
  int TESTS; scanf("%d\n", &TESTS);
  int test = 0;
  clock_t start = clock();
  while ( test < TESTS ) {
    ++test;
#ifndef _DEBUG
    {
      double p = double(test)/TESTS;
      clock_t now = clock();
      dprintf("Computing case: %d/%d (%.2f%%)", test, TESTS, 100 * p);
      dprintf("Times: %.2f (%.2f)", double(now - start) / CLOCKS_PER_SEC / 60,
        (now - start) / (p * CLOCKS_PER_SEC) / 60);
    }
#endif
    vector<int> vals;
    scanf("%d", &N);
    for ( int i = 0; i < N; ++i ) {
      scanf("%s", stringReader);
      int x = 0;
      for ( int j = N - 1; j > 0; --j ) if ( stringReader[j] == '1' ) {
        x = j;
        break;
      }
      vals.push_back(x);
    }
    printf("Case #%d: %lld\n", test, bs(vals));
  }
#ifndef _DEBUG
  dprintf(ATTEMPT".out written");
#endif
  return 0;
}
