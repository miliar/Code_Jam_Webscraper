#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <cmath>
#include <algorithm>

using namespace std;

struct Circle {
	int x, y, r;
};

Circle circle[50];

double getit(Circle& c1, Circle& c2, Circle& c3)
{
	double d = pow(c1.x - c2.x, 2.0) + pow(c1.y - c2.y, 2.0);
	d = sqrt(d);
	d += c1.r + c2.r;
	double r1 = d / 2.0;
	return max(r1, double(c3.r));
}

void doit(int now)
{
	int n;
	cin >> n;
	int x, y, r;
	for (int i = 0; i < n; i++)
		cin >> circle[i].x >> circle[i].y >> circle[i].r;
	if (n == 1) {
		double result = circle[0].r;
		printf("Case #%d: %.6f\n", now, result);
	} else if (n == 2) {
		double result = max(circle[0].r, circle[1].r);
		printf("Case #%d: %.6f\n", now, result);
	} else if (n == 3) {
		double r1 = getit(circle[0], circle[1], circle[2]);
		double r2 = getit(circle[0], circle[2], circle[1]);
		double r3 = getit(circle[1], circle[2], circle[0]);
		//cout << r1 << " " << r2 << " " << r3 << endl;

		double max1 = min(r1, r2);
		double result = min(max1, r3);
		printf("Case #%d: %.6f\n", now, result);
	} else {
		printf("Error\n");
	}
}

int main()
{
	int c;
	cin >> c;
	for (int i = 1; i <= c; i++)
		doit(i);

	return 0;
}
