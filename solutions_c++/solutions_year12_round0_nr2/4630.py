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

const int MAXN = 105;

int n, s, p;

int main() {
	freopen("B-large.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int test = 0; test < t; test++) {
		scanf("%d %d %d", &n, &s, &p);
		int ans = 0;
		for (int i = 0; i < n; i++) {
			int x;
			scanf("%d", &x);
			bool f[2] = {false};
			for (int j = -1; j < 1; j++) {
				int q = max(0, x / 3 + j);
				for (int a = 0; a <= 2; a++)
					for (int b = 0; b <= 2; b++)
						for (int c = 0; c <= 2; c++) {
							if (3 * q + a + b + c == x && max(q + a, max(q + b, q + c)) >= p) {
								if (a == 2 || b == 2 || c == 2)
									f[1] = true;
								else
									f[0] = true;
							}
						}
			}
			if (f[0])
				ans++;
			else if (f[1] && s) {
				ans++;
				s--;
			}
		}
		printf("Case #%d: %d\n", test + 1, ans);
	}
	return 0;
}

