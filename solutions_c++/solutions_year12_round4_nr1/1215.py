#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>

#include <iostream>
#include <iterator>
#include <sstream>
#include <string>

#include <vector>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <functional>
using namespace std;

#define pb push_back
#define mp make_pair
#define all(cont) (cont).begin(),(cont).end()
#define sz(cont) int(cont.size())

#define eachx(it,beg,end) for(typeof(beg) it=beg; it!=end;++it)
#define each(it,cont) eachx(it,cont.begin(),cont.end())

#define rep(i,n) for(typeof(n) i=0; i<(n); ++i)
#define repx(i,s,t) for(typeof(s) i=(s); i<(t); ++i)
#define times(n) for(typeof(n) _=0; _<n; ++_)

#define mset memset
#define mcpy memcpy
#define mclr(x,sz) mset(x,0,sz)
int main() {
	int T, CAS=1;
	cin >> T;
	while(T--) {
		vector<int> ps;
		vector<int> ls;
		map<int, int> range;
		int n;
		cin >> n;
		rep(i,n) {
			int pos, len;
			cin >> pos >> len;
			ps.pb(pos);
			ls.pb(len);
		}
		int d;
		cin >> d;
		range[0] = 2 * ps[0];
		int j=1;
		rep(i,n) {
			for(;j<n; ++j) {
				if(ps[j]>range[i]) break;
				int _range = min(ps[j]+ls[j], 2*ps[j]-ps[i]);
				range[j] = max(range[j], _range);
			}
		}
		
		bool canReach = false;
		rep(i,n)
			if(range[i] >= d) canReach = true;
		
		cout << "Case #" << CAS++ << ": ";
		if(canReach) cout << "YES" << endl;
		else cout << "NO" << endl;
	}
	return 0;
}
