#include <cstdio>
#include <cmath>
#include <cstring>
#include <cassert>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <set>
#include <map>

#define Eo(x) { std::cerr << #x << " = " << x << std::endl; }

#define maxn 11000
#define maxm 1000000
#define eps 1e-8

using namespace std;

typedef long long int64;

typedef double real;


real x[maxn], y[maxn], z[maxn], p[maxn];
int n;

inline real getz(real X, real Y, real Z){
	real res = 0.;
	int i;
	for (i = 0; i < n; i++) if (res < (fabs(x[i] - X) + fabs(y[i] - Y) + fabs(z[i] - Z)) / (real)(p[i]))
								res = (fabs(x[i] - X) + fabs(y[i] - Y) + fabs(z[i] - Z)) / (real)(p[i]);
	return res;
}

inline real gety(real X, real Y){
 	real l = 0., r = maxm;
 	while (r - l > eps){
 	 	real m1 = l + (r - l) / 3.;
 	 	real m2 = l + 2. * (r - l) / 3.;
 	 	if (getz(X, Y, m1) < getz(X, Y, m2)) r = m2; else l = m1;
 	}
 	return getz(X, Y, l);
}

inline real getx(real X){
 	real l = 0., r = maxm;
 	while (r - l > eps){
 	 	real m1 = l + (r - l) / 3.;
 	 	real m2 = l + 2 * (r - l) / 3.;
 	 	if (gety(X, m1) < gety(X, m2)) r = m2; else l = m1;
 	}
 	return gety(X, l);
}

inline real getans(){
 	real l = 0., r = maxm;
 	while (r - l > eps){
 	 	real m1 = l + (r - l) / 3.;
 	 	real m2 = l + 2 * (r - l) / 3.;
 	 	if (getx(m1) < getx(m2)) r = m2; else l = m1;
 	}
 	return getx(l);
}

int main() {
	int ferlon;
	scanf("%d", &ferlon);
	int _;
	for (_ = 0; _ < ferlon; ++_){
		scanf("%d", &n);
		int i;
		for (i = 0; i < n; i++) std::cin >> x[i] >> y[i] >> z[i] >> p[i];
		double ans = getans();
		printf("Case #%d: %.6lf\n", _ + 1, ans);
//		fprintf(stderr, "Case #%d: %.6lf\n", _ + 1, ans);
	}
	return 0;
}
