// CPPFLAGS=-std=gnu++0x -W -Wall -g -O2
#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdint>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <limits>
#include <map>
#include <queue>
#include <set>
#include <string>
#include <vector>

using namespace std;

#define all(c) (c).begin(),(c).end()
#define foreach(i,c) for(auto i=(c).begin();i!=(c).end();++i)
template<class T> bool in(T e, const set<T>& s) { return s.find(e) != s.end(); }

int main() {
  int tests; if (scanf("%d",&tests)!=1) return 1;
  for (int t=1;t<=tests;++t) {
    printf("Case #%d: ",t);
    double X, S, R, T, N; if (scanf("%lf %lf %lf %lf %lf",&X,&S,&R,&T,&N)!=5) return 1;
    double x = 0.0;
    int i;
    priority_queue<pair<double, double> > q;
    for (i=0;i<N;++i) {
      double B, E, w; if (scanf("%lf %lf %lf",&B,&E,&w)!=3) return 2;
      q.push(make_pair(0.0,B-x));
      q.push(make_pair(-w,E-B));
      x=E;
    }
    q.push(make_pair(0.0,X-x));
    double ans = 0.0;
    while (!q.empty()) {
      pair<double, double> tmp = q.top(); q.pop();
      double w = -tmp.first;
      double x = tmp.second;
      double tr = x / (R + w);
      if (tr <= T) {
        T -= tr;
        ans += tr;
      } else {
        ans += T;
        x -= (R + w) * T;
        T = 0.0;
        ans += x / (S + w);
      }
    }
    printf("%.15lf\n",ans);
  }
}
