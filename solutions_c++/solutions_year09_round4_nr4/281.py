#include <iostream>
#include <cmath>
#include <algorithm>

using namespace std;

int main(int argc, char ** argv)
{
	int ntest;

	scanf("%d", &ntest);

	for (int t = 0; t < ntest; t++) {
		int n;
		int xs[3], ys[3], rs[3];
		
		scanf("%d", &n);

		for (int i = 0; i < n; i++) {
			int x, y, r;

			scanf("%d %d %d", &x, &y, &r);
			xs[i] = x, ys[i] = y, rs[i] = r;
		}

		printf("Case #%d: ", t+1);

		if (n == 1)
			printf("%d", rs[0]);
		else if (n == 2)
			printf("%d", max(rs[0], rs[1]));
		else {
			double ret = 1e9;

			for (int a = 0; a < 3; a++)
				for (int b = a+1; b < 3; b++) {
					double v = (rs[a] + hypot(xs[a]-xs[b], ys[a]-ys[b]) + rs[b])/2;
					ret = min(ret, v);
				}

			for (int a = 0; a < 3; a++)
				ret = max(ret, (double)rs[a]);

			printf("%lf", ret);
		}
		printf("\n");
	}

	return 0;
}
