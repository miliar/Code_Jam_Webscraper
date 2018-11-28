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

int c, d;
VI V;

int main() {
	int test, cases;
	cin >> test;
	for( cases=1; cases<=test; cases++ ) {
		cin >> c >> d;
		V.clear();
		int i;
		for(i=0;i<c;i++) {
			int p, v; cin >> p >> v;
			while(v--) V.pb(p);
		}
		
		double high = 1e9;
		double low = 0;

		int t = 1000;
		int n = V.size();
		while(t--) {
			double mid = (high + low)/2;
			double last = 1e15;
			for(i=n-1;i>=0;i--) {
				double k = last - d;
				double a, b;
				a = V[i] - mid;
				b = V[i] + mid;
				if( a < k && b > k ) last = k;
				else if( b < k ) last = b;
				else if( a > k) break;
			}
			if( i < 0 ) high = mid;
			else low = mid;
		}
		pf("Case #%d: %.3lf\n", cases, (low+high)/2);
	}
	return 0;
}
