#include<cstdio>
#include<iostream>
#include<queue>
#include<vector>
#include<string>
#include<algorithm>
#include<map>
#include<sstream>
#include<cmath>
#include<cctype>
#include<cassert>

using namespace std;

#define pf printf
#define sf scanf
#define VI vector<int>
#define pb push_back
#define fo(a,b) for(a=0;a<b;a++)

const int inf = 1000000000;

int main() {
	int cases, t;
	cin >> t;
	for( cases = 1; cases <= t; cases++ ) {
		int n; cin >> n; VI V; V.clear();
		int i, j; fo(i, n) { int a; cin >> a; V.pb(a); }
		int res = -1;
		fo(i, (1<<n) ) {
			int s, p;
			s = p = 0;
			int xs, xp; xs = xp = 0;
			fo(j, n) {
				if( i & (1<<j) ) { s += V[j]; xs ^= V[j]; }
				else { p += V[j]; xp ^= V[j]; }
			}
			if( xp == xs && p && s) res >?= p;
		}
		pf("Case #%d: ", cases);
		if( res == -1 ) pf("NO\n");
		else pf("%d\n", res);
	}
	return 0;
}

