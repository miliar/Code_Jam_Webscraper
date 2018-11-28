#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(i=0;i<n;i++)
#define F1(i,n) for(i=1;i<=n;i++)
const int inf = 1000000009;
const double pi = atan(1.0)*4.0;
const double eps = 1e-8;
ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }
int bc(int n) { return n ? bc((n-1)&n)+1 : 0; }

int i, j, k, m, n, l, ans;

char ss[1000002];
int p[1500], c[15][1500], d[15][15][1500];

int rec(int i, int b, int w) {
	if (i == -1) {
		if (b < n-p[w]) return inf; else return 0;
	}
	int& ret = d[i][b][w];
	if (ret == -1) {
//		cout << i << " " << b << " " << w << endl;
		ret = inf;
		// don't
		ret = min(ret, rec(i-1, b, 2*w) + rec(i-1, b, 2*w+1));
		// buy
		ret = min(ret, rec(i-1, b+1, 2*w) + rec(i-1, b+1, 2*w+1) + c[i][w]);
	}
	return ret;
}

int main() {
//	freopen("b.in", "r", stdin);

//	freopen("B-small-attempt0.in", "r", stdin);
//	freopen("B-small-attempt0.out", "w", stdout);

	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int tt, tn; cin >> tn;
	F1(tt,tn) {
		cin >> n;
		m = (1<<n);
		F0(i,m) cin >> p[i];
		F0(i,n) F0(j, (1<<(n-1-i))) cin >> c[i][j];
		memset(d, -1, sizeof(d));
		ans = rec(n-1, 0, 0);
		printf("Case #%d: ", tt);
		cout << ans << endl;
	}
	
	return 0;
}
