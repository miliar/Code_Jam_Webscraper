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


Int price[4400];
int miss[1100];
int buy[4400];
Int total;
int N, P;

const Int inf = 1LL << 60;
Int memo[4400][16];

Int rec(int node, int fin) {
  if( node >= N ) {
    if( miss[node - N] < P - fin )
      return inf;
    else
      return 0;
  }
  
  Int &res = memo[node][fin];
  if( res != -1 ) return res;
  
  res = inf;
  res = min(res, price[node] + rec(node * 2 + 1, fin + 1) + rec(node * 2, fin + 1) );
  res = min(res,               rec(node * 2 + 1, fin) + rec(node * 2, fin) );
  return res;
}

Int run() {
  cin >> P;
  N = 1 << P;
  REP(i, N) cin >> miss[ N - 1 - i ];
  REP(i, N - 1) cin >> price[N - 1 - i];

//   REP(i, N) cout << i << ' ' << miss[i] << endl;
//   REP(i, N) cout << i << ' ' << price[i] << endl;

  memset(buy, 0, sizeof(buy));

  /*
  for(int i = N; i < N + N; i++) {
    int s = i;
    int m = miss[i - N];
    cout << i << ' ' << "miss = " << m << endl;
    while( s ) {
      int game = s / 2;
      s >>= 1;
      if( m == 0 ) {
        buy[game] = 1;
      }
      else
        m--;
    }
  }
  */

  memset(memo, -1, sizeof(memo));
  return rec(1, 0);
}

int main() {
  int TNO; scanf("%d", &TNO);
  for(int tno = 1; tno <= TNO; tno++) {

    printf("Case #%d: ", tno);
    cout << run() << endl;
  }
  return 0;
}
