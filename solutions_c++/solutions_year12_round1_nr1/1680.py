#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <iostream>
#include <algorithm>
using namespace std;

#define MAX 102
#define INF (double)(1<<30)

int T;
int A, B;
double p[MAX];

double keeptyping()
{
	double rate[MAX];
	double value[MAX];

	for (int i = 0; i < (1<<A); i++) {
		double buf = 1;
		bool f = false;
		for (int j = 0; j < A; j++) {
			if (!((i>>j)&1))
				buf *= p[A-1-j];
			else
				buf *= 1-p[A-1-j], f = true;
		}
		rate[i] = buf;
		value[i] = (f?B+1-A+B+1:B+1-A);
	}
	double ans = 0;
	for (int i = 0; i < (1 << A); i++)
		ans += rate[i] * value[i];
	return ans;
}

double n_back(int n)
{
	double rate[MAX];
	double value[MAX];

	for (int i = 0; i < (1<<A); i++) {
		double buf = 1;
		bool f = true;
		int ni = i;
		for (int j = 0; j < A; j++) {
			if (!((ni>>j)&1)) {
				buf *= p[A-1-j];
			} else {
				buf *= 1-p[A-1-j], f = false;
			}
		}
		ni = ni & (0xFFFF << n);
		rate[i] = buf;
		value[i] = (ni!=0?B-A+3+B+1:B+1-A+2*n);
	}

	double ans = 0;
	for (int i = 0; i < (1 << A); i++)
		ans += rate[i] * value[i];
	return ans;
}

double enterrightaway()
{
	return B+2;
}

double calc()
{
	double ans = INF;

	ans = min(ans, keeptyping());
	for (int i = 1; i <= A; i++) {
		ans = min(ans, n_back(i));
	}
	ans = min(ans, enterrightaway());

	return ans;
}

int main()
{
	cin >> T;
	for (int i = 1; i <= T; i++) {
		cin >> A >> B;
		for (int j = 0; j < A; j++)
			cin >> p[j];
		printf("Case #%d: %.6lf\n", i, calc());
	}
	return 0;
}
