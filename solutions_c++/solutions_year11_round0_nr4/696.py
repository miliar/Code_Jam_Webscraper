#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
using namespace std;
#define rep(i,n) for(int i=0; i<n; i++)
#define all(c) (c).begin(), (c).end()

double e(int k) {
  if(k <= 1) return 0.0;
  return k;
}

int main() {
  int T; scanf("%d", &T);
  
  for(int t=1; t<=T; t++) {
    int n; scanf("%d", &n);
    int v[n];
    rep(i, n) { scanf("%d", &v[i]); v[i]--; }
    
    double r = 0;
    bool vst[n]; rep(i, n) vst[i] = false;
    rep(i, n) {
      if(vst[i]) continue;
      int j = 0;
      while(!vst[i]) {
        vst[i] = true;
        i = v[i];
        j++;
      }
      r += e(j);
    }
    
    printf("Case #%d: %lf\n", t, r);
  }
  
  return 0;
}
