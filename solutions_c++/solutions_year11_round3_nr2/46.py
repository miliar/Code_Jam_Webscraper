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

int a[1000010];
int A[10010];

int main(){
  int T;
  cin >> T;
  REP(i, T){
    int L, N, C;
    long long t;
    cin >> L >> t >> N >> C;
    memset(A, 0, sizeof(A));
    long long t0, t1;
    t0 = 0;
    REP(j, N){
      int d;
      if(j < C){
        cin >> d;
      }else{
        d = a[j - C];
      }
      a[j] = d;
      t1 = t0 + d * 2;
      if(t0 > t){
        A[d]++;
      }else if(t1 > t){
        A[(t1 - t)/2]++;
      }
      t0 = t1;
    }
    for(int j = 10000; j >= 1; j--){
      int x = A[j];
      if(x == 0) continue;
      if(L > x){
        L -= x;
        t0 -= j * x;
      }else{
        t0 -= j * L;
        break;
      }
    }
    cout << "Case #" << i+1 << ": " << t0 << endl;
  }

  return 0;
}

