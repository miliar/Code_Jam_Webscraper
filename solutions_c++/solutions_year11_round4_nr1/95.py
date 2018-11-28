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

int main() {
//	freopen("a.in", "r", stdin);

//	freopen("A-small-attempt0.in", "r", stdin);
//	freopen("A-small-attempt0.out", "w", stdout);

	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int tt, tn; cin >> tn;
	F1(tt,tn) {
		printf("Case #%d: ", tt);

		int X, S, R, a, b, w;
		double t, t2, len;
		cin >> X >> S >> R >> t >> n;
		vector<pii> V;
		F0(i,n) {
			cin >> a >> b >> w;
			X -= (b - a);
			V.push_back(pii(w, b-a));
		}
		V.push_back(pii(0, X));
		sort(V.begin(), V.end());
		double ans = 0.0;
		F0(i,SZ(V)) {
			len = V[i].second;
			w = V[i].first;
			t2 = min(t, len / (w + R));
			ans += t2;
			t -= t2;
			len -= t2 * (w + R);
			ans += len / (w + S);
		}
		printf("%.10lf\n", ans);
	}
	
	return 0;
}
