#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
using namespace std;
#define rep(i,n) for(int i=0; i<n; i++)
#define MAX_C 1001
typedef pair<int, int> ii;

int a[MAX_C];

int main() {
  int t, count = 0;
  scanf("%d", &t);

  while(t--) {
    int l, t, n, c;
    scanf("%d%d%d%d", &l, &t, &n, &c);
    rep(i, c) scanf("%d", &a[i]);
    
    int total = 0;
    rep(i, c) total += a[i];
    int r = total * (n / c) * 2;
    rep(i, n % c) r += a[i] * 2;
    
    vector<ii> v(c);
    rep(i, c) v[i] = ii(a[i], 0);
    
    {
      int tmp = 0, k = 0, i;
      for(i=0; i<n; i++, k = (k+1) % c) {
        tmp += a[k] * 2;
        if(tmp >= t) {
          v.push_back(ii((tmp-t)/2, 1));
          break;
        }
      }
      
      i++; k = (k+1) % c;
      
      for(; i<n; i++, k = (k+1) % c) {
        v[k].second++;
      }
      
      /*
        rep(i, v.size()) {
        cout << v[i].first << " " << v[i].second << endl;
        }
      */
      
      sort(v.begin(), v.end());
      reverse(v.begin(), v.end());
    }
    
    //cout << r << endl;
    
    for(int i=0, k=0; i<v.size() && k < l; i++) {
      for(int j=0; j<v[i].second && k < l; j++, k++) {
        r -= v[i].first;
      }
    }
    
    printf("Case #%d: %d\n", ++count, r);
  }
  
  return 0;
}
