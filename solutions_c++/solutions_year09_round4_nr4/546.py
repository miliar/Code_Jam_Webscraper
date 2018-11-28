#include <iostream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <algorithm>
#include <queue>
#include <fstream>
using namespace std;

int matrix[50];
double max(double a, double b) {
	return a > b ? a : b;
}
double min(double a, double b){
	return a < b ? a : b;
}
	double x[10];
	double y[10];
	double r[10];
	double sqr(double a){ 
		return a * a;
	}
	double distance(int a, int b) {
		return sqrt(sqr(x[a] - x[b]) + sqr(y[a] - y[b]));
	}
int main()
{
	//freopen("a-small.in", "r", stdin);
	freopen("a-small.out", "w", stdout);
	ofstream fout("a-small.out");
	ifstream fin("a-small.in");
	int testcases;
	scanf("%d", &testcases);
	for (int tt=1; tt<=testcases; ++tt) {
		int N, i;
		scanf("%d", &N);
		for (i=0; i<N; ++i) {
			int xx, yy, rr;
			scanf("%d%d%d", &xx, &yy, &rr);
			x[i] = (double)xx;
			y[i] = (double)yy;
			r[i] = (double)rr;
		}
		if (N == 1) {
			printf("Case #%d: %0.7lf\n", tt, r[0]);
			continue;
		}
		if (N == 2) {
			printf("Case #%d: %0.7lf\n", tt, max(r[0], r[1]));
			continue;
		}
		if (N == 3) {
			double dis1 = distance(0, 1) + r[0] + r[1];
			double ans = max(dis1, 2 * r[2]);
			dis1 = distance(0, 2) + r[0] + r[2];
			ans = min(ans, max(dis1, 2 * r[1]));
			dis1 = distance(1, 2) + r[1] + r[2];
			ans = min(ans, max(dis1, 2 * r[0]));
			printf("Case #%d: %0.7lf\n", tt, ans / 2);
		}
	}

	return 0;
}