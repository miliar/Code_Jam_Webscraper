#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <cmath>
#include <complex>
using namespace std;

long double PI;
const double EPS = 1e-12;

int main(void)
{
	PI = acos(-1.0L);
	int number_of_tests;
	scanf("%d", &number_of_tests);
	for (int test_no = 1; test_no <= number_of_tests; test_no++)
	{
		printf("Case #%d: ", test_no);
		double x1, x2, x3, x4, y1, y2, y3, y4, t;
		scanf("%lf%lf%lf%lf%lf%lf", &x1, &y1, &x2, &y2, &t, &t);
		scanf("%lf%lf%lf%lf%lf%lf", &x3, &y3, &x4, &y4, &t, &t);
		complex<double> v1(x2-x1, y2-y1), v2(x4-x3, y4-y3);
		double scaling = abs(v2) / abs(v1);
		complex<double> a  = v2 / v1;
		complex<double> b  = complex<double>(x3, y3) - complex<double>(x1, y1) * a;
		if (abs(1.0-a) < EPS)
		{
			printf("0.00000 0.00000\n");
		}
		else
		{
			complex<double> res = b / (1.0 - a);
			printf("%.5lf %.5lf\n", real(res), imag(res));
		}
	}
	return 0;
}
