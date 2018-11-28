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

#define GETX(V) ((V) / 12)
#define GETY(V) ((V) % 12)
#define MAKEXY(X, Y) ((X) * 12) + (Y)

bool minCost[144][144];
int R, C;
vector<string> board;
int goals[2];
    int g = 0, b = 0;

struct S {
  int p[2];
  i64 c;
  S(int P[2], i64 C) {
    memcpy(p, P, sizeof(p));
    c = C;
  }
};

bool Ok(int p0, int p1) {
  return abs(GETX(p0) - GETX(p1)) + abs(GETY(p0) - GETY(p1)) <= 1;
}

void AddToQueue(queue<S>& q, int p0, int p1, i64 c) {
  if ( b == 1 ) p1 = p0;
  int p[] = { min(p0, p1), max(p0, p1) };
  if ( minCost[p[0]][p[1]] ) return;
  minCost[p[0]][p[1]] = true;
  q.push(S(p, c));
}

//#define ATTEMPT "xxx"
#define ATTEMPT "small-A.1"
//#define ATTEMPT "small-X.1"
//#define ATTEMPT "small-X.2"
//#define ATTEMPT "small-X.3"
//#define ATTEMPT "large"
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
    memset(minCost, false, sizeof(minCost));
    scanf("%d%d", &R, &C);
    board.clear();
    int box[2];
    g = 0, b = 0;
    for ( int i = 0; i < R; ++i ) {
      scanf("%s", stringReader);
      int N = int(strlen(stringReader));
      //printf("%s\n", stringReader);
      string row;
      for ( int j = 0; j < N; ++j ) {
        char cell = stringReader[j];
        if ( cell == 'w' ) {
          box[b++] = goals[g++] = MAKEXY(i, j);
          cell = '.';
        } else if ( cell == 'x' ) {
          goals[g++] = MAKEXY(i, j);
          cell = '.';
        } else if ( cell == 'o' ) {
          box[b++] = MAKEXY(i, j);
          cell = '.';
        }
        row += cell;
      }
      board.push_back(row);
    }
    if ( g == 1 ) {
      goals[1] = goals[0];
      box[1] = box[0];
    }
    sort(goals, goals + g);
    sort(box, box + b);
    queue<S> q;
    q.push(S(box, 0));
    i64 sol = -1;
    while ( !q.empty() ) {
      const S& st = q.front();
      if ( memcmp(st.p, goals, sizeof(goals)) == 0 ) {
        sol = st.c;
        break;
      }
      bool ok = Ok(st.p[0], st.p[1]);
      for ( int i = 0; i < b; ++i ) {
        int bp = st.p[i];
        int r = GETX(bp);
        int c = GETY(bp);
        int bp2 = st.p[1 - i];
        int r2 = GETX(bp2);
        int c2 = GETY(bp2);
        if ( r > 0 && r + 1 < R ) {
          if ( board[r + 1][c] == '.' && board[r - 1][c] == '.' ) {
            if ( !((r + 1 == r2 && c == c2) || (r - 1 == r2 && c == c2)) ) {
              int np0 = MAKEXY(r + 1, c);
              if ( ok || Ok(np0, bp2) ) {
                AddToQueue(q, np0, bp2, st.c + 1);
              }
              int np1 = MAKEXY(r - 1, c);
              if ( ok || Ok(np1, bp2) ) {
                AddToQueue(q, np1, bp2, st.c + 1);
              }
            }
          }
        }
        if ( c > 0 && c + 1 < C ) {
          if ( board[r][c + 1] == '.' && board[r][c - 1] == '.' ) {
            if ( !((r == r2 && c + 1 == c2) || (r == r2 && c - 1 == c2)) ) {
              int np0 = MAKEXY(r, c + 1);
              if ( ok || Ok(np0, bp2) ) {
                AddToQueue(q, np0, bp2, st.c + 1);
              }
              int np1 = MAKEXY(r, c - 1);
              if ( ok || Ok(np1, bp2) ) {
                AddToQueue(q, np1, bp2, st.c + 1);
              }
            }
          }
        }
      }
      q.pop();
    }
    printf("Case #%d: %lld\n", test, sol);
  }
#ifndef _DEBUG
  dprintf(ATTEMPT".out written");
#endif
  return 0;
}
