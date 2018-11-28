#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>

using namespace std;

int main() {
  int t;
  cin >> t;

  cout.precision(std::numeric_limits< double >::digits10);

  for(int tcase=1;tcase<=t;tcase++){

    int x, s, r, n;
    long double t;

    cin >> x >> s >> r >> t >> n;

    // long long extraa = r - s;
    // extraa *= t;
    // int extra;
    // if(extraa >= x) extra = x;
    // else extra = extraa;
    
    
    vector<pair<int, int> > a;

    int left=x;

    for(int i=0;i<n;i++){
      int b, e, w;
      cin >> b >> e >> w;
      a.push_back(make_pair(w, e-b));
      left -= (e-b);
    }

    a.push_back(make_pair(0, left));

    sort(a.begin(), a.end());
    
    //for(int i=0;i<a.size();i++)cerr << '(' << a[i].first << ' ' << a[i].second << ") ";cerr << '\n';

    typedef long double ldd;

    ldd sol = 0;

    for(vector<pair<int, int> >::iterator it=a.begin();it!=a.end();++it){
      if(it->second <= t * (it->first + r)) {
	sol += ldd(it->second)/(it->first + r);
	t -= ldd(it->second)/(it->first + r);
      } else {
	sol += t + (ldd(it->second) - t * (it->first + r))/(it->first + s);
	t = 0;
      }
    }
    cout << "Case #" << tcase << ": " << sol << '\n';
  }
}
