#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <algorithm>
#include <cmath>

using namespace std;


int N;
double eps = 0.0000001;

double ar(vector<double> vx, vector<double> vy)
{
	double res = 0;
	for (int i = 0; i < vx.size() - 1; i++)
		res += (vy[i] + vy[i + 1]) * (vx[i + 1] - vx[i]) / 2;

	return res;
}

double calcArea(double x1, double y1, double x2, double y2, double R)
{
	if (x2 < x1 + eps) return 0;
	if (x1 * x1 + y1 * y1 > R * R - eps) return 0;
	if (x2 * x2 + y2 * y2 < R * R + eps) return (y2 - y1)*(x2 - x1);
	double px1, py1, px2, py2;
	vector<double> upx, upy, downx, downy;

	if (x1 * x1 + y2 * y2 > R * R - eps)
	{
		px1 = x1;
		py1 = sqrt(R * R - px1 * px1);
		upx.push_back(px1);
		upy.push_back(py1);
	}
	else
	{
		upx.push_back(x1);
		upy.push_back(y2);
		py1 = y2;
		px1 = sqrt(R * R - py1 * py1);
		upx.push_back(px1);
		upy.push_back(py1);
	}

	downx.push_back(x1);
	downy.push_back(y1);

	if (x2 * x2 + y1 * y1 > R * R - eps)
	{
		py2 = y1;
		px2 = sqrt(R * R - py2 * py2);
		downx.push_back(px2);
		downy.push_back(py2);
		upx.push_back(px2);
		upy.push_back(py2);
	}
	else
	{
		downx.push_back(x2);
		downy.push_back(y1);
		px2 = x2;
		py2 = sqrt(R * R - px2 * px2);
		upx.push_back(px2);
		upy.push_back(py2);
	}
	double l = sqrt((px1 - px2)*(px1 - px2) + (py1 - py2)*(py1 - py2));
	return R * R * asin(l / (2 * R)) - l * sqrt(R * R - l * l / 4) / 2 + ar(upx, upy) - ar(downx, downy);
}


void solve(int I)
{
	double f, R, t, r, g;
	cin >> f >> R >> t >> r >> g;
	//r += f;
	double ans = 0;
	for (double i = r + f; i < R-t; i += g + r + r)
	{
		for (double j = r + f; j < R; j += g + r + r)
			ans += 4 * calcArea(i, j, i + g - f - f, j + g - f - f, R - t - f);
	}
	cout << "Case #" << I + 1 << ": " << 1 - ans / (asin(1.) * 2 * R * R) << endl;
}


int main()
{
	freopen("1.in", "r", stdin);
	freopen("1.out", "w", stdout);
	cin >> N;
	for (int I = 0; I < N; I++)
		solve(I);
	fclose(stdin);
	fclose(stdout);
	return 0;
}