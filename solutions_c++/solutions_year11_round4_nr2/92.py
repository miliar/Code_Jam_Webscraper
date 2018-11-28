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
char ss[505][505];
ll a[505][505], x[505][505], y[505][505], s[505][505];

int solve() { 
	for (i = k; i <= m; i++) {
		for (j = k; j <= n; j++) {
			int sumx = x[i][j] - x[i-k][j] - x[i][j-k] + x[i-k][j-k];
			sumx -= a[i-k+1][j-k+1]*(i-k+1)+a[i-k+1][j]*(i-k+1)+a[i][j-k+1]*i+a[i][j]*i;
			int mid = s[i][j] - s[i-k][j] - s[i][j-k] + s[i-k][j-k];
			mid -= a[i-k+1][j-k+1]+a[i-k+1][j]+a[i][j-k+1]+a[i][j];
			int sumy = y[i][j] - y[i-k][j] - y[i][j-k] + y[i-k][j-k];
			sumy -= a[i-k+1][j-k+1]*(j-k+1)+a[i-k+1][j]*j+a[i][j-k+1]*(j-k+1)+a[i][j]*j;
			if (2 * sumx == mid * (2*i-k+1) && 2 * sumy == mid * (2*j-k+1)) 
				return 1;
		}
	}
		
	return 0;
}

int main() {
//	freopen("b.in", "r", stdin);

//	freopen("B-small-attempt0.in", "r", stdin);
//	freopen("B-small-attempt0.out", "w", stdout);

	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int tt, tn; cin >> tn;
	F1(tt,tn) {
		printf("Case #%d: ", tt);
		scanf("%d %d %d\n", &m, &n, &k);
		F0(i,m) gets(ss[i]);

		F1(i,m) F1(j,n) a[i][j] = (ss[i-1][j-1] - '0');
		F1(i,m) F1(j,n) {
			x[i][j] = x[i-1][j] + x[i][j-1] - x[i-1][j-1] + a[i][j] * i;
			y[i][j] = y[i-1][j] + y[i][j-1] - y[i-1][j-1] + a[i][j] * j;
			s[i][j] = s[i-1][j] + s[i][j-1] - s[i-1][j-1] + a[i][j];
		}

		for (k = min(m, n); k >= 3; k--) 
			if (solve()) break;
		if (k >= 3) cout << k << endl;
		else cout << "IMPOSSIBLE" << endl;
	}
	
	return 0;
}
