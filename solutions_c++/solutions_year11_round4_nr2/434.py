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
template<class T>void pv(T a,T b){for(T i=a;i!=b;++i)cerr<<*i<<" ";cout<<endl;}
template<class T> inline T sq(T x){return x * x;}
template<class T> inline void checkmin(T &a,T b){if(b<a)a=b;}
template<class T> inline void checkmax(T &a,T b){if(b>a)a=b;}

int R, C, D; 
vector<string> s;

bool possible (int K) {
  for (int r = 0; r + K <= R; r++) {
    for (int c = 0; c + K <= C; c++) {
      double vx = 0;
      double vy = 0;

      double M = (K - 1) / 2.0;
      REP(i, K) REP(j, K) {
        if ( (i == 0 || i == K - 1) &&
             (j == 0 || j == K - 1)) continue;
        
        vx += (i - M) * (s[r + i][c + j] - '0');
        vy += (j - M) * (s[r + i][c + j] - '0');
      }
      if (abs(vx) < 0.1 && abs(vy) < 0.1) {
        return true;
      }
    }
  }
  return false;
}

int solve() {
  s.clear();
  cin >> R >> C >> D;
  
  REP(r, R) {
    string line; cin >> line;
    s.push_back(line);
  }

  for (int k = min(R, C); k >= 3; k--) {
    if ( possible(k) ) return k;
  }  
  return -1;
}

int main() {
  int TNO; scanf("%d", &TNO);
  for(int tno = 1; tno <= TNO; tno++) {
    
    printf("Case #%d: ", tno);
    int res = solve();
    if (res == -1)
      cout << "IMPOSSIBLE" << endl;
    else
      cout << res << endl;

  }
  return 0;
}
