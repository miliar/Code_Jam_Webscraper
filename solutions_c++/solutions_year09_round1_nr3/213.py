#include <cmath>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <iostream>

using namespace std;

#define D(x) cout << "> " << #x << " = " << x << '\n'
#define S(X) int(X.size())

inline int nextInt() 
{
	register int ans = 0, sgn = 1;
	register char ch;
	while ((ch = getchar()) < '0') if (ch == '-') sgn = -1;
	do {
		ans *= 10;
		ans += (ch - '0');
	} while ((ch = getchar()) >= '0');
	return sgn * ans;
}

long long dpC[50][50];

long long choose(int n, int k) { 
	if (k > n) return 0;
	return dpC[n][k]; 
}

int seen[50], c, n;
double dp[50];

double f(int got) 
{
	double &ref = dp[got];
	if (seen[got]) return ref;
	seen[got] = 1;

	ref = 0;
	if (got == c) return ref;

	for (int want = 1; want <= min(c - got, n); ++want) {
		double chance = (double)choose(c - got, want) / (double)choose(c, n) * (double)choose(got, n - want);
		ref += chance * (1 + f(got + want));
	}

	if (got >= n) {
		double chanceFail = (double)choose(got, n) / (double)choose(c, n);
		ref += chanceFail;
		ref /= 1.0 - chanceFail;
	}

	return ref;
}

int tt, i, j;

double ret;

int main(void)
{
	int t = nextInt();

	dpC[1][1] = 1;
	for (i = 0; i <= 50; ++i) dpC[i][0] = 1;

	for (i = 1; i <= 40; ++i) 
		for (j = 1; j <= i; ++j) dpC[i][j] = dpC[i - 1][j] + dpC[i - 1][j - 1];

	for (tt = 1; tt <= t; ++tt) 
	{
		c = nextInt();
		n = nextInt();

		memset(seen, 0, sizeof seen);
		if (n == c) ret = 1; else ret = 1 + f(n);

		printf("Case #%d: %lf\n", tt, ret);
	}
	
	return 0;
}