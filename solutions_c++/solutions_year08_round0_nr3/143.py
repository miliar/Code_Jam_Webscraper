#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <iostream>
#include <algorithm>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(i=0;i<n;i++)
#define F1(i,n) for(i=1;i<=n;i++)
const int inf = 1000000009;
const double eps = 1e-8;
const double pi = acos(-1.0);
int dx[]={-1,0,1,0};
int dy[]={0,-1,0,1};

int i, j, k, m, n, l, o, tt, tn;
double f, R, t, r, g;

double seg(double d) {
	if (fabs(d) < eps) return 0.0;
	double alp = asin(0.5*d / R);
	return alp * R * R - 0.5 * d * sqrt(R*R-d*d*0.25);
}

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	cin >> tn;
	F1(tt,tn) {
		cin >> f >> R >> t >> r >> g;
		double Total = pi * R * R;
		R -= t;
		R -= f;
		r += f;
		g -= 2*f;
		double S = 0.0, x, y, xr, yr, x2, y2;
		if (g >= 0.0 && R >= 0)
		for (i = 0; (x = (r + i * (g + 2*r))) <= R; i++) {
			for (j = 0; (y = (r + j * (g + 2*r))) <= R; j++)
			if (x*x+y*y <= R*R)
			{
				xr = min(sqrt(R*R-y*y), x+g);
				yr = min(sqrt(R*R-x*x), y+g);
				y2 = min(yr, sqrt(R*R-xr*xr));
				x2 = min(xr, sqrt(R*R-yr*yr));
				S += (xr-x)*(yr-y);
				S -= 0.5*fabs(yr-y2)*fabs(xr-x2);
				S += seg(hypot(x2-xr, y2-yr));
			}
		}
		printf("Case #%d: %.12lf\n", tt, 1-4*S / Total);
	}

	return 0;
}
