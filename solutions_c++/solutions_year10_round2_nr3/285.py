#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;

const int M = 100003;
int com[1024][1024];

int c(int n, int m) {
	if (m > n || n < 0 || m < 0) return 0;
	else if (m == 0 || m == n) return 1;
	if (com[n][m] != -1) return com[n][m];
	int &res = com[n][m];
	res = (c(n-1, m-1) + c(n-1, m)) % M;
	return res;
}

int f[512][512];

int solve(int n) {
	memset(f, 0, sizeof(f));
	for (int i = 1; i < n; ++i) f[i][n] = 1;
	for (int i = n-2; i > 0; --i) {
		for (int j =i+1; j < n; ++j) {
			for (int k = j+1; k <= n; ++k)
				f[i][j] = (f[i][j] + (long long) c(k-j-1, j-i-1) * f[j][k]) % M;
		}
	}
	int res = 0;

	for (int i = 2; i <= n; ++i) {
		res = (res + f[1][i]) % M;
	}
	return res;
}

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	
	memset(com, 255, sizeof(com));
	
	int T;
	cin >> T;
	for (int tc = 1; tc <= T; ++tc) {
		int n;
		cin >> n;
		printf("Case #%d: %d\n", tc, solve(n));
	}
	return 0;
}
