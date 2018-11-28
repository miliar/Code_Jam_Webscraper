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

int i, j, k, m, n, l;
int ok[105][105], p[105][105], g[1<<16], b[1<<16];

const int N = 101;
int x[N], y[N], V[N];
int d[N][N];

int rec(int i) {
	V[i] = 1;
	for (int j = 1; j <= n; j++) if (d[i][j]) {
		if (y[j] == 0 || (V[y[j]] == 0 && rec(y[j]))) {
			x[i] = j;
			y[j] = i;
			return 1;
		}
	}
	return 0;
}

int main() {
	//freopen("x.in", "r", stdin);

//	freopen("C-small-attempt0.in", "r", stdin);
//	freopen("C.out", "w", stdout);

	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);

	int tt, tn; cin >> tn;
	F1(tt,tn) {
		printf("Case #%d: ", tt);
		cin >> n >> m;
		F0(i,n) F0(j,m) cin >> p[i][j];

		memset(d, 0, sizeof(d));
		F1(i,n) F1(j,n) if (p[i-1][0] < p[j-1][0]) {
			d[i][j] = 1;
			F0(k,m) if (p[i-1][k] >= p[j-1][k]) d[i][j] = 0;
		}

		int ans = 0;
		memset(x, 0, sizeof(x));
		memset(y, 0, sizeof(y));
		F1(i,n) if (x[i] == 0) {
			for (j = 1; j <= n; j++) V[j] = 0;
			ans += rec(i);
		}
		cout << n-ans << endl;

/*
		F0(l,(1<<n)) {
			g[l] = 1;
			F0(i,n) if ((1<<i)&l)
				for (j=i+1;j<n;j++)
					if ((1<<j)&l) 
						F0(k,m) if ( (ll)(p[i][0]-p[j][0]) * (ll)(p[i][k]-p[j][k]) <= 0) g[l] = 0;
		}
		F0(i,(1<<n)) {
			if (i == 0) b[i] = 0;
			else {
				b[i] = inf;
				for (j=i; j>0; j = i&(j-1)) if (g[j]) {
					b[i] = min(b[i], 1 + b[i^j]);
				}
			}
		} 
		cout << b[(1<<n)-1] << endl;*/
	}
	
	return 0;
}
