#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cctype>

#include <algorithm>
#include <bitset>
#include <complex>
#include <deque>
#include <functional>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <sstream>
#include <string>
#include <utility>
#include <vector>

#include <ext/hash_set>
#include <ext/hash_map>
#include <ext/numeric>
#include <ext/functional>
#include <ext/rope>
#include <ext/rb_tree>
#include <ext/iterator>
#include <ext/slist>

#define PB push_back
#define ALL(x) (x).begin(),(x).end()
#define SZ(x) ((int)(x).size())
#define REP(i, n) for(int i=0; i<n; ++i)
#define REPD(i, n) for(int i=(n)-1; i>=0; --i)
#define FOR(i, b, e) for(typeof(e) i=b; i!=e; ++i)

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef istringstream ISS;

const double EPS=1e-9;

double circleline(double R, double l) {
  if(l>R-EPS) return M_PI*R*R;
  if(l<-R+EPS) return 0.0;
  double t=l/R;
  return 2.0*R*R*(2*t*sqrt(1-t*t)+2*asin(t)+M_PI)/4.0;
}

double circlerect(double R, double x, double y) {
  if(x<-R+EPS || y<-R+EPS) return 0.0;
  if(x>R-EPS) return circleline(R, y);
  if(y>R-EPS) return circleline(R, x);
  if(x>0.0) return circleline(R, y)-circlerect(R, -x, y);
  if(y>0.0) return circleline(R, x)-circlerect(R, x, -y);
  if(x*x+y*y>R*R-EPS) return 0.0;
  return (circleline(R, x)-circleline(R, -sqrt(R*R-y*y)))/2.0-(-y)*(x+sqrt(R*R-y*y));
}

double doit() {
  double f, Router, t, r, g;

  cin >> f >> Router >> t >> r >> g;

  double a=g+2.0*r;
  r+=f;
  if(g-2.0*f<EPS) return 1.0;

  double Rinner=Router-f-t;

  if(Rinner<EPS) return 1.0;

//  printf("Rinner %lf, r %lf, a %lf\n", Rinner, r, a);

  double res=M_PI*(Router*Router-Rinner*Rinner);

//  cout << res << endl;
  int bound=(int)((Rinner+r)/a)+1;
  for(int i=-bound; i<=bound; i++) {
    double opp=circleline(Rinner, a*i+r)-circleline(Rinner, a*i-r);
//    cout << opp << " ";
    res+=2.0*opp;
  }
//  cout << endl;
  for(int i=-bound; i<=bound; i++) {
    for(int j=-bound; j<=bound; j++) {
      double xh=a*i+r, xl=a*i-r;
      double yh=a*j+r, yl=a*j-r;
      double opp=circlerect(Rinner, xh, yh)-circlerect(Rinner, xh, yl)-circlerect(Rinner, xl, yh)+circlerect(Rinner, xl, yl);
//      cout << i << "," << j << " " << -opp << " ";
      res-=opp;
    }
  }
  //cout << endl;
  return res/(M_PI*Router*Router);
}

int main() {
  int nruns;
  cin >> nruns;
  REP(i, nruns) printf("Case #%d: %lf\n", i+1, doit());
/*
  cout << circlerect(1,-0.5,-0.5) << endl;
  cout << circlerect(1,0.5,-0.5) << endl;
  cout << circlerect(1,-0.5,0.5) << endl;
  cout << circlerect(1,0.5,0.5) << endl;
  cout << circlerect(1,0.5,0.5)-circlerect(1,-0.5,0.5)-circlerect(1,0.5,-0.5)+circlerect(1,-0.5,-0.5) << endl;*/
  return 0;
}
