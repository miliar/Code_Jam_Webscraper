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
#define READ_STRING(X) { scanf("%s", stringReader); X = stringReader; }
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

struct Cell {
  bool done;
  int sink_x;
  int sink_y;
  char label;
  Cell() : done(false) {}
};

int H, W;
vector<vector<int> > amap;
vector<vector<Cell> > cmap;
char sink;

void DFS(int x, int y, vector<int>&px, vector<int>&py) {
  if ( cmap[y][x].done ) {
    for ( int i = 0, GSIZE(N, px); i < N; ++i ) {
      Cell& cell = cmap[py[i]][px[i]];
      cell.done = true;
      cell.sink_x = cmap[y][x].sink_x;
      cell.sink_y = cmap[y][x].sink_y;
      cell.label = cmap[y][x].label;
    }
    return;
  }
  int dx[] = { 0, -1, 1, 0 };
  int dy[] = { -1, 0, 0, 1 };
  int bk = -1;
  int ba = oo<int>();
  for ( int k = 0; k < 4; ++k ) {
    int nx = x + dx[k];
    int ny = y + dy[k];
    if ( nx < 0 || nx >= W || ny < 0 || ny >= H ) continue;
    if ( amap[ny][nx] >= amap[y][x] ) continue;
    if ( amap[ny][nx] < ba ) {
      ba = amap[ny][nx];
      bk = k;
    }
  }
  px.push_back(x);
  py.push_back(y);
  if ( bk < 0 ) {
    // sink
    Cell& cell = cmap[y][x];
    if ( !cell.done ) {
      cell.done = true;
      cell.sink_x = x;
      cell.sink_y = y;
      cell.label = sink++;
    }
    DFS(x, y, px, py);
  } else DFS(x + dx[bk], y + dy[bk], px, py);
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
  while ( test < TESTS ) {
    ++test;
    READ_INT(H); READ_INT(W);
    amap.clear(); cmap.clear();
    for ( int i = 0; i < H; ++i ) {
      vector<int> row;
      READ_VECTOR(row, W, int);
      amap.push_back(row);
      cmap.push_back(vector<Cell>(W));
    }
    sink = 'a';
    for ( int i = 0; i < H; ++i ) {
      for ( int j = 0; j < W; ++j ) {
        vector<int> px, py;
        DFS(j, i, px, py);
      }
    }
    printf("Case #%d:\n", test);
    for ( int i = 0; i < H; ++i ) {
      for ( int j = 0; j < W; ++j ) {
        if ( j ) printf(" ");
        printf("%c", cmap[i][j].label);
      }
      printf("\n");
    }
  }
  return 0;
}
