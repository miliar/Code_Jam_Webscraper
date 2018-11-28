#include <cstdio>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <string>
#include <set>
#include <vector>
#include <cmath>
#include <cassert>
#include <cstdlib>
#include <map>

#define y0 y63475625
#define y1 y28435
#define sqr(x) ((x)*(x))
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define re return

#ifdef ONLINE_JUDGE
#pragma comment(linker, "/STACK:16777216")
#endif

using namespace std;

typedef vector <int> vi;
typedef vector <vi> vvi;
typedef long long ll;
typedef long double ld;
typedef pair <int, int> ii;
typedef vector <ii> vii;

template <class T> T abs(const T & a) {
	return a > 0 ? a : -a;
}

template <class T> int sgn(const T & a) {
	return a > 0 ? 1 : (a < 0 ? -1 : 0);
}

#ifdef ONLINE_JUDGE
const double M_PI = 2.0 * acos(1.0);
#endif

int xo[1000010];
double X[1000010];

int main()
{
	int T;
	scanf("%d", &T);
	for (int I = 0; I < T; I++) {
		cerr << I << endl;
		int n, d, m = 0;
		scanf("%d%d", &n, &d);
		for (int i = 0; i < n; i++) {
			int x, k;
			scanf("%d%d", &x, &k);
			for (int j = 0; j < k; j++) xo[m++] = x;
		}
		sort(xo, xo + m);
		n = m;
		double L = 0.0, R = 1e13;
		for (int it = 0; it < 100; it++) {
			double t = (L + R) / 2.0;
			bool kpyto = true;
			for (int i = 0; i < n; i++) {
				if (i == 0) X[i] = xo[i] - t; else {
					double x = xo[i] - t;
					if (x - X[i - 1] < d) {
						double v = (X[i - 1] + d - xo[i]) / t;
						if (abs(v) > 1) {
							kpyto = false; break;
						}
						X[i] = xo[i] + v * t;
					} else X[i] = x;
				}
			}
			if (kpyto) R = t; else L = t;
		}
		printf("Case #%d: %.10lf\n", I + 1, R);
	}
	return 0;
}
