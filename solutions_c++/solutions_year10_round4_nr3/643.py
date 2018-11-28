#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <numeric>
#include <cstring>
#include <queue>
#include <stack>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <string>
#include <sstream>
#include <complex>
#include <cassert>
using namespace std;
#define rep(i,s,e) for(int i=(s),___e=(e);i<___e;++i)
#define REP(i,n) rep(i,0,n)
#define ITER(c) __typeof((c).begin())
#define FOR(i,c) for(ITER(c) i=(c).begin(),___e=(c).end();i!=___e;++i)
#define ALL(c) (c).begin(), (c).end()
#define CLEAR(v) memset(v, 0, sizeof(v))
typedef unsigned int ui;
typedef long long ll;
const double PI = atan(1.0) * 4.0;
int in_c() { int c; while ((c = getchar()) <= ' ') { if (!~c) return ~0; } return c; }
int in() {
  int x = 0, c;
  while ((ui)((c = getchar()) - '0') >= 10) { if (c == '-') return -in(); if (!~c) return ~0; }
  do { x = 10 * x + (c - '0'); } while ((ui)((c = getchar()) - '0') < 10);
  return x;
}

const int M = 200;
bool Bact[M][M][2];
bool AllZero(bool t) {
  REP(i, M) REP(j, M) if(Bact[i][j][t]) return false;
  return true;
}
int main() {
  int T = in();
  REP(turn, T) {
    CLEAR(Bact);
    int R = in();
    REP(i, R) {
      int r1 = in(), c1 = in();
      int r2 = in(), c2 = in();
      rep(r, r1, r2 + 1) rep(c, c1, c2 + 1)
        Bact[r][c][0] = 1;
    }
    int ans = 0;
    for(bool t = 1, p = 0; ; swap(t, p)) {
      rep(r, 1, M) rep(c, 1, M) {
        if( Bact[r-1][c][p] && Bact[r][c-1][p] )
          Bact[r][c][t] = 1;
        else if( !Bact[r-1][c][p] && !Bact[r][c-1][p] )
          Bact[r][c][t] = 0;
        else
          Bact[r][c][t] = Bact[r][c][p];
      }
      ++ans;
      if(AllZero(t)) break;
    }
    printf("Case #%d: %d\n", turn + 1, ans);
  }
  return 0;
}

