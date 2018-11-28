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

int X, S, R, T, N;
const int MX = 100000, MN = 1000;
int B[MN], E[MN], W[MN];

struct Walk {
  int speed, length;
  bool operator < (const Walk& w) const {
    return speed < w.speed;
  }
};

int nws;
Walk walks[MN + 1];

int main() {
  int TURN;
  cin >> TURN;
  REP(turn, TURN) {
    cin >> X >> S >> R >> T >> N;
    REP(i, N) {
      cin >> B[i] >> E[i] >> W[i];
    }
    int remain = X;
    REP(i, N) {
      int l = E[i] - B[i];
      remain -= l;
      int s = W[i];
      walks[i] = (Walk) {s, l};
    }
    nws = N;
    if (remain) {
      walks[N] = (Walk) {0, remain};
      ++nws;
    }
    sort(walks, walks + nws);
    //REP(i, nws) cout << walks[i].speed << ' ' << walks[i].length << endl;
    // solve
    double ans = 0;
    double remt = T;
    REP(i, nws) {
      if ((R + walks[i].speed) * remt < walks[i].length) {
        //cout << "half run" << endl;
        ans += (double) (walks[i].length - (R + walks[i].speed) * remt) /( walks[i].speed + S);
        ans += remt;
        remt = 0;
      } else {
        //cout << "run" << endl;
        double t = (double) walks[i].length / (walks[i].speed + R);
        remt -= t;
        ans += t;
      }
    }
    printf("Case #%d: %.6f\n", turn + 1, ans);
  }
  return 0;
}
