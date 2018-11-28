#include <iostream>
#include <iomanip>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <utility>
#include <algorithm>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>

using namespace std;

#define REP(i,n) for(int i = 0; i < (int)(n); i++)
#define rep(i,m,n) for(int i = m; i < (int)(n); i++)
#define FOR(i,c) for(__typeof((c).begin()) i = (c).begin(); i != (c).end(); ++i)
#define ALLOF(c) (c).begin(), (c).end()

typedef double decimal;
const decimal EPS = 1e-8;

typedef complex<decimal> P;
struct C {
  P p;
  decimal r;
};

int nCases;
int N;
C p[40];

bool points(C p, C q, decimal r, P *ps){
  if(p.r > r || q.r > r) return false;
  C c1 = {p.p, r - p.r};
  C c2 = {q.p, r - q.r};
  decimal d = abs(c1.p - c2.p);
  if(d - EPS > c1.r + c2.r) return false;
  decimal rc = (d*d + c1.r*c1.r - c2.r*c2.r) / (2*d);
  decimal rs = sqrt(c1.r*c1.r - rc*rc);
  P diff = (c2.p - c1.p) / d;
  ps[0] = c1.p + diff * P(rc, rs);
  ps[1] = c1.p + diff * P(rc, -rs);
  return true;
}

bool solve(int i, int j, decimal r, vector<int> inv[2]){
  P ps[2];
  bool _ = points(p[i], p[j], r, ps);
  if(!_) return false;
  bool ok = false;
  REP(px, 2){
    inv[px].clear();
    REP(k, N){
      if(abs(p[k].p - ps[px]) - (r - p[k].r) > EPS) inv[px].push_back(k);
    }
  }
  return true;
}

bool check(vector<int>& a1, vector<int>& a2){
  bool c[40];
  REP(i, 40) c[i] = false;
  REP(i, a1.size()){
    c[a1[i]] = true;
  }
  REP(i, a2.size()){
    if(c[a2[i]]) return false;
  }
  return true;
}

int main(){
  scanf("%d ", &nCases);
  REP(ic, nCases){
    cin >> N;
    REP(i, N){
      decimal x, y, r;
      cin >> x >> y >> r;
      p[i].p = P(x, y);
      p[i].r = r;
    }
    decimal lo = 0;
    decimal hi = 5000;
    decimal ret;
    if(N == 1){
      ret = p[0].r;
      goto shortcut;
    }else if(N == 2){
      ret = max(p[0].r, p[1].r);
      goto shortcut;
    }
    while(hi - lo > EPS){
      decimal r = (hi + lo) / 2;
      bool ok = false;
      REP(j, N) REP(i, j){
        vector<int> inv[2];
        if(!solve(i, j, r, inv)) continue;
        REP(px, 2){
          switch(inv[px].size()){
           case 0:
            ok = true;
            break;
           case 1:
            ok = p[inv[px][0]].r - r < EPS;
            break;
           default:
            {
              REP(y, inv[px].size()) REP(x, y){
                int X = inv[px][x];
                int Y = inv[px][y];
                vector<int> inv2[2];
                if(!solve(X, Y, r, inv2)) continue;
                REP(px2, 2){
                  if(check(inv[px], inv2[px2])){
                    ok = true;
                    break;
                  }
                }
                if(ok) break;
              }
            }
            break;
          }
          if(ok) break;
        }
        if(ok) break;
      }
      if(ok){
        hi = r;
      }else{
        lo = r;
      }
    }
    ret = (hi + lo) / 2;
shortcut:

    printf("Case #%d: %.10f\n", ic+1, ret);
  }

  return 0;
}

