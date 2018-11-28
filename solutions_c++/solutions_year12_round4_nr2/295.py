#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cctype>
#include <cmath>
#include <cassert>
#include "../../../../print.hpp"

using namespace std;

#define all(c) (c).begin(), (c).end()
#define iter(c) __typeof((c).begin())
#define cpresent(c, e) (find(all(c), (e)) != (c).end())
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define tr(c, i) for (iter(c) i = (c).begin(); i != (c).end(); ++i)
#define pb(e) push_back(e)
#define mp(a, b) make_pair(a, b)


vector<pair<double, int> > r;
int n;
int w, l;
vector<double> x, y;

int inf = 100000000;
double eps = 1e-9;

bool far(int i, int j) {
  int idi = r[i].second;
  int idj = r[j].second;
  return (r[i].first + r[j].first)*(r[i].first + r[j].first) < (x[idi]-x[idj])*(x[idi]-x[idj]) + (y[idi]-y[idj])*(y[idi]-y[idj]) -eps;
}

bool solve() {
  srand(time(NULL));
  sort(all(r));
  reverse(all(r));
  rep(i, n) {
    while(true) {
      int id = r[i].second;
      double rx = rand() % inf;
      double ry = rand() % inf;
      double xx = (double)w * rx / inf;
      double yy = (double)l * ry / inf;
      x[id] = xx;
      y[id] = yy;
      bool ok = true;
      rep(j, i) {
	if(!far(i, j)) {
	  ok = false;
	  break;
	}
      }
      if(ok) {
	break;
      }
    }
  }

}

double sqr(double x) {
  return x*x;
}

bool check() {
  rep(i, n) {
    rep(j, n) {
      if(i == j) {
	continue;
      }
      double ri = r[i].first;
      double rj = r[j].first;
      double xi = x[r[i].second];
      double xj = x[r[j].second];
      double yi = y[r[i].second];
      double yj = y[r[j].second];
      if(sqr(ri+rj) > sqr(xi-xj)+sqr(yi-yj)) {
	cout << "out " << i << " " <<  j << endl;
      }
    }
  }
}


int main(){
  int t; scanf("%d\n", &t);
  for(int j = 1;j<=t;j++){
    cin >> n >> w >> l;
    r.clear(); r.resize(n);
    rep(i, n) {
      int b; cin >> b;
      r[i] = mp(b, i);
    }
    x.clear(); x.resize(n);
    y.clear(); y.resize(n);

    solve();
    check();

    cout << "Case #" << j << ": ";
    rep(i, n) {
      if(i == n-1) {
	printf("%.9f %.9f", x[i], y[i]);
      }else {
	printf("%.9f %.9f ", x[i], y[i]);
      }
    }
    cout << endl;
  }
  return 0;

}
