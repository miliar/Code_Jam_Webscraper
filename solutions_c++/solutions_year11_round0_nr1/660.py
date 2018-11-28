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

int main(){
  int T;
  cin >> T;
  REP(i, T){
    int P[2], M[2];
    int ret = 0;
    P[0] = P[1] = 1;
    M[0] = M[1] = 0;
    int N;
    cin >> N;
    REP(j, N){
      char c;
      int p;
      cin >> c >> p;
      bool b = c == 'B';
      int m = max(abs(p - P[b]) - M[b] + 1, 1);
      P[b] = p;
      M[b] = 0;
      M[b^1] += m;
      ret += m;
    }
    cout << "Case #" << i+1 << ": " << ret << endl;
  }

  return 0;
}

