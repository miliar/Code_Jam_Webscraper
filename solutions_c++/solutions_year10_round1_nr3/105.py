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

const int SIZE = 5000;
char dp[5000][5000];

int rec(int a, int b) {
  if( a > b ) swap(a, b);
  
  if( a <= 0 || b <= 0 ) return 1;
  if( a == b ) return 0;
  if( b % a == 0 ) return 1;
  
  if( a < SIZE && b < SIZE ) if( dp[a][b] != -1 ) return dp[a][b];

  int res = 0; // win == 1, lose = 0;

  for(int k = max(1, b / a - 2); b - k * a > 0; k++) {
    int t = rec( a, b - k * a);
    if( t == 0 ) {
      res = 1;
      break;
    }
  }
  if( a < SIZE && b < SIZE ) dp[a][b] = res;
  return res;
}

int main() {
  int TNO;
  scanf("%d", &TNO);
  for(int tno = 1; tno <= TNO; tno++) {
    memset( dp, -1, sizeof(dp) );
    
    printf("Case #%d: ", tno);
    int A1, A2, B1, B2;
    scanf("%d%d%d%d", &A1, &A2, &B1, &B2);

    double phi = (1.0 + sqrt(5.0)) / 2.0;
    double r = 1.0 / phi; 
    
    long long ans = 0;
    for(int A = A1; A <= A2; A++) {
      int th = A * 1.0 * r;
      
      if( B1 <= th ) {
        int add = 0;
        if( th <= B2 ) 
          add = th - B1 + 1;
        else
          add = B2 - B1 + 1;
        ans += add;        
      }
    }
    swap(A1, B1);
    swap(A2, B2);
    for(int A = A1; A <= A2; A++) {
      int th = A * 1.0 * r;
      if( B1 <= th ) {
        int add = 0;
        if( th <= B2 ) 
          add = th - B1 + 1;
        else
          add = B2 - B1 + 1;
        ans += add;
      }
    }
    printf("%lld\n", ans);   
  }  
  return 0;
}
