/*#include <iostream>
#include <vector>
#include <cstdio>
#include <cstdlib>

using namespace std;
#include <assert.h>

const int MAX_N = 16;

int c[MAX_N][MAX_N];

inline int next(int x)
{
	int lo = x & -x;
	int nx = x + lo;
	return nx | ((nx & -nx) / lo / 2 - 1);
}

double expected(int n, int k)
{
	vector<double> exp(1 << n);
	for (int set = (1 << n) - 2; set >= 0; --set) {
		int a = c[n][k];
		double b = c[n][k];
		for (int x = (1 << k) - 1; (x >> n & 1) == 0; x = next(x)) {
			if ((set | x) == set)
				--a;
			else
				b += exp[set | x];
		}
		assert(a > 0);
		exp[set] = b / a;
	}
	return exp[0];
}

int main()
{
	FILE *fp = fopen("out.txt","w");
	
	memset(c, 0, sizeof(c));
	c[0][0] = 1;
	for (int i = 1; i < MAX_N; ++i) {
		c[i][0] = 1;
		for (int j = 1; j < MAX_N; ++j) 
			c[i][j] = c[i - 1][j] + c[i - 1][j - 1];
	}
	
	int T;
	cin >> T;
	for (int ncases = 1; ncases <= T; ++ncases) {
		int n;
		int k;
		cin >> n >> k;
		fprintf(fp,"Case #%d: %.7f\n", ncases, expected(n, k));
	}
	fclose(fp);
	return 0;
}
*/