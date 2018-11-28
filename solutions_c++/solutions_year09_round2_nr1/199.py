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

#define READ_INT(X) scanf("%d\n", &(X))
#define READ_I64(X) scanf("%lld", &(X))
#define READ_STRING() scanf("%s", stringReader)
#define READ_VECTOR(X, N, T) { T ASDQWEASD; for ( int asdqweasd = 0; asdqweasd < N && cin >> ASDQWEASD; ++asdqweasd ) X.push_back(ASDQWEASD); }
#define READ_LINE(N) { N = 0; for ( char* ptr = stringReader; scanf("%c", ptr) == 1; ++ptr, ++N ) if ( *ptr == '\n' || *ptr == '\r' ) { *ptr = 0; break; } }
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

struct Tree {
  string name;
  double w;
  Tree* left;
  Tree* right;
  Tree() : name(""), w(0), left(0), right(0) {}

  const char* build(const char * ptr) {
    while ( *ptr && *ptr != '(' ) ++ptr;
    ++ptr;
    while ( *ptr && *ptr == ' ' ) ++ptr;
    int i = 0;
    while ( *ptr && (isdigit(*ptr) || *ptr == '.') ) {
      stringReader[i++] = *ptr++;
      stringReader[i] = 0;
    }
    w = atof(stringReader);
    while ( *ptr && *ptr == ' ' ) ++ptr;
    if ( *ptr != ')' ) {
      while ( *ptr && isalpha(*ptr) ) {
        name += *ptr++;
      }
      left = new Tree();
      ptr = left->build(ptr);
      right = new Tree();
      ptr = right->build(ptr);
    }
    while ( *ptr && *ptr != ')' ) ++ptr;
    return ptr + 1;
  }

  double cute(double p, const set<string>& att) {
    p *= w;
    if ( left == 0 ) return p;
    return ((att.find(name) == att.end()) ? right : left)->cute(p, att);
  }
};

int main() {
#ifdef TEST_FILE
  freopen(FILE_NAME".in", "rt", stdin);
#endif
#ifdef OUT_FILE
  freopen(FILE_NAME".out", "wt", stdout);
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
      fprintf(stderr, "Computing case: %d/%d (%.2f%%)\n", test, TESTS, 100 * p);
      fprintf(stderr, "Times: %.2f (%.2f)\n", (double(now - start) / CLOCKS_PER_SEC) / 60,
        ((now - start) / (p * CLOCKS_PER_SEC)) / 60);
    }
#endif

    int lines;
    READ_INT(lines);
    string stree = "";
    for ( int i = 0; i < lines; ++i ) {
      int N;
      READ_LINE(N);
      stree += stringReader;
    }
    Tree root;
    root.build(stree.c_str());
    READ_INT(lines);
    printf("Case #%d:\n", test);
    for ( int i = 0; i < lines; ++i ) {
      READ_STRING();
      int atts;
      scanf("%d", &atts);
      set<string> att;
      for ( int j = 0; j < atts; ++j ) {
        READ_STRING();
        att.insert(stringReader);
      }
      printf("%.8lf\n", root.cute(1, att));
    }
    int N;
    READ_LINE(N);
  }
  return 0;
}
