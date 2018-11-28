#include <iostream>
#define _USE_MATH_DEFINES
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <list>
#include <stack>
#include <queue>
#include <sstream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int N;
	cin >> N;
	long long d[2000], a[2000], g[2000];
	for (int i = 0; i < N; ++i) {
		long long n, m, X, Y, Z;
		cin >> n >> m >> X >> Y >> Z;
		for (int j = 0; j < m; ++j) {
			cin >> g[j];
		}
		for (int j = 0; j < n; ++j) {
			a[j] = g[j % m];
			g[j % m] = (X * g[j % m] + Y * (j + 1)) % Z;
		}
		d[0] = 1;
		for (int i = 1; i < n; ++i) {
			d[i] = 1;
			for (int j = 0; j < i; ++j)
				if (a[j] < a[i]) {
					d[i] += d[j] % 1000000007LL;
					d[i] %= 1000000007LL;
				}
			}
		int ans = 0;
		for (int j = 0; j < n; ++j) {
			ans = (ans + d[j]) % 1000000007;
		}
		cout << "Case #" << i + 1 << ": " << ans << endl;
	}

	return 0;
}
