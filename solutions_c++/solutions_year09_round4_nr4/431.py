//#pragma comment(linker, "/STACK:100000000")

#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cmath>
#include <ctime>

using namespace std;

#define sqr(a) ((a)*(a))
#define ab(a) (((a)>0)?(a) : (-(a)))
#define dist2(x1, y1, x2, y2) (sqr((x1)-(x2)) + sqr((y1)-(y2)))
#define PB push_back
#define SZ size()
#define ALL(a) (a).begin(),(a).end()
#define mset(a, val) memset(a, val, sizeof(a))
#define UNIQUE(p) sort(ALL(p)), p.resize( (int)(unique(ALL(p)) - p.begin()) )

#define pii pair < int, int >
#define pdd pair < double, double >
#define MP make_pair
#define X first
#define Y second

#define N 50

pdd a[N];
double r[N];
int n;

double f (int i, int j) {
	double d = dist2(a[i].X, a[i].Y, a[j].X, a[j].Y);
	if (d < 0.0) d = 0.0;
	d = sqrt(d);
	d += r[i] + r[j];
	return d*0.5;
}

int main () {
	int i, j, CAS;

	scanf("%d", &CAS);

	for (int cas = 1; cas <= CAS; cas++) {

		scanf("%d", &n);

		for (i = 0; i < n; ++i) scanf("%lf%lf%lf", &a[i].X, &a[i].Y, &r[i]);

		double res = 1e100;

		if (n == 1) {
			res = r[0];
		}
		else if (n == 2) {
			res = max(r[0], r[1]);
		}
		else if (n == 3) {
			res = min(res, max(r[0], f(1,2)));
			res = min(res, max(r[1], f(0,2)));
			res = min(res, max(r[2], f(0,1)));		
		}
		else throw 0;

		
		printf("Case #%d: %.8lf\n", cas, res);
		cerr << cas << "\n";
	}

	cerr << "clock(): " << clock() << "\n";

	return 0;
}



