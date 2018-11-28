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

char a[64][64];

int main(){
  int T;
  cin >> T;
  REP(i, T){
    int H, W;
    cin >> H >> W;
    memset(a, '.', sizeof(a));
    REP(j, H) REP(k, W){
      char c;
      cin >> c;
      a[j][k] = c;
    }
    cout << "Case #" << i+1 << ":" << endl;
    REP(j, H) REP(k, W){
      if(a[j][k] == '#'){
        if(a[j][k+1] == '#' && a[j+1][k] == '#' && a[j+1][k+1] == '#'){
          a[j][k] = a[j+1][k+1] = '/';
          a[j][k+1] = a[j+1][k] = '\\';
        }else{
          cout << "Impossible" << endl;
          goto out;
        }
      }
    }
    REP(j, H){
      a[j][W] = '\0';
      cout << a[j] << endl;
    }
out:;
  }

  return 0;
}

