#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;
#define pb         push_back
#define all(a)     (a).begin(),(a).end()
#define rll(a)     (a).rbegin(),(a).rend()
#define sz(a)      (int)((a).size())
#define rep(i,n)   for(int i=0; i<n; ++i)
#define REP(i,j,k) for(int i=j; i<k; ++i)

int main () {
  int TC; scanf("%d", &TC);
  rep (tc, TC) {
    int n, s, p; scanf("%d %d %d", &n, &s, &p);
    vector<int> v(n);
    rep (i, n) scanf("%d", &v[i]);
    sort(rll(v));
    int result = 0;
    int m = 0;
    rep (i, n) m += v[i] > 1;
    rep (i, n) {
      int no = v[i]/3 + (v[i]%3 != 0);
      int su = (v[i]>1 && v[i]<29)?(v[i]-2)/3+2:-1;
      if (su > -1 && s > 0 && m-i == s) {
	s--;
	if (su >= p) result++;
      } else {
	if (no >= p) result++;
	else if (s > 0 && su >= p) {
	  s--;
	  result++;
	}
      }
    }
    cout << "Case #" << tc+1 << ": " << (s?0:result) << endl;
  }
  return 0;
}
