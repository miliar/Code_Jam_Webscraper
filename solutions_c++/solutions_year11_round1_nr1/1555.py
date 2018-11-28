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

ll gcd(ll a, ll b) {
  return a == 0 ? b : gcd(b % a, a);
}

bool IsPossible(ll N, int PD, int PG) {
    bool ok = false;
//     for (int d = 0; d <= N; ++d) {
//       int w = PD * d;
//       if (w % 100 == 0) {
//         // w / d, w' / g
//         // w' >= w, g >= d
//         int rw = PG - w / 100;
//         int rg = 100 - d;
//         ok = rw <= rg;
//       }
//     }
    for (int d = 1; d <= N; ++d) {
      int wd = PD * d;
      if (wd % 100 == 0) {
        wd /= 100;
        // w / d, w' / g
        // w' >= w, g >= d
//         int rw = PG - w / 100;
//         int rg = 100 - d;
//         ok = rw <= rg;
        for (int g = d; g <= 1000000; ++g) {
          int wg = PG * g;
          if (wg % 100 == 0) {
            wg /= 100;
            //            if (g >= d + wg) {
            if (wg >= wd && g >= d + wg - wd) {
              // printf("%d/%d, %d/%d\n", wd, d, wg, g);
              ok = true;
              return ok;
            }
          }
        }
      }
    }
    return ok;
}

int main() {
  int T;
  cin >> T;
  REP(turn, T) {
    ll N;
    int PD, PG;
    cin >> N >> PD >> PG;
    bool ok = IsPossible(N, PD, PG);
    printf("Case #%d: %s\n", turn + 1, ok ? "Possible" : "Broken");
  }
  return 0;
}
