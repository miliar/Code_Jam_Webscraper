#include <iostream>
#include <algorithm>
using namespace std;

const int maxn = 210;

double d;
int c;
double p[maxn];
int v[maxn];

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("b.out", "w", stdout);

	int tc;
	cin >> tc;
	for (int tt = 1; tt <= tc; tt++) {
		cin >> c >> d;
		for (int i = 0; i < c; i++)
			cin >> p[i] >> v[i];

		double l = 0, r = 1e15, mid;
		int cnt = 10000;
		while (cnt --) {
			mid = (l + r) / 2;

			double lb = -1e20;
			bool flag = true;
			for (int i = 0; i < c; i++) {
				double left = (double)p[i] - mid;
				if (left < lb + d)
					left = lb + d;

				double right = left + d * (double)(v[i] - 1);

				if (right - p[i] > mid) {
					flag = false;
					break;
				}

				lb = right;
			}
			// cout << flag << endl;

			if (flag)
				r = mid;
			else
				l = mid;
		}
		
		printf("Case #%d: %.7lf\n", tt, l);
	}
}
