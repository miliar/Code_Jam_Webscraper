#include <iostream>
#include <sstream>
#include <iomanip>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <algorithm>
#include <complex>
#include <string>
#include <stdint.h>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>

using namespace std;

#define REP(i,n) for(int i = 0; i < (int)(n); i++)
#define rep(i,m,n) for(int i = m; i < (int)(n); i++)
#define FOR(i,c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define ALLOF(c) (c).begin(), (c).end()

typedef double decimal;
typedef complex<decimal> P;

const decimal EPS = 1e-8;

const int MOD = 1000000007;

int a[512][512];

int main(){
  int T;
  cin >> T;
  REP(i, T){
    int H, W, D;
    cin >> H >> W >> D;
    REP(h, H) REP(w, W){
      char c;
      cin >> c;
      a[h][w] = c - '0';
    }
    for(int sz = min(H, W); sz >= 3; sz--){
      REP(j, H-sz+1) REP(k, W-sz+1){
        int l = j + sz-1;
        int m = k + sz-1;
        int w0 = 0;
        int w1 = 0;
        for(int p = j; p <= l; p++) for(int q = k; q <= m; q++){
          if((p == j || p == l) && (q == k || q == m)) continue;
          int r = j+l-p;
          int s = k+m-q;
          if(p > r || (p == r && q >= s)) continue;
          int diff = a[p][q] - a[r][s];
          w0 += (p-r) * diff;
          w1 += (q-s) * diff;
        }
        if(w0 == 0 && w1 == 0){
          printf("Case #%d: %d\n", i+1, sz);
          goto out;
        }
      }
    }
    printf("Case #%d: IMPOSSIBLE\n", i+1);
out:;
  }

  return 0;
}

