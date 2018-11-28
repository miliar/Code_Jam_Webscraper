// Headers {{{
#include <algorithm>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <list>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
using namespace std;
#define REP(i,n) for(int i=0; i<(n); ++i)
#define FOR(i,j,k) for(int i=(j); i<=(k); ++i)
#define FORD(i,j,k) for(int i=(j); i>=(k); --i)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin(); it!=(c).end(); ++it)
#define ST first
#define ND second
#define MP make_pair
#define ALL(a) (a).begin(),(a).end()
#define SQR(a) ((a)*(a))
#define debug(x) cerr << #x << " = " << x << '\n'
#define size(x) ((int)(x).size())
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<pair<int,int> > VPII;
typedef unsigned long long ULL;
typedef long long LL;
typedef long double LD;
typedef pair<int,int> PII;
const int INF=1000000000;
// }}}

char board[4][5];

bool checkwin(char c) {
  REP(i, 4) {
    bool row = true;
    REP(j, 4) if (board[i][j] != 'T' && board[i][j] != c) row = false;
    if (row) return true;
  }
  REP(j, 4) {
    bool col = true;
    REP(i, 4) if (board[i][j] != 'T' && board[i][j] != c) col = false;
    if (col) return true;
  }
  bool diag1 = true;
  REP(i, 4) if (board[i][i] != 'T' && board[i][i] != c) diag1 = false;
  bool diag2 = true;
  REP(i, 4) if (board[i][3 - i] != 'T' && board[i][3 - i] != c) diag2 = false;
  return diag1 || diag2;
}

bool filled() {
  bool res = true;
  REP (i, 4) REP(j, 4) if (board[i][j] == '.') res = false;
  return res;
}

void tc(int num) {
  printf("Case #%d: ", num);
  REP(i,4) scanf("%s", board[i]);
  if (checkwin('X')) printf("X won\n");
  else if (checkwin('O')) printf("O won\n");
  else if (filled()) printf("Draw\n");
  else printf("Game has not completed\n");
}

int main() {
  int ntc;
  scanf("%d", &ntc);
  FOR (i, 1, ntc) tc(i);
  return 0;
}
