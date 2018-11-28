#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;

int n;
long long f[40];

int main() {
	freopen("A-large.in", "r", stdin);	
	freopen("a.out", "w", stdout);
	int i, j, t;
	long long k;
	for (i = 1; i <= 36; ++i)
		f[i] = f[i - 1] * 2 + 1;
	scanf("%d", &t);
	for (j = 1; j <= t; ++j) {
		cin >> n >> k;
		if (k >= f[n] && (k - f[n]) % (f[n] + 1) == 0)
			printf("Case #%d: ON\n", j); else
			printf("Case #%d: OFF\n", j);
	}
	return 0;
}
