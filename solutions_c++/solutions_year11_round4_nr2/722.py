#include <iostream>
#include <cstdio>
#include <cassert>
#include <climits>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <numeric>
#include <functional>
#include <vector>
#include <map>
#include <set>
#include <list>
#include <deque>
#include <stack>
#include <queue>
#include <string>
#include <sstream>
#include <fstream>
#include <complex>
#include <iterator>
#include <memory>
#include <utility>
using namespace std;
#define REP(i,n) for(int i=0;i<(int)n;++i)
#define rep(i,s,n) for(int i=s;i<(int)n;++i)
#define FOR(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define ALL(c) (c).begin(), (c).end()
#define MP(a, b) make_pair((a), (b))
typedef unsigned int ui;
typedef unsigned long long ull;
typedef long double ld;
typedef long long ll;
static const double PI = atan(1.0) * 4.0;
int in_c() { int c; while ((c = getchar()) <= ' ') { if (!~c) return ~0; } return c; }
int in() {
  int x = 0, c;
  while ((ui)((c = getchar()) - '0') >= 10) { if (c == '-') return -in(); if (!~c) return ~0; }
  do { x = 10 * x + (c - '0'); } while ((ui)((c = getchar()) - '0') < 10);
  return x;
}

const int MD = 100000, MR = 500, MC = 500;
int R, C, D;

int w[MR][MC];

bool EQ(double a, double b) { return abs(a - b) < 1e-9; }

bool IsValid(int r, int c, int K) {
  //cout << K << ' ' << r << ' ' << c << endl;
  double gr = (double) r + K * 0.5, gc = (double) c + K * 0.5;
  double wr = 0, wc = 0;
  REP(i, K) REP(j, K) {
    if (!((i == 0 || i == K - 1) && (j == 0 || j == K - 1))) {
      int rr = r + i, cc = c + j;
      wr += (rr + 0.5 - gr) * w[rr][cc];
      wc += (cc + 0.5 - gc) * w[rr][cc];
    }
  }
  return EQ(wr, 0) && EQ(wc, 0);
}

bool Check(int K) {
  REP(i, R - K + 1) {
    REP(j, C - K + 1) {
      if (IsValid(i, j, K)) {
        //        cout << "found " << i << ' ' << j << endl;
        return true;
      }
    }
  }
  return false;
}

int main() {
  int TURN;
  cin >> TURN;
  REP(turn, TURN) {
    cin >> R >> C >> D;
    REP(i, R) {
      string line;
      cin >> line;
      REP(j, C) {
        w[i][j] = D + line[j] - '0';
        //cout << w[i][j];
      }
      //cout << endl;
    }
    int ansK = -1;
    for (int K = min(R, C); K >= 3; --K) {
      if (Check(K)) {
        ansK = K;
        break;
      }
    }

    printf("Case #%d: ", turn + 1);
    if (ansK == -1) puts("IMPOSSIBLE");
    else printf("%d\n", ansK);
  }
  return 0;
}
