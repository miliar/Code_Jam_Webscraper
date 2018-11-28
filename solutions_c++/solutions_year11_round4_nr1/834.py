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

double a[110];

int main(){
  int T;
  cin >> T;
  REP(i, T){
    int X, S, R, N;
    double t;
    cin >> X >> S >> R >> t >> N;
    int x = 0;
    memset(a, 0, sizeof(a));
    REP(j, N){
      int B, E, w;
      cin >> B >> E >> w;
      a[w] += E-B;
      x += E-B;
    }
    a[0] = X - x;
    double T = 0;
    REP(j, 101){
      int s = j + S;
      int r = j + R;
      double t0 = a[j] / r;
      if(t0 < t){
        t -= t0;
        T += t0;
      }else{
        T += t + (a[j] - r * t) / s;
        t = 0;
      }
    }
    printf("Case #%d: %.10f\n", i+1, T);
  }

  return 0;
}

