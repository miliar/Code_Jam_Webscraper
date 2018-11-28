#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <numeric>

using namespace std;

#define Eo(x) { cerr << #x << " = " << x << endl; }

typedef long long int64;
typedef double real;

#define inf 0x3f3f3f3f

#define maxn (1 << 6)

#define tol 1e-8

struct pnt {
	real x, y;

	pnt() { }
	pnt(real _x, real _y) : x(_x), y(_y) { }

	pnt operator + (const pnt& rhs) const {
		return pnt(x+rhs.x, y+rhs.y);
	}
	pnt operator - (const pnt& rhs) const {
		return pnt(x-rhs.x, y-rhs.y);
	}
	pnt operator * (real rhs) const {
		return pnt(x*rhs, y*rhs);
	}

	real operator ! () const {
		return x*x + y*y;
	}

	pnt rotate(real ang) {
		return pnt(x*cos(ang) - y*sin(ang), x*sin(ang) + y*cos(ang));
	}
};

inline real sqr(real x) { return x * x; }

inline real my_acos(real c) {
	if(c < -1.0) c = -1.0;
	if(c >  1.0) c =  1.0;
	return acos(c);
}

pnt pts[maxn];
real r[maxn];
int n, was[maxn];

bool solve(real R, int cnt);

bool go(pnt cent, real R, int cnt) {
	int owas[maxn], i;
	memcpy(owas, was, sizeof(owas));
	for(i = 0; i < n; i++)
		if(sqrt(!(pts[i]-cent)) + r[i] <= R + tol)
			was[i] = true;
	//fprintf(stderr, "!! "); for(int u = 0; u < n; u++) fprintf(stderr, "%d ", was[u]); fprintf(stderr, "\n");
	if(solve(R, cnt-1))
		return true;
	memcpy(was, owas, sizeof(owas));
	return false;
}

bool solve(real R, int cnt) {
	int i, j;
	for(i = 0; i < n; i++)
		if(!was[i]) break;
	if(i >= n) return true;
	if(cnt == 0)
		return false;
	for(i = 0; i < n; i++)
		if(!was[i]) {
			//Eo(cnt);
			//Eo(i);
			//for(int u = 0; u < n; u++) fprintf(stderr, "%d ", was[u]); fprintf(stderr, "\n");
			was[i] = 1;
			if(solve(R, cnt-1))
				return true;
			was[i] = 0;
		}
	for(i = 0; i < n; i++)
		for(j = i+1; j < n; j++) {
			//Eo(cnt);
			//Eo(i);
			//Eo(j);
			//for(int u = 0; u < n; u++) fprintf(stderr, "%d ", was[u]); fprintf(stderr, "\n");
			real d2 = !(pts[i] - pts[j]);
			real d = sqrt(d2);
			real cosb = (d2 + sqr(R-r[j]) - sqr(R-r[i])) / (2.0 * d * (R-r[j]));
			real beta = my_acos(cosb);

			pnt v = (pts[i]-pts[j]).rotate(beta);
			v = v * ((R-r[j]) / sqrt(!v));
			pnt cent = pts[j] + v;
			//if(i == 0 && j == 1)
				//fprintf(stderr, "(%.3lf, %.3lf) : %.3lf\n", cent.x, cent.y, beta);

			if(go(cent, R, cnt))
				return true;
			cent = pts[j] + (pts[i]-pts[j]).rotate(-beta);
			if(go(cent, R, cnt))
				return true;
		}
	return false;
}

int main() {
	int t = 1, tc, i, j;
	for(scanf("%d", &tc); t <= tc; t++) {
		printf("Case #%d:", t);
		scanf("%d", &n);
		for(i = 0; i < n; i++)
			scanf("%lf%lf%lf", &pts[i].x, &pts[i].y, r+i);

		real ll = 0.0, rr = 1e20;
		for(i = 0; i < n; i++)
			if(ll < r[i]) ll = r[i];

		memset(was, 0, sizeof(was));
		//Eo(solve(6.0+tol, 2));
		//continue;

		while(rr-ll > tol) {
			real R = (ll+rr) * 0.5;
			memset(was, 0, sizeof(was));
			if(solve(R, 2))
				rr = R;
			else
				ll = R;
		}
		printf(" %.8lf\n", rr);
	}
	return 0;
}
