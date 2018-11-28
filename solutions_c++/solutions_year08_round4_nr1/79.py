#include <iostream>
#include <sstream>
#include <stdio.h>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <list>
#include <stack>
#include <string>
#include <algorithm>
#include <numeric>
#include <math.h>
using namespace std;

#define TR(it, c) for(typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
#define rTR(it, c) for(typeof((c).rbegin()) it = (c).rbegin(); it != (c).rend(); ++it)
#define REP(i,n) for(int i=0; i<(int)(n); ++i)
#define rREP(i, n) for(int i = (int)(n) - 1; i >=0; --i)
#define sz size()
#define all(c) (c).begin(), (c).end()

#define mp make_pair
#define pb push_back

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<bool> vb;

#define fi first
#define se second


void help(pii &a, pii &b, pii &c, int G, int d) {
	if (G == 0) {
		if (a.se != INT_MAX && b.se != INT_MAX) c.se <?= d + a.se + b.se;
						
		if (a.fi != INT_MAX && b.se != INT_MAX) c.fi <?= d + a.fi + b.se;
		if (a.se != INT_MAX && b.fi != INT_MAX) c.fi <?= d + a.se + b.fi;
		if (a.fi != INT_MAX && b.fi != INT_MAX) c.fi <?= d + a.fi + b.fi;
	}else{ // and
		if (a.fi != INT_MAX && b.fi != INT_MAX) c.fi <?= d + a.fi + b.fi;
						
		if (a.fi != INT_MAX && b.se != INT_MAX) c.se <?= d + a.fi + b.se;
		if (a.se != INT_MAX && b.fi != INT_MAX) c.se <?= d + a.se + b.fi;
		if (a.se != INT_MAX && b.se != INT_MAX) c.se <?= d + a.se + b.se;		
	}	
}

void solve() {
	int M, V, i = 0, tmp;
	vpii DP(15000, mp(INT_MAX, INT_MAX)); 
	vi G(15000), C(15000, 0);	
	
	cin >> M >> V;
	
	REP(j, (M-1) / 2) {
		cin >> G[i] >> C[i];
		++i;
	}
	
	REP(j, (M+1)/2) {
		cin >> tmp;
		if (tmp == 1) DP[i].fi = 0; else DP[i].se = 0;
		++i;
	}
	
			
	rREP(i, (M-1)/2) {
		pii &a = DP[2*i+1], &b = DP[2*i+2], &c = DP[i];
		
		help(a, b, c, G[i], 0);
		if (C[i] == 1) help(a, b, c, 1-G[i], 1);
	}
	
	int res = (V == 1 ? DP[0].fi: DP[0].se);
	
	if (res == INT_MAX) cout << "IMPOSSIBLE"; else cout << res;
}

int main() {
	int n; cin >> n;
	REP(i, n) 
		{ cout << "Case #" << i+1 << ": "; solve(); cout << endl; }		
	return 0;
}
