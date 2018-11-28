#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cstdio>
using namespace std;
#define rep(i,n) for(int i=0; i<n; i++)
#define all(c) (c).begin(), (c).end()
#define INF (1<<28)
#define EPS (1e-8)
typedef long long ll;

struct dd {
  double len, speed;
  dd() {}
  dd(double len, double speed): len(len), speed(speed) {}
  bool operator<(const dd& o) const {
    return speed < o.speed;
  }
};

int main() {
  int T, x, s, r, t, n, tc = 0;
  scanf("%d", &T);
  
  while(T--) {
    scanf("%d%d%d%d%d", &x, &s, &r, &t, &n);
    vector<dd> v;
    int len = 0;
    rep(i, n) {
      int b, e, w; scanf("%d%d%d", &b, &e, &w);
      len += (e - b);
      v.push_back(dd(e-b, w));
    }
    v.push_back(dd(x-len, 0));
    sort(all(v));
    
    double res = 0.0, rest = t, i;
    for(i=0; i<v.size() && rest>EPS; i++) {
      if(v[i].len > (v[i].speed+r)*rest) {
        res += rest;
        v[i].len -= (v[i].speed+r)*rest;
        rest = 0;
        i--;
      }
      else {
        res += v[i].len / (v[i].speed+r);
        rest -= v[i].len / (v[i].speed+r);
      }
    }
    for(; i<v.size(); i++) {
      res += v[i].len / (v[i].speed+s);
    }
    
    
    printf("Case #%d: %lf\n", ++tc, res);
  }
  
  return 0;
}
