#include <map>
#include <set>
#include <stack>
#include <queue>
#include <cmath>
#include <string>
#include <vector>
#include <cstdio>
#include <sstream>
#include <complex>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

typedef long long       li;
typedef vector<li>      vi;
typedef complex<double> pt;
typedef pair<pt, pt>    line;
typedef pair<li, li>    pi;
typedef vector<string>  vs;

#define rep(i,to)       for(li i=0;i<((li)to);i++)
#define foreach(it,set) for(__typeof((set).begin()) it=(set).begin();it!=(set).end();it++)
#define all(v)          v.begin(), v.end()

inline li bit(li n){ return 1LL<<n; }
template <class T> ostream& operator<<(ostream& os, vector<T> x){
  foreach(it, x) os << *it << ' ';
  return os;
}
template <class T> inline void dbg(T x){
  // return;
  cerr << x << endl; 
}

li vx[8] = {1, -1, 0,  0, -1, 1,  1, -1};
li vy[8] = {0,  0, 1, -1, -1, 1, -1,  1};

ostream& operator<<(ostream& os, pt p){
  os << p.real() << ' ' << p.imag();
  return os;
}

double rrand(){
  return (double)rand() / (RAND_MAX- 1);
}

void solve(li casenum){
  vector<pt> ans;
  li n, w, l;
  cin >> n >> w >> l;
  vi r(n);
  rep(i, n) cin >> r[i];

  li tried = 0;
  while((li)ans.size() < n){
    if(tried < 100){
      pt tmp(rrand() * w, rrand() * l);
      li ok = 1;
      rep(i, ans.size()){
        if(abs(ans[i] - tmp) + 1e-6 < r[i] + r[ans.size()]){
          ok = 0;
          break;
        }
      }
      if(ok){
        ans.push_back(tmp);
        tried = 0;
      } else {
        tried++;
      }
    } else {
      ans.clear();
    }
  }

  cout << "Case #" << casenum << ": " << ans << endl;
  cerr << "solved : " << casenum << endl;
  return;
}

int main(){
  li t;
  cout.presicison(9);
  cin >> t;
  rep(i, t) solve(i+1);
  return 0;
}
