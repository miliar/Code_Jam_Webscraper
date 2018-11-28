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

struct S {
  i64 digs;
  int i, j;
  string current;
  string below;
  S(i64 D, int I, int J, const string& c, const string& B) : digs(D), i(I), j(J), current(c), below(B) {}
  bool operator<(const S& o) const {
    //if ( i == R - 1 && o.i < R - 1 ) return false;
    //if ( i < R - 1 && o.i == R - 1 ) return true;
    if ( digs != o.digs ) return digs > o.digs;
    if ( i != o.i ) return i < o.i;
    if ( j != o.j ) return j > o.j;
    return false;
  }
};

map<string, i64> minCost[60][60];
int R, C, F;

vector<string> cave;
void InitCost() {
  for ( int i = 0; i < 60 ;++i ) for ( int j = 0; j < 60 ;++j ) minCost[i][j].clear();
  cave.clear();
}

void add(priority_queue<S>& pq, i64 d, int i, int j, const string& c, const string& b) {
  if ( j < 0 ) return;
  if ( j >= C ) return;
  string x = c + b;
  map<string, i64>::const_iterator it = minCost[i][j].find(x);
  if ( it != minCost[i][j].end() && d >= it->second ) return;
  minCost[i][j][x] = d;
  pq.push(S(d, i, j, c, b));
}

int Fall(int i, int j) {
  int f = 1;
  for ( int k = i + 1; k < R; ++k ) {
    if ( cave[k][j] == '#' ) return f;
    ++f;
  }
  return f;
}

//#define ATTEMPT "xxx"
#define ATTEMPT "small-B.0"
//#define ATTEMPT "small-B.1"
//#define ATTEMPT "small-B.2"
//#define ATTEMPT "small-B.3"
//#define ATTEMPT "large-B"
int main() {
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
      dprintf("Times: %.2f (%.2f)", double(now - start) / CLOCKS_PER_SEC,
        (now - start) / (p * CLOCKS_PER_SEC));
    }
#endif
    scanf("%d%d%d", &R, &C, &F);
    InitCost();
    for ( int i = 0; i < R; ++i ) {
      scanf("%s", stringReader);
      cave.push_back(stringReader);
    }
    cave.push_back(string(C, '#'));
    i64 sol = -1;
    priority_queue<S> pq;
    add(pq, 0, 0, 0, cave[0], cave[1]);
    while ( !pq.empty() ) {
      S s = pq.top(); pq.pop();
      if ( s.i == R - 1 ) {
        sol = s.digs;
        break;
      }
      if ( s.j && s.current[s.j - 1] == '.' && s.below[s.j - 1] == '#' ) {
        add(pq, s.digs, s.i, s.j - 1, s.current, s.below);
      }      
      if ( s.j + 1 < C && s.current[s.j + 1] == '.' && s.below[s.j + 1] == '#' ) {
        add(pq, s.digs, s.i, s.j + 1, s.current, s.below);
      }      
      if ( s.j && s.current[s.j - 1] == '.' && s.below[s.j - 1] == '.' ) {
        int f = Fall(s.i + 1, s.j - 1);
        if ( f <= F ) add(pq, s.digs, s.i + f, s.j - 1, f == 1 ? s.below : cave[s.i + f], cave[s.i + f + 1]);
      }
      if ( s.j + 1 < C && s.current[s.j + 1] == '.' && s.below[s.j + 1] == '.' ) {
        int f = Fall(s.i + 1, s.j + 1);
        if ( f <= F ) add(pq, s.digs, s.i + f, s.j + 1, f == 1 ? s.below : cave[s.i + f], cave[s.i + f + 1]);
      }
      /*
      if ( s.j && s.current[s.j - 1] == '.' && s.below[s.j - 1] == '#' ) {
        int f = Fall(s.i + 1, s.j - 1);
        if ( f <= F ) add(pq, s.digs + 1, s.i + f, s.j - 1, cave[s.i + f], cave[s.i + f + 1]);
      }
      if ( s.j + 1 < C && s.current[s.j + 1] == '.' && s.below[s.j + 1] == '#' ) {
        int f = Fall(s.i + 1, s.j + 1);
        if ( f <= F ) add(pq, s.digs + 1, s.i + f, s.j + 1, cave[s.i + f], cave[s.i + f + 1]);
      }
      */
      if ( s.j && s.current[s.j - 1] == '.' && s.below[s.j - 1] == '#' ) {
        string b = s.below;
        b[s.j - 1] = '.';
        add(pq, s.digs + 1, s.i, s.j, s.current, b);
      }
      if ( s.j + 1 < C && s.current[s.j + 1] == '.' && s.below[s.j + 1] == '#' ) {
        string b = s.below;
        b[s.j + 1] = '.';
        add(pq, s.digs + 1, s.i, s.j, s.current, b);
      }
    }
    if ( sol == -1 ) printf("Case #%d: No\n", test);
    else printf("Case #%d: Yes %lld\n", test, sol);
  }
#ifndef _DEBUG
  dprintf(ATTEMPT".out written");
#endif
  return 0;
}
