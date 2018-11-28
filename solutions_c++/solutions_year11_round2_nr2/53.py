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

int C, D;
int P[202], V[202];

bool possible (double t) {
  double prev = -1e20;

  int done[202] = {0};
  for (int i = 0; i < C; ) {
    if (V[i] <= done[i]) {
      i++;
      continue;
    }
    double pos = P[i];
    done[i]++;
    
    if (prev + D <= pos - t) {
      prev = pos - t;
    } else if (prev + D <= pos + t) {
      prev = prev + D;
    } else {
      return false;
    }
    
  }
  
  
  return true;
}

double solve() {
  cin >> C >> D;
  REP(i, C) {
    cin >> P[i] >> V[i];
  }

  double hi = 1e20;
  double lo = 0;
  REP(loop, 200) {
    double mid = (hi + lo) / 2.0;
    if (possible(mid))
      hi = mid;
    else
      lo = mid;
  }
  return hi;
}

int main() {
  int TNO; scanf("%d", &TNO);
  for(int tno = 1; tno <= TNO; tno++) {
    double res = solve();
    printf("Case #%d: ", tno);
    printf("%.8f\n", res);

  }
  return 0;
}
