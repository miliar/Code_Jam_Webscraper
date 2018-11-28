#include <cstdio>
#include <vector>
#include <cstring>
#include <string>
#include <map>
#include <utility>
#include <algorithm>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <cmath>
#include <numeric>

using namespace std;

int tab[500];
int all;
int n;

bool g(int i, double p) {
	double v = tab[i] + all*p;
	for (int j=0; j<n; ++j) {
		if (j == i) continue;
		double w = v - tab[j];
		if (w < 0) continue;
		w /= all;
		p += w;
		if (p > 1) return false;
	}
	return true;
}

const double E = 0.1E-12;
double f(int i) {
	double l = 0., r = 1.;
	while (l+E < r) {
		double m = (l+r)/2;
		if (g(i, m)) {
			l = m;
		} else {
			r = m;
		}
	}
	return (l+r)/2;
}

int main(void) {
	int t;
	scanf("%d", &t);
	for (int tc=1; tc<=t; ++tc) {
		scanf("%d", &n);
		for (int i=0; i<n; ++i) scanf("%d", tab+i);
		all = accumulate(tab, tab+n, 0);
		printf("Case #%d:", tc);
		for (int i=0; i<n; ++i) {
			printf(" %.6lf", 100*f(i));
		}
		printf("\n");
	}
	return 0;
}
