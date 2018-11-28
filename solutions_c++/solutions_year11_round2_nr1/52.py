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

vector<double> solve() {
  int N; cin >> N;
  string s[N];
  REP(i, N) cin >> s[i];

  vector<double> res(N);
  vector<int> w(N),t(N);
  
  
  double WP[N][3];
  REP(i, N) {
    int win = 0;
    int total = 0;
    REP(j, N) {
      if (s[i][j]!='.') {
        total++;
        if (s[i][j] == '1')
          win++;              
      }
    }
    WP[i][0] = (double) win / total;
    w[i] = win;
    t[i] = total;
  }

  REP(i, N) {
    double acc = 0;
    int total = 0;
    REP(j, N) {
      if (s[i][j]!='.') {
        total++;
        int weight = (s[j][i] == '1') ? -1 : 0;
        acc += (double)(w[j] + weight) / (t[j] - 1);
      }
    }
    WP[i][1] = acc / total;
  }

  
  REP(i, N) {
    double acc = 0;
    int total = 0;
    REP(j, N) {
      if (s[i][j]!='.') {
        total++;
        acc += WP[j][1];
      }
    }
    WP[i][2] =  acc / total;
  }

  REP(i, N) {
    res[i] = 0.25 * WP[i][0] + 0.50 * WP[i][1] + 0.25 * WP[i][2];
  }
  
  return res;
}

int main() {
  int TNO; scanf("%d", &TNO);
  for(int tno = 1; tno <= TNO; tno++) {
    
    printf("Case #%d: \n", tno);

    vector<double> res = solve();
    REP(i, res.size()) {
      printf("%.10f\n", res[i]);
    }
  }
  return 0;
}
