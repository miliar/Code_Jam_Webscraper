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

ll i, j, k, m, n, l, A;

void solve() {
	ll x1, y1, x2, y2, S;
	F0(x1,m+1) F0(y1,n+1) F0(x2,m+1) {
		S = A + x2 * y1;
		if (x1 != 0 && S % x1 == 0 && S / x1 <= n) {
			y2 = S / x1;
			cout << 0 << " " << 0 << " " << x1 << " " << y1 << " " << x2 << " " << y2;
			return;
		}
	}
	cout << "IMPOSSIBLE";
}

void solvegood() {
	ll x1, y1, x2, y2;
	if (m * n < A) {
		cout << "IMPOSSIBLE";
		return;
	}
	x1 = (A+n-1) / n;
	y2 = n;
	if (A % n == 0) {
		x2 = 0;
		y1 = 0;
	} else {
		x2 = 1;
		y1 = n - A % n;
	}
	if (x1 < 0 || x1 > m || x2 < 0 || x2 > m || y1 < 0 || y1 > n || y2 < 0 || y2 > n || x1*y2-x2*y1 != A) {
		while (1);
	}
	cout << 0 << " " << 0 << " " << x1 << " " << y1 << " " << x2 << " " << y2;
}


int main() {

//	freopen("x.in", "r", stdin);

//	freopen("B-small-attempt1.in", "r", stdin);
//	freopen("B.out", "w", stdout);

	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int tt, tn; cin >> tn;
	F1(tt,tn) {
		printf("Case #%d: ", tt);
		cin >> m >> n >> A;
		solvegood();
		printf("\n");
	}
	
	return 0;
}
