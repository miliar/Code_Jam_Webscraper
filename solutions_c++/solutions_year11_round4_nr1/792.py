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

#define debug 0

const int inf = 1000000000;

struct node {
	int start, end;
	int w;
};

vector<node> V;

bool cmp(const node &a, const node &b) {
	return a.w < b.w;
}

int main() {
	int test, cases = 1;
	cin >> test;
	for( cases=1; cases<=test; cases++ ) {
		int X, S, R, t, N;
		cin >> X >> S >> R >> t >> N;
		V.clear();
		int i;
		fo(i, N) {
			node A; cin >> A.start >> A.end >> A.w;
			V.pb(A);
		}
		sort(V.begin(), V.end(), cmp);
		double sum = 0;
		for(i=0;i<V.size();i++) sum += (V[i].end-V[i].start);
		double rem = X - sum;

		double res = 0;
		double tm_rem = t;

		double a = rem / R;
		if( a > tm_rem) {
			res += t;
			tm_rem = -1;
			rem -= t*R;
			res += rem / S;
		}
		else {
			res += a;
			tm_rem -= a;
		}
if( debug ) cout << "--" << res << endl;
		for(i=0;i<V.size();i++) {
			if( tm_rem < 0 ) {
				res += 1.0 * (V[i].end - V[i].start) / (V[i].w + S); 
			}
			else {
				double speed = V[i].w + R;
				double tm = 1.0 * (V[i].end - V[i].start) / speed;
				if( tm > tm_rem ) {
					res += tm_rem;
					double dis = tm_rem * speed;
					dis = 1.0 * (V[i].end - V[i].start) - dis;
					tm_rem = -1;
					res += dis / (V[i].w + S);
				}
				else {
					res += tm;
					tm_rem -= tm;
				}
			}
		}
		pf("Case #%d: %.9lf\n", cases, res);

	}
	return 0;
}
