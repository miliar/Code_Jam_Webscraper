#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <algorithm>
#include <cassert>
#include <string>
#include <cmath>
#include <map>
#include <set>

using namespace std;

const double eps = 1e-7;

struct circle {
	double x, y, r;
	circle(double xx = 0, double yy = 0, double rr = 0) { x = xx, y = yy, r = rr; }
	void read() { cin >> x >> y >> r; }
};

double cdist(const circle & a, const circle & b) { return sqrt(fabs(((a.x - b.x)*(a.x - b.x) + (a.y - b.y)*(a.y - b.y)))); }

int main()
{
	int test_cnt;
	scanf("%d", &test_cnt);
	for (int test_id = 1; test_id <= test_cnt; ++test_id)
	{
		int n;
		cin >> n;
		circle * x = new circle[n];
		for (int i = 0; i < n; ++i) x[i].read();
        double r = 1e+9;
        for (int i = 0; i < n; ++i)
        {
        	double r1 = x[i].r;
            for (int j1 = 0; j1 < n; ++j1) if (j1 != i)
            	for (int j2 = 0; j2 < n; ++j2) if (j2 != i)
            		r1 = max(r1, (x[j1].r + x[j2].r + cdist(x[j1], x[j2]))*0.5);
            r = min(r, r1);
        }

        cout.precision(9);
        cout << "Case #" << test_id << ": " << r << endl;
    }

	return 0;
}
