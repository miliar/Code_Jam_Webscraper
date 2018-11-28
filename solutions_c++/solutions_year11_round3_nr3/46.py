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

long long F[10010];

int main(){
  int T;
  cin >> T;
  REP(i, T){
    int N, L, H;
    cin >> N >> L >> H;
    REP(j, N){
      cin >> F[j];
    }
    // small
    for(long long f = L; f <= H; f++){
      REP(j, N){
        if(F[j] % f != 0 && f % F[j] != 0){
          goto out2;
        }
      }
      cout << "Case #" << i+1 << ": " << f << endl;
      goto out;
out2:;
    }
    cout << "Case #" << i+1 << ": NO" << endl;
out:;
  }

  return 0;
}

