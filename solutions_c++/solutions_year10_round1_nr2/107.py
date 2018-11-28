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

const int inf = 987654321;
int dp[110][260];

int main() {
  int TNO;
  scanf("%d", &TNO);
  for(int tno = 1; tno <= TNO; tno++) {

    int D, I, M, N; scanf("%d%d%d%d", &D, &I, &M, &N);
    int a[N];
    REP(i, N) scanf("%d", &a[i]);

    REP(i, 110) REP(j, 260) dp[i][j] = inf;
    for(int val = 0; val < 256; val++) {
      dp[0][val] = 0;
    }
    for(int i = 1; i <= N; i++) {
      for(int val = 0; val < 256; val++) {
        
        // change
        {
          int prev = inf;
          for(int j = val - M; j <= val + M; j++) {
            if( 0 <= j && j <= 255 ) checkmin(prev, dp[i-1][j]);
          }
          checkmin( dp[i][val], (int)llabs(a[i - 1] - val) + prev );
        }

        // delete
        {
          checkmin( dp[i][val], D + dp[i-1][val] );
        }

      }
      // insert      
      for(bool change = true; change;){        
        change = false;
        for(int val = 0; val < 256; val++) {          
          for(int k = -M; k <= M; k++) {
            if( 0 <= val + k && val + k <= 255 ) {
              if( dp[i][val + k] > I + dp[i][val] ) {
                dp[i][val + k] = I + dp[i][val];
                change = true;
              }
            }
          }
        }
      }
      
    }
    
    int best = inf;
    for(int val = 0; val < 256; val++)
      checkmin( best, dp[N][val] );

    printf("Case #%d: ", tno);
    printf("%d\n", best);
  }
  return 0;
}
