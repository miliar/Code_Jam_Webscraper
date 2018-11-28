#include <algorithm>
#include <climits>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <iterator>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <string> 
#include <vector>

using namespace std;

typedef long long ll;

ll choose (ll n, ll k) {
  if (k==0) return 1;
  if (k>n) return 0;
  if (k==n) return 1;
  ll ret = 1;
  for (ll i = 0; i < k; ++i)  ret*=n-i;
  for (ll i=1; i<=k; ++i) ret/=i;
  return ret;
}


int main() {

  // cout << choose (2,1) << "\n";
  
  int num_cases;
  cin >> num_cases;
  for (int case_num = 1; case_num <= num_cases; ++case_num) {
    ll n, A, B, C, D, x0, y0, M;
    cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
    
    ll X = x0, Y = y0;
    // vector<pair<ll,ll> > points;
    ll moddat[3][3];
    for (int i = 0; i < 3; ++i) {
      for (int j = 0; j < 3; ++j) {
        moddat[i][j] = 0;
      }
    }
    ++moddat[((X%3)+3)%3][((Y%3)+3)%3];
    // points.push_back (make_pair (X,Y));
    // print X, Y
    for (int i = 1; i < n; ++i) {
      // for i = 1 to n-1
      X = (A * X + B) % M;
      Y = (C * Y + D) % M;
      ++moddat[((X%3)+3)%3][((Y%3)+3)%3];
      // points.push_back (make_pair (X,Y));
    }
    // for (int i = 0; i < (int)points.size();++i) {
    //   ++moddat[((points[i].first%3)+3)%3][((points[i].second%3)+3)%3];
    //   // cerr << points[i].first << " " << points[i].second << "\n";
    // }
    vector<int> conf (6,0);
    bool good=true;
    ll ret = 0;
    set<vector<vector<int> > > seen;
    while (good) {
      vector<vector<int> > taken (3, vector<int> (3, 0));
      int xmod=0,ymod=0;
      for (int i = 0; i < 3; ++i) {
        ++taken[conf[2*i]][conf[2*i+1]];
        xmod += conf[2*i];
        ymod += conf[2*i+1];
      }
      
      xmod%=3;
      ymod%=3;
      if (!(xmod != 0 || ymod != 0 || seen.find (taken) != seen.end())) {
        // copy (conf.begin(), conf.end(), ostream_iterator<int>(cerr, " " ));
        // cerr << ".";
      
        seen.insert (taken);
        ll curr = 1;
        for (int i = 0; i < 3; ++i) {
          for (int j = 0; j < 3; ++j) {
            // cerr << moddat[i][j] << " " << taken[i][j] << "\n";
            curr *= choose (moddat[i][j],taken[i][j]);
          }
        }
        // cerr << curr << "\n" ;
      
      
        ret += curr;
      }
      
      good = false;
      for (int i = 0; i < 6; ++i) {
        if (conf[i]<2) {
          good = true;
          ++conf[i];
          break;
        }
        else conf[i] = 0;
      }
    }
    cout << "Case #"<< case_num << ": " << ret << "\n";
  }
  
  
  
}

