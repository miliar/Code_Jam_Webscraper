#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

#define sz(a) int((a).size())
#define all(X) (X).begin(), (X).end()
typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;

const int MAXN = 128;

int upx[MAXN], upy[MAXN];
int downx[MAXN], downy[MAXN];
int w, l, u, g;

double calit(double x)
{
	double sum = 0;
	for (int i = 1; i < u; ++i) {
		if (upx[i] > x) {
			sum += (upy[i - 1] + upy[i - 1] + (upy[i] - upy[i - 1]) * (x - upx[i - 1]) / (upx[i] - upx[i - 1])) * (x - upx[i - 1]) / 2.0;
			break;
		}
		else {
			sum += (upy[i] + upy[i - 1]) * (upx[i] - upx[i - 1]) / 2.0;
		}
	}
	for (int i = 1; i < l; ++i) {
		if (downx[i] > x) {
			sum -= (downy[i - 1] + downy[i - 1] + (downy[i] - downy[i - 1]) * (x - downx[i - 1]) / (downx[i] - downx[i - 1])) * (x - downx[i - 1]) / 2.0;
			break;
		}
		else {
			sum -= (downy[i] + downy[i - 1]) * (downx[i] - downx[i - 1]) / 2.0;
		}
	}
	return sum;
}

double calx(double area)
{
	double down = 0, up = w;
	for (int i = 0; i < 100; ++i) {
		double mid = (down + up) / 2;
		if (calit(mid) < area) {
			down = mid;
		}
		else {
			up = mid;
		}
	}
	return up;
}

void run()
{
	scanf("%d %d %d %d", &w, &l, &u, &g);
	for (int i = 0; i < l; ++i) {
		scanf("%d %d", downx + i, downy + i);
	}
	for (int i = 0; i < u; ++i) {
		scanf("%d %d", upx + i, upy + i);
	}
	double sum = 0;
	for (int i = 1; i < u; ++i) {
		sum += (upy[i] + upy[i - 1]) * (upx[i] - upx[i - 1]) / 2.0;
	}
	for (int i = 1; i < l; ++i) {
		sum -= (downy[i] + downy[i - 1]) * (downx[i] - downx[i - 1]) / 2.0;
	}
	sum /= g;
	for (int i = 0; i < g - 1; ++i) {
		double area = sum * (i + 1);
		printf("%.10lf\n", calx(area));
	}
}

int main()
{
	freopen("A1.in", "r", stdin);
	freopen("A1.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		printf("Case #%d:\n", i);
		run();
	}
	return 0;
}