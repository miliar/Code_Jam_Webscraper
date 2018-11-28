#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <vector>
#include <set>
#include <utility>
#include <string>
#include <queue>
#include <bitset>
#include <climits>

#ifdef _DEBUG_MODE_
#define db(X) { cerr << "* DEBUG [L" << __LINE__ << "]: " << #X << " = " << X << endl; }
#define db_arr(X) { cerr << "* DEBUG [L" << __LINE__ << "]: {" << #X << "} = "; for (int __i__=0; __i__<sizeof(X)/sizeof(X[0]); __i__++) cerr << X[__i__] << " "; cerr << endl; }
#define db_arrM(X, M) { cerr << "* DEBUG [L" << __LINE__ << "]: {" << #X << "} = "; for (int __i__=0; __i__<M; __i__++) cerr << X[__i__] << " "; cerr << endl; }
#define db_arrMN(X, M, N) { cerr << "* DEBUG [L" << __LINE__ << "]: {" << #X << "} = "; for (int __i__=M; __i__<N; __i__++) cerr << X[__i__] << " "; cerr << endl; }
#else
#define db(X)
#define db_arr(X)
#define db_arrM(X, M)
#define db_arrMN(X, M, N)
#endif

#define For(i, n) for(i=0;i<(n);i++)
#define ForL(i, m, n) for(i=(m);i<(n);i++)

#define Clear(X) memset( (X), 0, sizeof( (X) ) )
#define Fill(X) memset( (X), -1, sizeof( (X) ) )

#define ArraySize(X) (sizeof(X)/sizeof(X[0]))

template <typename T> void xchg(T &a, T &b) { T c=a; a=b; b=c; }

using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;
typedef unsigned long ulong;

void _main();

int main() {
  // COUNTER CODE STARTS HERE
  int cases;
  cin >> cases;

  for (int i = 1; i <= cases; ++i) {
    printf("Case #%d: ", i);
    _main();
  }

  // COUNTER CODE ENDS HERE
  return 0;
}

// ACTUAL CODE STARTS BELOW

char map[4][4];
bool endgame = true;
char line[5] = {0};

char getWinner() {
  int x = 0, t = 0, o = 0;
  int i;

  For (i, 4) {
    switch(line[i]) {
    case '.': return 0;
    case 'X': ++x; break;
    case 'O': ++o; break;
    case 'T': ++t; break;
    }
  }

  if (t == 1) {
    if (x == 3) return 'X';
    if (o == 3) return 'O';
    return 0;
  }

  if (x == 4) return 'X';
  else if (o == 4) return 'O';
  return 0;
}

void _main() {
  int i, j;
  char c;
  endgame = true;

  For (i, 4) For (j, 4) {
    while (c = getchar()) {
      if (c == 'X' || c == 'O' || c == '.' || c == 'T') {
        map[i][j] = c;
        if (c == '.') endgame = false;
        break;
      }
    }
  }

  // Row
  For (i, 4) {
    For (j, 4) {
      line[j] = map[i][j];
    }

    if (c = getWinner()) {
      cout << c << " won" << endl;
      return;
    }
  }

  // Column
  For (i, 4) {
    For (j, 4) {
      line[j] = map[j][i];
    }

    if (c = getWinner()) {
      cout << c << " won" << endl;
      return;
    }
  }

  // Diag 1
  For (j, 4) {
    line[j] = map[j][j];
  }

  if (c = getWinner()) {
    cout << c << " won" << endl;
    return;
  }

  // Diag 2
  For (j, 4) {
    line[j] = map[j][3-j];
  }

  if (c = getWinner()) {
    cout << c << " won" << endl;
    return;
  }

  if (endgame) {
    puts("Draw");
  } else {
    puts("Game has not completed");
  }
}
