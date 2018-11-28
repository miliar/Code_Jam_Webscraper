#include<iostream>
#include<cstring>
#include<map>
#include<algorithm>
#include<stack>
#include<queue>
#include<cmath>

using namespace std;

const int N = 1000100;
const double EPS = 1e-8;

int P[N];
int n, D, C;

bool solve(double t)
{
	double last = P[0] - t;
	for (int i = 1; i <  n;  i++) {
		double y = last + D;
		if (P[i] < y) {
			if (P[i] + t < y) return false;
			last = y;
		} else {
			double tt = min(t, P[i] - y);
			last = P[i] - tt;
		}
	}
	return true;
}


int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int T, t = 1;
	scanf("%d", &T);
	while ( T-- ) {
		scanf("%d%d", &C, &D);
		n = 0;
		int p, v;
		for (int i = 0; i < C; i++) {
			scanf("%d%d", &p, &v);
			while(v--) {
				P[n++] = p;
			}
		}
		sort(P, P+n);
		double l = 0, r = 1e20;
		int cnt = 0;
		while(cnt++ < 100 && r - l > EPS) {
			double mid = (r + l) / 2.0;
			if (solve(mid)) r = mid;
			else l = mid;
		}
		printf("Case #%d: %.6f\n", t++, (l+r)/2.0);
	}
	return 0;
}
