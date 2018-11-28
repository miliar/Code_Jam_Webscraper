#include <algorithm>
#include <iomanip>
#include <iostream>
#include <sstream>
#include <string.h>
#include <climits>
#include <vector>
#include <queue>
#include <stack>
#include <cmath>
using namespace std;

#define NMAX 3
#define LARGE 1e20

int C, N;

class Plant {
	public:
		int x;
		int y;
		int r;
};

Plant plants[NMAX];

double dist(int x1, int y1, int x2, int y2) {
        return sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
}

int
main()
{
	double r, tmp;

	cin >> C;

	for (int cas = 1; cas <= C; cas++) {
		cin >> N;
		for (int n = 0; n < N; n++) {
			cin >> plants[n].x >> plants[n].y >> plants[n].r;
		}
		r = LARGE;

		if (N == 1) {
			r = plants[0].r;
		} else if (N == 2) {
			r = plants[0].r;
			if (r < plants[1].r)
				r = plants[1].r;
		} else {
			for (int n = 0; n < N; n++) {
				for (int n2 = 0; n2 < N; n2++) {
					if (n == n2)
						continue;

					//printf("%d %d %d\n", N, n, n2);
					tmp = dist(plants[n].x, plants[n].y, plants[n2].x, plants[n2].y) + plants[n].r + plants[n2].r;
					if (tmp < r)
						r = tmp;
				}
			}
			r /= 2;
			for (int n = 0; n < N; n++) {
				if (plants[n].r > r)
					r = plants[n].r;
			}
		}

		printf("Case #%d: %.6lf\n", cas, r);
	}

	return 0;
}
