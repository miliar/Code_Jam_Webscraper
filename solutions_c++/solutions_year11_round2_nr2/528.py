#include <iostream>
#include <algorithm>

double D, vendor[1000002];

double abs(double x)
{
	if (x < 0) return -x; else return x;
}

double fmax(double a, double b)
{
	if (a > b) return a; else return b;
}

int main()
{
    freopen("a.txt", "r", stdin);
	freopen("b.txt", "w", stdout);

	int t, n;

	std::cin >> t;
	for (int i = 0; i < t; i++) {
		double d;
		int c;
		n = 0;
		std::cin >> c >> d;
		for (int j = 0; j < c; j++) {
			double pos; int s;
			std::cin >> pos >> s;
			for (int k = 0; k < s; k++) 
				vendor[n++] = pos;
		}
		std::sort(vendor, vendor + n);
		double res = 0;
		double min, max;
		min = 0; max = 10000000000000.0;
		while (abs(max - min) > 1e-12) {
			double mid = (max + min) / 2;
            double last = -100000000000000.0;
			bool succeed = true;
			for (int j = 0; j < n; j++) {
				double pos = last + d;
				if (vendor[j] <= pos) {
					if (abs(pos - vendor[j]) > mid) succeed = false;
					else last = pos;
				} else last = fmax(vendor[j] - mid, pos);
			}
			if (succeed) max = mid; else min = mid;
		}
		printf("Case #%d: %0.7lf\n", i + 1, (min + max) / 2);
	}
	return 0;
}