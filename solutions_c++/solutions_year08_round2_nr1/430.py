#include <iostream>
#include <algorithm>
#include <utility>
#include <sstream>
#include <vector>
using namespace std;

typedef __int64 ll;
typedef pair<ll,ll> ii;
#define sz(x) (int)(x).size()
#define pb push_back
#define clr(x) (x).clear()
#define all(x) (x).begin(), (x).end()

vector<ii> generate( int x0, int y0, int a, int b, int c, int d, int m, int n ) {
	int i;
   	ll x, y;
	vector<ii> ret;
	ret.pb(ii(x0,y0));
	x = x0;
	y = y0;
	for(i=1;i<=n-1;++i) {
		x = ( a * x + b ) % m;
		y = ( c * y + d ) % m;
		ret.pb(ii(x,y));
	}
	return ret;
}

int solve(vector<ii> &p) {
	int i, j, k;
	ll x, y;
	int ret = 0;
	for(i=0;i<sz(p);++i) for(j=i+1;j<sz(p);++j) for(k=j+1;k<sz(p);++k) {
		x = p[i].first + p[j].first + p[k].first;
		y = p[i].second + p[j].second + p[k].second;
		if(x%3==0&&y%3==0) ++ret;
	}
	return ret;
}

int main() {
	int tn, cc, ret;
	int n, a, b, c, d, x0, y0, m;
	cin >> tn;
	for(cc=1;cc<=tn;++cc) {
		cin >> n >> a >> b >> c >> d >> x0 >> y0 >> m;
		vector<ii> p = generate(x0,y0,a,b,c,d,m,n);
		// for(int i=0;i<sz(p);++i) cerr << p[i].first << ' ' << p[i].second << endl;
		ret = solve(p);
		printf("Case #%d: %d\n", cc,ret);
	}
	
}
