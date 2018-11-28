#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <climits>
#include <cfloat>
#include <map>
#include <utility>
#include <set>
#include <iostream>
#include <memory>
#include <string>
#include <vector>
#include <algorithm>
#include <functional>
#include <sstream>
#include <complex>
#include <stack>
#include <queue>
#include <list>
#include <fstream>
#include <cstring>

using namespace std;
static const double EPS = 1e-10;
typedef long long ll;
typedef complex<double> VEC;

static const int MAX_DEPTH = 10;
static const int MAX_MONTEKARURO = 100;
static const double PI = 3.141592653589793238462643383;

//ƒnƒG‚ªŠO˜g‚Ì“à‘¤‚É“ü‚Á‚Ä‚¢‚é
int check(double x, double y, double r)
{
	return (x * x + y * y < r * r + EPS) ? 1 : 0;
}

double calcArea(double left, double bottom, double right, double top, double r, int depth)
{
	if (depth > MAX_DEPTH){
		int counter = 0;
		for (int i = 0; i < MAX_MONTEKARURO; ++i){
			counter += check(left + (right - left) * rand() / RAND_MAX, bottom + (top - bottom) * rand() / RAND_MAX, r);
		}

		return (right - left) * (top - bottom) * counter / MAX_MONTEKARURO;
	}

	int flag[2] = {0, 0};
	++flag[check(left, bottom, r)];
	++flag[check(right, bottom, r)];
	++flag[check(left, top, r)];
	++flag[check(right, top, r)];

	if (flag[0] && flag[1]){
		const double x = (left + right) * 0.5;
		const double y = (bottom + top) * 0.5;
		return calcArea(left, bottom, x, y, r, depth + 1) +
			calcArea(x, bottom, right, y, r, depth + 1) +
			calcArea(left, y, x, top, r, depth + 1) +
			calcArea(x, y, right, top, r, depth + 1);
	}

	return flag[1] ? (right - left) * (top - bottom) : 0;
}

int main() {
	int N;
	cin >> N;

	for (int testCase = 1; testCase <= N; ++testCase){
		double f, R, t, r, g;
		cin >> f >> R >> t >> r >> g;

		double unhitArea = 0;
		double completeUnhitArea = g - f * 2;
		if (completeUnhitArea < 0){
			printf("Case #%d: %.20lf\n", testCase, 0);
			continue;
		}
		completeUnhitArea *= completeUnhitArea;

		for (double left = r; left < R; left += g + r * 2){
			for (double bottom = r; bottom < R; bottom += g + r * 2){
				if (abs(VEC(left + g, bottom + g)) < R - t + EPS){
					unhitArea += completeUnhitArea;
					continue;
				}

				unhitArea += calcArea(left + f + EPS, bottom + f + EPS, left + g - f - EPS, bottom + g - f - EPS, R - t - f, 0);
			}
		}

		const double wholeArea = R * R * PI * 0.25;
		const double answer = 1.0 - unhitArea / wholeArea;

		printf("Case #%d: %.20lf\n", testCase, answer);
	}
}
