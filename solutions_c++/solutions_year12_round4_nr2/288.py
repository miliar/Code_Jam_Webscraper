#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
using namespace std;
#define rep(i,n) for(int i=0; i<n; i++)
#define all(c) (c).begin(), (c).end()
inline int rd() { srand(rand()); return rand(); }
const double eps = 1e-4;
const int inf = (1<<28);

double dist(double x1, double y1, double x2, double y2) {
  return hypot(x1-x2, y1-y2);
}

double f(const vector<double> &X, const vector<double> &Y, const vector<double> &R, int n, double x, double h) {
  double y = 0.0;
  rep(i,n) {
    if(X[i]+R[i]<x   -R[n]) continue;
    if(x   +R[n]<X[i]-R[i]) continue;
    double lb = Y[i], ub = h;
    rep(k,30) {
      double m = (lb+ub)/2.0;
      if(dist(X[i],Y[i],x,m)<R[i]+R[n]+eps) lb = m;
      else ub = m;
    }
    y = max(y, ub);
  }
  return y;
}

int main() {
  srand(time(NULL));
  int t; cin >> t;
  for(int cs=1; cs<=t; cs++) {
    int n, w, h; cin >> n >> w >> h;
    vector<double> X(n), Y(n), R(n);
    rep(i,n) cin >> R[i];
    rep(i,n) {
      double _x, _y=inf;
      rep(k,100) {
        double x=rd()%(w+1),y=f(X,Y,R,i,x,h);
        if(y<_y) _x=x, _y=y;
      }
      X[i]=_x, Y[i]=_y;
    }

    cout << "Case #" << cs << ": ";
    rep(i,n) printf("%.4lf %.4lf ", X[i], Y[i]);
    cout << endl;
  }
  return 0;
}
