#include <string>
#include <cstring>
#include <vector>
#include <cmath> 
#include <cstdio>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <algorithm>
#include <utility>
#include <sstream>
#include <iostream>
 
using namespace std;
 
#define REP(a,n) for(int a=0; a<(n); ++a)
#define FOR(a,b,c) for(int a=(b); a<=(c); ++a)
#define INIT(a, v) __typeof(v) a = (v)
#define FOREACH(a, v) for (INIT(a, (v).begin()); a!=(v).end(); ++a)
 
template<class T>
inline int size(const T&t){return t.size();}
 
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef long long LL;

#define INF 1000000000
#define PB push_back
#define MP make_pair
 
//////////////////////////////////////////

int W,s[2],G;
double x[2][105];
double y[2][105];

double licz_pole(double do_x) {
  double pole[2];
  REP(n, 2) {
    pole[n] = 0;
    REP(a, s[n]-1) {
      double pr = x[n][a+1];
      double pry = y[n][a+1];
      if (do_x<pr) {
        pry = y[n][a]+(pry-y[n][a])*(do_x-x[n][a])/(pr-x[n][a]);
        pr = do_x;
      }
      pole[n] += (pr-x[n][a])*(pry+y[n][a]);
      if (do_x<=pr)
        break;
    }
  }
  return pole[1]-pole[0];
}

void szukaj(double ma_byc) {
  double l = 0, p = W;
  REP(a, 50) {
    double m = (l+p)/2;
    double pole = licz_pole(m);
    if (pole<ma_byc)
      l = m;
    else
      p = m;
  }
  printf("%.6f\n", l);
}

int main() {
    int TT;
    scanf("%d", &TT);
    REP(tt, TT) {
        scanf("%d%d%d%d", &W, &s[0], &s[1], &G);
        REP(a, s[0])
          scanf("%lf%lf", &x[0][a], &y[0][a]);
        REP(a, s[1])
          scanf("%lf%lf", &x[1][a], &y[1][a]);
        double pole = licz_pole(W);
        printf("Case #%d:\n", (tt+1));
        FOR(n, 1, G-1)
            szukaj(pole*n/G);
    }
}


