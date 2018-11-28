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

int org[256][256];

void rotate(int N) {
  int buf[256][256];
  REP(i, N) REP(j, N) buf[i][j] = org[i][j];

  for(int i = 0; i < N; i++) {
    for(int j = 0; j < N; j++) {
      org[i][j] = buf[j][N - i - 1];
    }
  }
}


const int inf = 987654321;
int test(int N, int K, int best, int L) {
  int res = K * K - N * N;
  if( best <= res ) return inf;

  int buf[K][K];
  REP(i, K) REP(j, K) buf[i][j] = -1;
  REP(i, N) REP(j, N) {
    if( i + L >= K ) return inf;
    buf[i + L][j] = org[i][j];
  }

  REP(i, K) REP(j, i) {
    if( buf[i][j] != buf[j][i] ) {
      if( buf[i][j] != -1 && buf[j][i] != -1 ) return inf;
      if( buf[i][j] == -1 ) buf[i][j] = buf[j][i];
      if( buf[j][i] == -1 ) buf[j][i] = buf[i][j];
    }
  }

  
  
  {
    int temp[256][256];
    REP(i, K) REP(j, K) temp[i][j] = buf[i][j];
    for(int i = 0; i < K; i++) {
      for(int j = 0; j < K; j++) {
        buf[i][j] = temp[j][K - i - 1];
      }
    }
  }
  
  REP(i, K) REP(j, i) {
    if( buf[i][j] != buf[j][i] ) {
      if( buf[i][j] != -1 && buf[j][i] != -1 ) return inf;
      if( buf[i][j] == -1 ) buf[i][j] = buf[j][i];
      if( buf[j][i] == -1 ) buf[j][i] = buf[i][j];
    }
  }

  return res;
}

int run() {
  int N; cin >> N;

  for(int i = 0; i < N * 2; i++) {
    for(int j = 0; j <= i; j++) {
      int x = i - j;
      int y = j;
      if( 0 <= x && x < N && 0 <= y && y < N )
        cin >> org[x][y];
    }
  }

  int best = inf;
  for(int k = N; k <= 4 * N; k++) {
    for(int d = 0; d < 4; d++) {
      
      for(int L = 0; L < N; L++) {
        int t = test(N, k, best, L);
        checkmin(best, t);        
      }
      
      rotate(N);      
    }
  }
  return best;
}

int main() {
  int TNO; scanf("%d", &TNO);
  for(int tno = 1; tno <= TNO; tno++) {

    printf("Case #%d: ", tno);

    cout << run() << endl;
  }
  return 0;
}
