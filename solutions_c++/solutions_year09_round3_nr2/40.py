#define _CRT_SECURE_NO_DEPRECATE

#include <iostream>
#include <algorithm>
#include <cassert>
#include <string>
#include <cmath>
#include <map>
#include <set>

using namespace std;

const double eps = 1e-9;

struct tpoint {
	double x, y, z;
	tpoint(double xx = 0, double yy = 0, double zz = 0) { x = xx, y = yy, z = zz; }
	void read() { cin >> x >> y >> z; }
	void operator +=  (const tpoint & b) { x += b.x, y += b.y, z += b.z; }
	void operator /=  (double n) { x /= n, y /= n, z /= n; }
	friend double mul(const tpoint & a, const tpoint & b) { return (a.x*b.x + a.y*b.y + a.z*b.z); }
};

int main()
{
	int test_cnt;
	scanf("%d", &test_cnt);
	for (int test_id = 1; test_id <= test_cnt; ++test_id)
	{
		int n;
		tpoint t, p, v;
		cin >> n;
        for (int i = 0; i < n; ++i)
        {
        	t.read();
        	p += t;
        	t.read();
        	v += t;
        }
        p /= n, v /= n;
        double sv = mul(v, v);
        double dmin = sqrt(fabs(mul(p, p)));
        double tmin = 0;
        if (sv > eps)
        {
	        double k = -mul(p, v) / sv;
            if (k > eps) dmin = sqrt(fabs(mul(p, p) - k*k*sv)), tmin = k;
        }

//        cout.precision(9);
//        cout << "Case #" << test_id << ": " << dmin << " " << tmin << endl;
        printf("Case #%d: %0.9lf %0.9lf\n", test_id, dmin, tmin);
    }

	return 0;
}
