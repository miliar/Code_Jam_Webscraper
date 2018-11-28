#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
#define rep(i,n) for(int i=0; i<n; i++)
#define all(c) (c).begin(), (c).end()

int main() {
  int t; cin >> t;
  for(int cs=1; cs<=t; cs++) {
    cout << "Case #" << cs << ": ";
    int n, m; cin >> n;
    vector<int> d(n), l(n), r(n,-1);
    r[0] = 0;
    rep(i,n) cin >> d[i] >> l[i];
    cin >> m;
    d.push_back(m);
    l.push_back(0);
    r.push_back(-1);
    n++;
    
    for(int i=0,j=1; i<n; i++) if(r[i]!=-1) {
      int x = min(d[i]+(d[i]-r[i]), d[i]+l[i]);
      for(; j<n&&d[j]<=x; j++) {
        r[j] = d[i];
      }
    }

    /*
    cout << endl;
    rep(i,n) cout << d[i] << " "; cout << endl;
    rep(i,n) cout << l[i] << " "; cout << endl;
    rep(i,n) cout << r[i] << " "; cout << endl;
      */
    cout << (r.back()==-1?"NO":"YES") << endl;
  }
  return 0;
}
