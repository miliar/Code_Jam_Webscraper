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

struct Interval {
  int beg, end;
  int w;

  bool operator < (const Interval &o) const {
    return w < o.w;
  }
};

double solve() {
  int X, S, R, N;
  double t;
  cin >> X >> S >> R >> t >> N;
  vector<int> v;
  vector<Interval> intervals;  
  REP(i, N) {
    int B, E, w; cin >> B >> E >> w;
    v.push_back(B);
    v.push_back(E);
    intervals.push_back( (Interval) {B, E, w} );
  }
  
  {
    v.push_back(0);
    v.push_back(X);
    sort(ALL(v));    
    for (int i = 0; i < v.size(); i += 2) {
      intervals.push_back( (Interval) {v[i], v[i + 1], 0} );
    }
  }

  sort(ALL(intervals));

  double res = 0;
  REP(i, intervals.size()) {
    const Interval& I = intervals[i];
    if (t > 0) {
      double need = (double)(I.end - I.beg) / (I.w + R);
      if (need < t) {
        t -= need;
        res += need;
      } else {
        double sat = t * (I.w + R);        
        res += t;
        res += (double)(I.end - I.beg - sat) / (I.w + S);
        t = 0;
      }
    } else {
      res += (double)(I.end - I.beg) / (I.w + S);
    }
  }
  return res;
  
}
int main() {
  int TNO; scanf("%d", &TNO);
  for(int tno = 1; tno <= TNO; tno++) {
    
    printf("Case #%d: %.10f\n", tno, solve());
    
  }
  return 0;
}
