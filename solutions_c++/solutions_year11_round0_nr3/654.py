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
    int N;
    cin >> N;
    int mini = 10000000;
    int sum = 0;
    int B = 0;
    REP(_, N){
      int c;
      cin >> c;
      B ^= c;
      sum += c;
      mini = min(c, mini);
    }
    cout << "Case #" << i+1 << ": ";
    if(B != 0){
      cout << "NO" << endl;
    }else{
      cout << sum - mini << endl;
    }
  }

  return 0;
}

