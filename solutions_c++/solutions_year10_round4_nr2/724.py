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
int M[1 << 10];
int Price[10][1 << 10];

int main() {
  int T = in();
  REP(turn, T) {
    int P = in();
    int N = 1 << P;
    REP(i, N) M[i] = in();
    REP(i, P) REP(j, 1 << (P - 1 - i)) Price[i][j] = in();
    int ans = 0;
    for(int C = P - 1; C >= 0; --C) {
      int x = P - 1 - C;
      int E = 1 << (P - C);
      for(int i = 0; i < N; i += E) {
        int me = *min_element(M + i, M + i + E);
        if(me == x) {
          ++ans;
          rep(j, i, i + E) ++M[j];
        }
      }
    }
    printf("Case #%d: %d\n", turn + 1, ans);
  }
  return 0;
}


