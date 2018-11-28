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

const int MC = 200, MN = 1000000;
int C, D;
int P[MC], V[MC];

int N;
int POS[MN];

int main() {
  int T;
  cin >> T;
  REP(turn, T) {
    cin >> C >> D;
    REP(i, C) cin >> P[i] >> V[i];
    N = 0;
    REP(i, C) REP(j, V[i]) POS[N++] = P[i];
//     REP(i, N) cout << POS[i] << ' ';
//     cout << endl;
    double L = 0, R = 1e30;
    REP(loop, 300) {
      double M = L + (R - L) / 2.0;
      bool ok = true;
      double left = (double) POS[0] - M;
      for (int i = 1; i < N; ++i) {
        // -M ~ +M
        double opt = left + D;
        double next = 1e100;
        if (opt <= POS[i]) {
          next = max(opt, (double) POS[i] - M);
        } else {
          if (opt - POS[i] > M) {
            ok = false;
            goto END;
          } else {
            next = opt;
          }
        }
        left = next;
      }
   END:;
      if (ok) {
        R = M;
      } else {
        L = M;
      }
    }
    printf("Case #%d: %.10f\n", turn + 1, R);
  }
  return 0;
}
