#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <complex>
#include <queue>
#include <stack>
#include <cstdlib>
#include <cmath>
#include <map>
#include <set>
#include <iomanip>

using namespace std;
#define pb push_back
#define all(a) (a).begin(),(a).end()
#define sz(a) (int)((a).size())
#define rep(i,n) for(int i=0; i<n; ++i)
#define fori(T,v,i) for(T::iterator i = v.begin(); i != v.end(); i++)
#define forc(T,v,i) for(T::const_iterator i = v.begin(); i != v.end(); i++)
static const double EPS = 1e-8;
typedef long long ll;



int main () {
  int T; cin >> T;
  rep (t, T) {
    int r, k, n; cin >> r >> k >> n;
    queue<int> g;
    rep (i, n) {
      int gn; cin >> gn;
      g.push(gn);
    }
        
    ll result = 0;

    rep (i, r) {
      int s = 0;
      vector<int> next;
      for (; !g.empty() && s+g.front() <= k; ) {
	next.pb(g.front());
	s += g.front();
	g.pop();
      }
      result += s;
      fori(vector<int>, next, e)g.push(*e);
    }
    
    cout << "Case #" << t+1 << ": " << result << endl;
  }
  return 0;
}
