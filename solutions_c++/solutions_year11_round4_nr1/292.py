#include <iostream>
#include <iomanip>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
using namespace std;

int main(int argc, char *argv[])
{
  cout<<setiosflags(ios::fixed)<<setprecision(10);

  int cases; cin>>cases;
  for (int cn = 1; cn <= cases; cn++){
    int x, s, r, t, n;
    cin>>x>>s>>r>>t>>n;

    vector<pair<int, pair<int, int> > > w(n);
    for (int i=0; i<n; i++)
      cin>>w[i].first>>w[i].second.first>>w[i].second.second;

    sort(w.begin(), w.end());

    vector<pair<int, pair<int,int> > > v;
    int cur=0;
    for (int i=0; i<(int)w.size(); i++){
      v.push_back(make_pair(0, make_pair(cur, w[i].first)));
      v.push_back(make_pair(w[i].second.second, make_pair(w[i].first, w[i].second.first)));
      cur = w[i].second.first;
    }
    v.push_back(make_pair(0, make_pair(cur, x)));

    sort(v.begin(), v.end());

    double rt = t;
    double ans = 0;
    for (int i=0; i<(int)v.size(); i++){
      double span = v[i].second.second - v[i].second.first;
      double tm = span / (r + v[i].first);
      tm = min(rt, tm);
      
      rt -= tm;
      span -= (r + v[i].first) * tm;
      ans += tm;
      ans += span / (s + v[i].first);
    }

    cout<<"Case #"<<cn<<": "<<ans<<endl;
  }
  
  return 0;
}
