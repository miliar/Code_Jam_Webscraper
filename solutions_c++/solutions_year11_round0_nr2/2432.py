#include <iostream>
#include <cstdio>
#include <string>
#include <cstring>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <sstream>
#include <complex>
#include <cmath>
#include <iomanip>
#include <cstdlib>

using namespace std;
#define pb          push_back
#define all(a)      (a).begin(),(a).end()
#define sz(a)       (int)((a).size())
#define REP(i,j,k)  for(int i=j;i<k;++i)
#define rep(i,n)    for(int i=0;i<n;++i)
#define fori(T,v,i) for(T::iterator i = v.begin(); i != v.end(); i++)
#define forc(T,v,i) for(T::const_iterator i = v.begin(); i != v.end(); i++)
const int INF = 100000000;
const double EPS = 1e-8;
typedef long long ll;

int main () {
  int T; scanf("%d", &T);

  rep (tc, T) {
    int C, D, N;
    scanf("%d", &C); vector<string> cs(C); rep (i, C) cin >> cs[i];
    scanf("%d", &D); vector<string> ds(D); rep (i, D) cin >> ds[i];
    scanf("%d", &N); string s; cin >> s;
    string t = "";
    rep (i, N) {
      t += s[i];
      rep (j, C) {
	if (sz(t) < 2) break;
	if ((t[sz(t)-2] == cs[j][0] && t[sz(t)-1] == cs[j][1]) ||
	    (t[sz(t)-2] == cs[j][1] && t[sz(t)-1] == cs[j][0])) {
	  t.erase(sz(t)-1, 1);
	  t[sz(t)-1] = cs[j][2];
	}
      }

      rep (j, D) {
	rep (k, sz(t)-1) {
	  if ((t[k] == ds[j][0] && t[sz(t)-1] == ds[j][1]) ||
	      (t[k] == ds[j][1] && t[sz(t)-1] == ds[j][0])) {
	    t = "";
	  }
	}
      }
    }
    
    printf("Case #%d: [", tc+1);
    rep (i, sz(t)-1) cout << t[i] << ", ";
    if (sz(t))       cout << t[sz(t)-1];
    puts("]");
  }
  return 0;
}
