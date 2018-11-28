#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <numeric>

#define Eo(x) { std::cerr << #x << " = " << std::endl; }

typedef long long int64;

#define P 100003
#define maxn (1 << 9)

int a[maxn][maxn];
int c[maxn][maxn];

inline void inc(int& a, int b) {
	a += b;
	a %= P;
}
inline int mul(int a, int b) {
	return (int64(a) * b) % P;
}

int main() {
	int t = 1, tc;
	for(int i = 0, j; i < maxn; i++)
		for(c[i][0] = j = 1; j <= i; j++) {
			c[i][j] = c[i-1][j];
			inc(c[i][j], c[i-1][j-1]);
		}
	a[1][0] = 1;

	for(int i = 2; i < maxn; i++)
		for(int j = 1; j < i; j++)
			for(int k = 0; k < j; k++)
				inc(a[i][j], mul(a[j][k], c[i-j-1][j-k-1]));

	for(scanf("%d", &tc); t <= tc; t++) {
		printf("Case #%d: ", t);
		int n, ans = 0;
		scanf("%d", &n);
		for(int j = 1; j < n; j++)
			inc(ans, a[n][j]);
		printf("%d\n", ans);
	}
	return 0;
}
