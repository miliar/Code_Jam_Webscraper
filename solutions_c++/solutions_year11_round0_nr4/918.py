#include <iostream>
#include <cstdio>

using namespace std;

const int MXN = 1007;

double c[MXN][MXN];
double d[MXN], f[MXN];
int a[MXN];

void init()
{
	for (int i = 1; i <= 1000; ++i) {
		c[i][0] = c[i][i] = 1;
		for (int j = 1; j < i; ++j)
			c[i][j] = c[i - 1][j] + c[i][j - 1];
	}
	d[0] = 1;
	double cnt = 1;
	for (int i = 1; i <= 1000; ++i) {
		cnt /= i;
		if (i & 1) d[i] = d[i - 1] - cnt;
		else d[i] = d[i - 1] + cnt;
	}
	for (int i = 1; i <= 1000; ++i) {
		f[i] = 1;
		double k = 1;
		for (int j = 1; j < i; ++j) {
			k /= j;
			f[i] += k * d[i - j] * f[i - j];
		}
		f[i] /= (1 - d[i]);
	}
}

int main()
{
	int T;
	scanf("%d", &T);
	init();
	for (int numCase = 1; numCase <= T; ++numCase) {
		int n, m =0;
		scanf("%d", &n);
		for (int i = 1; i <= n; ++i)
			scanf("%d", a + i);
		for (int i = 1; i <= n; ++i)
			if (a[i] != i) ++m;
		printf("Case #%d: %.6f\n", numCase, f[m]);
	}
}
