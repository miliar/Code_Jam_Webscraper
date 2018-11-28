#include <iostream>

using namespace std;

const int C = 210;

const int V = 1000010;

typedef struct node {
	long long x;
	long long v;
}Point;

bool cmp(Point a, Point b) {
	if (a.x < b.x) {
		return true;
	}
	return false;
}

Point ps[C];

long long c, d;

bool isok(long long res) {
	long long left = ps[0].x - res - d;
	bool f = true;

	for (int i = 0; i < c; ++i) {
		for (int j = 0; j < ps[i].v; ++j) {
			if (ps[i].x + res < left) {
				f = false;
			} else {
				left = max(left + d, ps[i].x - res +d);
			}
		}
	}

	return f;
}

int main() {

	int Tc;
	
	freopen( "B-large.in", "r", stdin );
	freopen( "B-large-out", "w", stdout );

	scanf("%d", &Tc);

	for (int tc = 1; tc <= Tc; ++tc) {
		
		scanf("%I64d%I64d", &c, &d);
		
		d *= 2;

		for (int i = 0; i < c; ++i) {
			long long x, v;
			scanf("%I64d%I64d", &x, &v);
			ps[i].x = 2 * x;
			ps[i].v = v;
		}
		
		sort(ps, ps + c, cmp);
		
		long long low = 0;
		long long high = 10000000;
		high *= 10000000;
		long long mid;

		while (low < high - 4) {
			mid = (low + high) / 2;
			if (isok(mid)) {
				high = mid;
			} else {
				low = mid;
			}
		}
		
		long long res;
		for (res = low; res <= high; ++res) {
			if (isok(res)) {
				break;
			}
		}
					
		printf("Case #%d: %lf\n", tc, 1.0 * res / 2);
	}

	return 0;
}




