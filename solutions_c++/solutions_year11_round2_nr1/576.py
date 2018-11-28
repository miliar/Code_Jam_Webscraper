#include <algorithm>
#include <iostream>
#include <sstream>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <vector>
#include <string>
#include <set>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <cstdlib>
#include <cstring>

#define sz(a) (int)a.size()
#define all(a) a.begin(), a.end()
#define rall(a) a.rbegin(), a.rend()
#define llong long long
#define zero(a) fabs(a) < 1e-9
#define resz(a, n) a.clear(), a.resize(n)
#define same(a, n) memset(a, n, sizeof(a))
#define make(a, b) make_pair(a, b)

using namespace std;

int main() {
	int test;
	scanf("%d", &test);
	for (int t = 1; t <= test; t++) {
		char b[105][105];
		int n, win[105] = {0}, play[105] = {0};
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			scanf("%s", b[i]);
			for (int j = 0; j < n; j++) {
				if (b[i][j] != '.')
					play[i]++;
				if (b[i][j] == '1')
					win[i]++;
			}
		}
		double owp[105] = {0};
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++)
				if (j != i && b[j][i] != '.')
					owp[i] += (double)(win[j] - (b[j][i] == '1')) / (play[j] - 1);
			owp[i] /= play[i];
		}
		printf("Case #%d:\n", t);
		for (int i = 0; i < n; i++) {
			double now = 0.25 * win[i] / play[i] + 0.50 * owp[i], get = 0;
			for (int j = 0; j < n; j++)
				if (b[i][j] != '.')
					get += owp[j];
			now += 0.25 * get / play[i];
			printf("%.9lf\n", now);
		}
	}
	return 0;
}

