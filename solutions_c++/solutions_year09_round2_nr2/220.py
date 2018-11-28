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
#define CAST(X, Y) {stringstream ss; ss << (X); ss >> (Y);}

#define READ_INT(X) scanf("%d", &(X))
#define READ_I64(X) scanf("%lld", &(X))
#define READ_STRING() scanf("%s", stringReader)
#define READ_VECTOR(X, N, T) { T ASDQWEASD; for ( int asdqweasd = 0; asdqweasd < N && cin >> ASDQWEASD; ++asdqweasd ) X.push_back(ASDQWEASD); }
#define READ_LINE(N) { N = 0; for ( char* ptr = stringReader; scanf("%c", ptr) == 1; ++ptr, ++N ) if ( *ptr == '\n' || *ptr == '\r' ) { *ptr = 0; break; }
//#define READ_LINE() for ( char* ptr = stringReader; scanf("%c", ptr) == 1; ++ptr ) if ( *ptr == '\n' || *ptr == '\r' ) { *ptr = 0; break; }

typedef long long i64;
template<typename _Type>
_Type oo() { return numeric_limits<_Type>::has_infinity ? numeric_limits<_Type>::infinity() : (numeric_limits<_Type>::max() / 2); }
template<typename _Type>
bool oo(_Type x) { return x >= oo<_Type>(); }
const double eps = 1e-9;
const double bs_high = 1LL << numeric_limits<double>::digits;

#define FILE_NAME "xxx"

#define TEST_FILE

#ifndef _DEBUG
#define OUT_FILE
#endif

static char stringReader[2097152];

string find(const string& number) {
  SIZE(N, number);
  int src = -1;
  int dest = -1;
  for ( int i = N - 1; i > 0; --i ) {
    for ( int j = i - 1; j >= 0; --j ) if ( number[j] < number[i] ) {
      if ( dest < j ) {
        src = i;
        dest = j;
      }
    }
  }
  if ( dest >= 0 ) {
    int i = src;
    int j = dest;
    string same = number.substr(0, j);
    string rest = "";
    for ( int k = j; k < N; ++k ) if ( k != i ) rest.push_back(number[k]);
    sort(ALL(rest));
    return same + string(1, number[i]) + rest;
  }
  return "";
}

int main() {
#ifdef TEST_FILE
  freopen(FILE_NAME".in", "rt", stdin);
#endif
#ifdef OUT_FILE
  freopen(FILE_NAME".out", "wt", stdout);
#endif
  int TESTS; scanf("%d", &TESTS);
  int test = 0;
  clock_t start = clock();
  while ( test < TESTS ) {
    ++test;
#ifndef _DEBUG
    {
      double p = double(test)/TESTS;
      clock_t now = clock();
      fprintf(stderr, "Computing case: %d/%d (%.2f%%)\n", test, TESTS, 100 * p);
      fprintf(stderr, "Times: %.2f (%.2f)\n", (double(now - start) / CLOCKS_PER_SEC) / 60,
        ((now - start) / (p * CLOCKS_PER_SEC)) / 60);
    }
#endif
    READ_STRING();
    string number = stringReader;
    string next = find(number);
    if ( next == "" ) next = find("0" + number);
    printf("Case #%d: %s\n", test, next.c_str());

    /* debugger 
    i64 nn, nnn;
    CAST(number, nn);
    CAST(next, nnn);
    string xx = number;
    sort(ALL(xx));
    for ( i64 i = nn + 1; i < nnn; ++i ) {
      string x;
      CAST(i, x);
      sort(ALL(x));
      if ( x == xx ||test == 44) {
        fprintf(stderr, "%3d %s\n", test, number.c_str());
        fprintf(stderr, "%3d %s\n", test, next.c_str());
        fprintf(stderr, "%3d %lld\n", test, i);
        break;
      }
    }
    */
  }
  return 0;
}
