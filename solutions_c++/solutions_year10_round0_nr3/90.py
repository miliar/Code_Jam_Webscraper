#include <iostream>
#include <sstream>
#include <algorithm>
#include <numeric>
#include <vector>
#include <deque>
#include <queue>
#include <set>
#include <map>
#include <functional>
#include <complex>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <climits>
#include <cassert>
using namespace std;

#define REP(i,n) for(int i=0;i<(int)(n);++i)
#define SZ(a) ((int)((a).size()))
#define REPSZ(i,v) REP(i,SZ(v))
#define ALL(a) (a).begin(),(a).end()
typedef long long Int;
template<class T> inline T sq(T x){return x * x;}
template<class T> inline void checkmin(T &a,T b){if(b<a)a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a)a=b;}

Int solve(int R, int K, int N, vector<int> a) {
  Int memo[N];   memset(memo, -1, sizeof(memo));
  int timestamp[N]; memset(timestamp, -1, sizeof(timestamp));

  Int money = 0;
  int p = 0;
  for(int r = 0; r < R; r++) {
    if( memo[p] == -1 ) {
      memo[p] = money;
      timestamp[p] = r;
    } else {
      int len = r - timestamp[p];
      Int add = money - memo[p];
      
      money += ((R - timestamp[p]) / len - 1) * add;
      r = R - 1 - (R - timestamp[p]) % len;
      memset( memo, -1, sizeof(memo) );
      continue;
    }
    
    Int cur = 0;
    for(int i = 0; i < N; i++) {
      int np = (p + i) % N;
      if( cur + a[np] > K ) {
        p = np;
        break;
      } else {
        if( i == N - 1 ) p = np;
        cur += a[np];
      }
    }
    money += cur;
  }
  return money;
}

int main() {
  int TNO;
  scanf("%d", &TNO);
  for(int tno = 1; tno <= TNO; tno++) {
    printf("Case #%d: ", tno);
    int R, K, N; cin >> R >> K >> N;
    vector<int> a;
    REP(i, N) {
      int x;
      cin >> x;
      a.push_back( x );
    }
    cout << solve(R, K, N, a) << endl;
  }
}
