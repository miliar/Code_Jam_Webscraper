#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
using namespace std;
#define rep(i,n) for(int i=0; i<n; i++)
#define all(c) (c).begin(), (c).end()
typedef pair<int, int> ii;

int n, bn, on;
vector<ii> bv, ov;

int solve() {
  int r = 0, i = 0;
  int bp = 1, op = 1;
  int bi = 0, oi = 0;
  
  while(i < n) {
    bool f = false;
    if(bi < bn) { // Blue
      if(bv[bi].second == bp && i == bv[bi].first)
        { bi++; i++; f = true; }
      else {
        if(bp < bv[bi].second) bp++;
        else if(bp > bv[bi].second) bp--;
      }
    }
    if(oi < on) { // Orange
      if(ov[oi].second == op && i == ov[oi].first && !f)
        { oi++; i++; }
      else {
        if(op < ov[oi].second) op++;
        else if(op > ov[oi].second) op--;
      }
    }
    r++;
  }
  
  return r;
}

int main() {
  int T; scanf("%d", &T);
  
  for(int t=1; t<=T; t++) {
    scanf("%d", &n);
    bv.clear(); ov.clear();
    rep(i, n) {
      char r[2]; int p; scanf("%s%d", r, &p);
      if(r[0] == 'B') bv.push_back(ii(i, p));
      else ov.push_back(ii(i, p));
    }
    bn = bv.size(); on = ov.size();
    printf("Case #%d: %d\n", t, solve());
  }
  
  return 0;
}
