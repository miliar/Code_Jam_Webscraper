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
const double eps = 1e-9;
ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }
int bc(int n) { return n ? bc((n-1)&n)+1 : 0; }

int i, j, k, m, n, l, z1, z2;
double x[500], y[500], r[500], R;

vector< vector<int> > V;
vector<int> all;

void add(double X, double Y) {
	all.clear();	
	int i; F0(i,n) if ( hypot(X-x[i], Y-y[i]) <= R - r[i] + eps) all.push_back(i);

	i = i;

	V.push_back(all);
}

int ok() {
	int i, j, k, ii, jj;
	V.clear();
	F0(i,n) {
		add(x[i], y[i]);
	}
	F0(i,m) if (SZ(V[i]) == n) return 1;
	F0(i,n) for (j=i+1; j < n; j++) if (x[i] != x[j] || y[i] != y[j]) {
		double d = hypot(x[i] - x[j], y[i] - y[j]);
		double a = R-r[i];
		double b = R-r[j];
		if (d > a + b + eps || a > b + d + eps || b > a + d + eps) continue;
		double _x = (a*a-b*b+d*d) / (2*d);
		double c = _x / d;
		double _X = x[i] + c * (x[j] - x[i]);
		double _Y = y[i] + c * (y[j] - y[i]);
		double _y = sqrt(a*a - _x*_x);
		
		add( _X - (y[j] - y[i]) * _y / d, _Y + (x[j] - x[i]) * _y / d);
		add( _X + (y[j] - y[i]) * _y / d, _Y - (x[j] - x[i]) * _y / d);
	}

	int m = SZ(V);
	F0(i,m) if (SZ(V[i]) == n) return 1;
	F0(i,m) for(j=i+1;j<m;j++) if (SZ(V[i]) + SZ(V[j]) >= n) {
		z1 = SZ(V[i]); z2 = SZ(V[j]); ii = jj = 0;

		for (k = 0; k < n; k++) {
			int f = 0;
			if (ii < z1 && V[i][ii] == k) { f = 1; ii++; }
			if (jj < z2 && V[j][jj] == k) { f = 1; jj++; }
			if (!f) break;
		}
		if (k == n) return 1;
	}

	return 0;
}

int main() {
//	freopen("x.in", "r", stdin);

//	freopen("D-small-attempt0.in", "r", stdin);
//	freopen("D-small-attempt1.out", "w", stdout);

	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);

	int tt, tn; cin >> tn;
	F1(tt,tn) {
		printf("Case #%d: ", tt);
		cin >> n;
		F0(i,n) cin >> x[i] >> y[i] >> r[i]; 
/*		n = 40;
		F0(i,n) x[i] = y[i] = r[i] = rand()%100;*/
		double P = 0.0, Q = 5000;
		F0(i,n) P = max(P, r[i]);
		int u;
		F0(u,50) {
			R = (P+Q) / 2.0;
			if (ok()) Q = R; else P = R;
		}
		printf("%.10lf\n", R);
	}
	
	return 0;
}
