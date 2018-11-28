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


struct union_find {
  vector<int> s;
  i64 total_set;
  union_find(i64 N) : s(vector<int>((int)N, -1)), total_set(N) {}
  i64 parent(i64 x) {
    if ( s[int(x)] < 0 ) return x;
    return parent(s[int(x)]);
  }
  bool join(i64 x, i64 y) {
    x = parent(x);
    y = parent(y);
    if ( x == y ) return false;
    --total_set;
    s[int(x)] = int(y);
    return true;
  }
};


#define DEF_VEC(_Type, _Name) typedef vector<_Type> V##_Name
DEF_VEC(bool, B);
DEF_VEC(int, I);
void GeneratePrimes(int N, VB& prime, VI& primes, int cap = int(oo)) {
  N = min(N, cap);
  prime.assign(N, true); prime[0] = prime[1] = false;
  primes.assign(1, 2);
  for ( int j = 4; j < N && j < cap; j += 2 ) prime[j] = false;
  for ( int i = 3; i < N && i < cap; i += 2 ) {
    if ( !prime[i] ) continue;
    primes.push_back(i);
    for ( i64 j = i64(i) * i; j < N && j < cap; j += 2LL * i ) prime[int(j)] = false;
  }
}
void Factorize(int N, const VI& primes, VI& factors, VI& factors_count, bool save_0 = false) {
  const int sq = DFORCE(sqrt(double(N)), floor);
  for ( SIZE(s, primes), i = 0; i < s && primes[i] <= sq; ++i ) {
    int count = 0;
    while ( (N % primes[i]) == 0 ) {
      N /= primes[i];
      ++count;
    }
    if ( count || save_0 ) {
      factors.push_back(i);
      factors_count.push_back(count);
    }
  }
  if ( N > 1 ) {
    VI::const_iterator it = find(ALL(primes), N);
    if ( it == primes.end() ) return;
    factors.push_back(it - primes.begin());
    factors_count.push_back(1);
  }
}




int main() {
  freopen("xxx.in", "rt", stdin);
#ifndef _DEBUG
  freopen("xxx.out", "wt", stdout);
#endif
  clock_t time_begin = clock();
  int TCases; scanf("%d", &TCases);
  
  VI primes;
  VB prime;
  GeneratePrimes(1000, prime, primes);
  
  for ( int tcase = 1; tcase <= TCases; ++tcase ) {
    i64 A, B, P; scanf("%lld%lld%lld", &A, &B, &P);
    i64 N = B - A + 1;
    union_find uf(N);
    while ( !prime[P] ) ++P;
    int ppos = find(ALL(primes), P) - primes.begin();
    for ( i64 x = A; x <= B; ++x ) {
      VI xfactors, xcount;
      Factorize(int(x), primes, xfactors, xcount);
      for ( i64 y = x + 1; y <= B; ++y ) {
        VI yfactors, ycount;
        Factorize(int(y), primes, yfactors, ycount);
        VI::iterator xit = lower_bound(ALL(xfactors), ppos);
        VI::iterator yit = lower_bound(ALL(yfactors), ppos);
        while ( true ) {
          bool xover = xit == xfactors.end();
          bool yover = yit == yfactors.end();
          if ( xover || yover ) break;
          if ( *xit == *yit ) {
            uf.join(x - A, y - A);
            break;
          }
          if ( *xit < *yit ) ++xit;
          else ++yit;
        }
      }
    }
    printf("Case #%d: %lld\n", tcase, uf.total_set);
  }
  clock_t time_end = clock();
  fprintf(stderr, "\ntime: %.2f secs (%d ticks)\n", double(time_end - time_begin) / CLOCKS_PER_SEC, time_end - time_begin);
  return 0;
}