#include <iostream>
#include <stdio.h>
#include <string.h>
#include <string>
#include <vector>
#include <algorithm>
#include <queue>
#include <sstream>
#include <set>
#include <map>
using namespace std;

#define N 505

int tt, T, n, i, j, k, res;
int f[N];
int dp[N][N];
long long pw[N], mod;

long long cn[N][N];

long long cnk(int n, int k) {
	return cn[n-k][k];
}

int main() {
	mod = 100003;
	freopen("large.in", "r", stdin);	freopen("large.out", "w", stdout);
	cin >> T;
	f[1] = 1;
	f[2] = 1;
	pw[0] = 1;
	for (i = 1; i < N; i ++) {
		pw[i] = (2 * pw[i-1]) % mod;
	}
	for (i = 3; i < N;i ++) {
		f[i] = (f[i-1] + f[i-2]) % mod;
	}
	for (i = 0; i < N; i ++) {
		cn[i][0] = cn[0][i] = 1;
	}
	for ( i= 1; i < N; i ++) {
		for (j=  1; j < N; j ++) {
			cn[i][j] = (cn[i-1][j] + cn[i][j-1]) % mod;
		}
	}
	for (i = 1; i < N; i ++) {
		dp[i][1] = 1;
	}
	for (i = 2; i < N; i ++) {
		for (j = 2; j < i; j ++) {
			for (k = 1; k < j && j + (j-k) >= i; k ++) {
				dp[i][j] = (dp[i][j] + cnk(j -k - 1,i-j-1) *dp[j][k]) % mod;
			}
		}
	}



	for (tt = 1; tt <= T; tt ++) {
		cin >> n;
		res = 0;
		for (i = 1; i < n; i ++) {
			res = (res + dp[n][i]) % mod;
		}
		printf("Case #%d: %d\n", tt, res);
	}
	return 0;
}