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
#define READ_LINE() for ( char* ptr = stringReader; scanf("%c", ptr) == 1; ++ptr ) if ( *ptr == '\n' || *ptr == '\r' ) { *ptr = 0; break; }

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

typedef vector<bool> Token;

int main() {
/*
  freopen(FILE_NAME".in", "wt", stdout);

  printf("15 5000 500\n");
  for ( int i = 0; i < 5000; ++i ) {
    printf("abcdefghijklmno\n");
  }
  for ( int i = 0; i < 500; ++i ) {
    for ( int j = 0; j < 15; ++j )  printf("(abcdefghijklmno)");
    printf("\n");
  }

  return 0;
*/


#ifdef TEST_FILE
  freopen(FILE_NAME".in", "rt", stdin);
#endif
#ifdef OUT_FILE
  freopen(FILE_NAME".out", "wt", stdout);
#endif
  int L, D; READ_INT(L); READ_INT(D);
  int TESTS; scanf("%d", &TESTS);
  vector<string> dic;
  READ_VECTOR(dic, D, string);
  int test = 0;
  while ( test < TESTS ) {
    ++test;
    READ_STRING();
    char* ptr = stringReader;
    vector<Token> pattern;
    while ( *ptr ) {
      Token tok(26, false);
      if ( *ptr == '(' ) {
        while ( *++ptr != ')' ) tok[*ptr - 'a'] = true;
        ++ptr;
      } else tok[*ptr++ - 'a'] = true;
      pattern.push_back(tok);
    }
    int sol = 0;
    for ( int i = 0; i < D; ++i ) {
      bool ok = true;
      for ( int j = 0; j < L && ok; ++j ) ok = pattern[j][dic[i][j] - 'a'];
      if ( ok ) ++sol;
    }
    printf("Case #%d: %d\n", test, sol);
  }
  return 0;
}
