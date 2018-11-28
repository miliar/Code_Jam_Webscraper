#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define PB push_back
#define MP make_pair

const double pi = 3.1415926535;
const double eps = 1e-6;

double x[1100], y[1100], fx[1100], fy[1100];
int n, W, L, r[1100];
double sqr(double x) {
	return x * x;
}
double fixx(double x) {
	if (x < 0) return 0;
	if (x > W) return W;
	return x;
}
double fixy(double y) {
	if (y < 0) return 0;
	if (y > L) return L;
	return y;
}
bool check()
{
	for (int i = 0; i < n; i++)
		for (int j = i + 1; j < n; j++) {
			double d = sqrt(sqr(x[i] - x[j]) + sqr(y[i] - y[j]));
			if (d <= r[i] + r[j] + eps / 10.) return 0;
		}
	return 1;
}
int main()
{
	freopen("b.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int T, ca = 0;
	for (scanf("%d", &T); T; T--) {
		scanf("%d%d%d", &n, &W, &L);
		for (int i = 0; i < n; i++)
			scanf("%d", r + i);
		for (int C = 0; C < 5; C++) {
			for (int i = 0; i < n; i++) {
				x[i] = ((double)rand() / 32768) * W;
				y[i] = ((double)rand() / 32768) * L;
			}
			double del = 1;
			while (del > 1e-6) {
//				memset(fx, 0, sizeof fx);
	//			memset(fy, 0, sizeof fy);
				for (int i = 0; i < n; i++)
					fx[i] = 0, fy[i] = 0;
				for (int i = 0; i < n; i++)
					for (int j = i + 1; j < n; j++) {
						double d = sqrt(sqr(x[i] - x[j]) + sqr(y[i] - y[j]));
						if (d < r[i] + r[j] + eps) {
							double k = (r[i] + r[j] - d) / (r[i] + r[j]);
//							k = 1;
							fx[i] += (x[i] - x[j]) * k;
							fx[j] += (x[j] - x[i]) * k;
							fy[i] += (y[i] - y[j]) * k;
							fy[j] += (y[j] - y[i]) * k;
						}
					}
				del *= 0.78;
				for (int i = 0; i < n; i++) {
					x[i] = fixx(x[i] + fx[i]);
					y[i] = fixy(y[i] + fy[i]);
				}
			}
			if (check())
				break;
		}
		printf("Case #%d:", ++ca);
		cerr << ca << endl;
		if (check()) {
			for (int i = 0; i < n; i++)
				printf(" %.9f %.9f", x[i], y[i]);
			puts("");
		} else {
			puts("ri");
		}
	}
}
