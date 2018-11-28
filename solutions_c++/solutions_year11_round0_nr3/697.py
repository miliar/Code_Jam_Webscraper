#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
using namespace std;
#define rep(i,n) for(int i=0; i<n; i++)
#define all(c) (c).begin(), (c).end()

int main() {
  int T; scanf("%d", &T);
  
  for(int t=1; t<=T; t++) {
    int n; scanf("%d", &n);
    vector<int> v(n);
    rep(i, n) scanf("%d", &v[i]);
    sort(all(v));
    
    bool f = false;
    for(int i=1; i<(1<<21); i<<=1) {
      int sum = 0;
      rep(j, n) sum += ((v[j] & i) > 0);
      if(sum % 2) { f = true; break; }
    }
    
    if(f) { printf("Case #%d: NO\n", t); continue; }
    
    int total = 0;
    rep(i, n) total += v[i];
    printf("Case #%d: %d\n", t, total-v[0]);
  }
  
  return 0;
}
