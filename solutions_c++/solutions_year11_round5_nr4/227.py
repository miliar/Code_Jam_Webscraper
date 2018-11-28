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
		char s[70];
		int n, sz = 0, a[70];
		llong add = 0;
		scanf("%s", s);
		n = strlen(s);
		for (int i = 0; i < n; i++) {
			if (s[i] == '?')
				a[sz++] = i;
			else if (s[i] == '1')
				add += (1ll << (n - i - 1));
		}
		for (int i = 0; i < (1 << sz); i++) {
			llong now = add;
			for (int j = 0; j < sz; j++)
				if (i & (1 << j))
					now += (1ll << (n - a[j] - 1));
			llong q = sqrt(now);
			if (q * q == now) {
				for (int j = 0; j < sz; j++) {
					if (i & (1 << j))
						s[a[j]] = '1';
					else
						s[a[j]] = '0';
				}
				printf("Case #%d: %s\n", t, s);
				break;
			}
		}
	}
	return 0;
}

