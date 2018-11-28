#include <cstdio>
#include <cstring>
#include <cmath>
#include <iostream>
#include <vector>
#include <algorithm>
typedef long long LL;
using namespace std;
#define F_IN  "B-small-attempt2.in"
#define F_OUT "B-small-attempt2.out"
#define PI 3.1415926535897932384626433832795
#define MAXN  2000
#define PX 1000
#define PY 1000
int n;
double r[MAXN];
double X, Y;
double x[MAXN];
double y[MAXN];
bool nn[MAXN];

bool good(double xx, double yy, int k) {
	for(int i=0; i<k; ++i) {
		double dist = sqrt((x[i] - xx)*(x[i] - xx) +
				(y[i] - yy)*(y[i] - yy));
		if (dist - 1e-9 < r[i] + r[k]) return false;
	}
	return true;
}

int main()
{
    int tc, tt;
    freopen(F_IN, "r", stdin);
    freopen(F_OUT, "w", stdout);

    scanf("%i", &tc);
    for(tt=1; tt<=tc; ++tt)
    {
		cerr << tt << endl;
		
		scanf("%i %lf %lf", &n, &X, &Y);

		for(int i=0; i<n; ++i) scanf("%lf", &r[i]);
//		sort(&r[0], &r[n]);
//		reverse(&r[0], &r[n]);

		memset(nn, 0, sizeof(nn));
		for(int i=0; i<n; ++i) {
			
			bool ok = false;
			for(int p=0; p<PX; ++p) {
				double dx = X / PX * p;
				for(int q=0; q<PY; ++q) {
					double dy = Y / PY * q;
					if (good(dx, dy, i)) {
						x[i] = dx;
						y[i] = dy;
						p = PX;
						q = PY;
						ok = true;
					}
				}
			}
			if (!ok) cerr << "epic fail " << i << endl;
		}

		
		printf("Case #%i:", tt);
		for(int i=0; i<n; ++i) {
		
			printf(" %.6f %.6f", x[i], y[i]);
		}
		printf("\n");
    }

    return 0;
}


