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
    int N, PD, PG;
    bool ok;
    cin >> N >> PD >> PG;
    if(PG == 0){
      ok = PD == 0;
    }else if(PG == 100){
      ok = PD == 100;
    }else if(N >= 100){
      ok = true;
    }else{
      ok = false;
      REP(i, N){
        if((i+1) * PD % 100 == 0){
          ok = true;
          break;
        }
      }
    }
    cout << "Case #" << i+1 << ": " << (ok ? "Possible" : "Broken") << endl;
  }

  return 0;
}

