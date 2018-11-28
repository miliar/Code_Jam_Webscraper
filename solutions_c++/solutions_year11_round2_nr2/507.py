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

int i, j, k, m, n, l, ans, D;
int cnt[205], x[205];

int main() {
//	freopen("b.in", "r", stdin);

	freopen("B-small-attempt0.in", "r", stdin);
	freopen("B-small-attempt0.out", "w", stdout);

//	freopen("B-large.in", "r", stdin);
//	freopen("B-large.out", "w", stdout);

	int tt, tn; cin >> tn;
	F1(tt,tn) {
		printf("Case #%d: ", tt);

		cin >> n >> D;
		F0(i,n) 
			cin >> x[i] >> cnt[i];

		double P = 0.0, Q = 1e6, R;

		F0(k,200) {
			R = (P + Q) / 2;
			double z = -1e100, z2;
			F0(i,n) {
				z = max(z + D, x[i] - R);
				z2 = z + (cnt[i] - 1) * D;
				if (z2 > x[i] + R) break;
				z = z2;
			}
			if (i == n) Q = R; else P = R;
		}
		
		printf("%.10lf\n", P);
	}
	
	return 0;
}
