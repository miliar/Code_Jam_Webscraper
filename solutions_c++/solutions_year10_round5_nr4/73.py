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

const Int mod = 1000000007;

int cnt;

void rec(int N, int start, int B, vector<int> used) {
  if( N == 0 ) {
    cnt++;
    return;
  }

  for(int i = start; i <= N; i++) {

    bool go = true;
    vector<int> next = used;
    int n = i;
    int keta = 0;
    while( n ) {
      int x = n % B;
      n /= B;
      keta++;
      if( used[keta] & (1 << x) ) {
        go = false;
        break;
      }
      next[keta] |= (1 << x);
    }
    
    if( go )
      rec( N - i, i, B, next );
  }
}

void run() {
  int N, B; cin >> N >> B;
  cnt = 0;

  vector<int> used(20);
  rec(N, 1, B, used);

  cout << cnt << endl;
}

int main() {
  int TNO; scanf("%d", &TNO);
  for(int tno = 1; tno <= TNO; tno++) {

    printf("Case #%d: ", tno);
    run();
  }
  return 0;
}
