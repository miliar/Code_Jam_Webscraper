#include <map>
#include <set>
#include <cmath>
#include <cstdio>
#include <vector>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

double ans;
int cas, n;
vector<int> vec;
double p[1024], f[1024], dp[1024], ci[1024][1024];

int main() {
	freopen("D-large.in", "r", stdin);
	freopen("D-large.out", "w", stdout);
	//n = 1024;
	//f[1] = 1; f[2] = 2;
	//p[1] = 0; p[2] = 1;
	//for (int i = 3; i < n; ++i) {
	//	p[i] = (i - 1) * (p[i - 1] + p[i - 2]);
	//	f[i] = i * f[i - 1];
	//}
	//for (int i = 0; i < n; ++i)
	//	ci[i][0] = 1.0;
	//for (int i = 1; i < n; ++i)
	//	for (int j = 1; j <= i; ++j)
	//		ci[i][j] = ci[i - 1][j] + ci[i - 1][j - 1];
	//int num = 200;
	//dp[0] = 0;
	//dp[1] = 0;
	//for (int i = 2; i <= num; ++i) {
	//	double fac = 1 - p[i] / f[i];
	//	//printf("i = %d, fac = %lf\n", i, fac);
	//	double sum = 1.0;
	//	for (int j = 0; j < i; ++j)
	//		sum += (ci[i][j] * p[j]) / f[i] * dp[j];
	//	dp[i] = sum / fac;
	//	printf("dp[%d] : %lf\n", i, dp[i]);
	//}
	scanf("%d", &cas);
	for (int c = 1; c <= cas; ++c) {
		scanf("%d", &n);
		vec.resize(n);
		for (int i = 0; i < n; ++i) {
			scanf("%d", &vec[i]);
			-- vec[i];
		}
		double num = 0;
		for (int i = 0; i < n; ++i)
			num += (vec[i] != i);
		//dp[0] = 0;
		//dp[1] = 0;
		//for (int i = 2; i <= num; ++i) {
		//	double fac = 1 - p[i] / f[i];
		//	//printf("i = %d, fac = %lf\n", i, fac);
		//	double sum = 1.0;
		//	for (int j = 0; j < i; ++j)
		//		sum += (ci[i][j] * p[j]) / f[i] * dp[j];
		//	dp[i] = sum / fac;
		//}
		printf("Case #%d: %.8lf\n", c, num);
	}
	return 0;
}