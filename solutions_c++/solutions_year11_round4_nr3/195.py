#include <map>
#include <cstdio>

using namespace std;

const int MAXN = 1024;
map<int, int> x[MAXN], y[MAXN], z;

map<int, int> gao(int n) {
	map<int, int> ret;
	for (int i = 2; n > 1; ++i) {
		while (n % i == 0) {
			++ret[i];
			n /= i;
		}
	}
	return ret;
}

int main() {
	int re, n, a, b;

	for (int i = 2; i < MAXN; ++i) {
		x[i] = gao(i);
		y[i] = y[i - 1];
		for (map<int, int>::const_iterator j = x[i].begin(); j != x[i].end(); ++j) {
			y[i][j->first] = max(y[i][j->first], j->second);
		}
	}
	scanf("%d", &re);
	for (int ri = 1; ri <= re; ++ri) {
		scanf("%d", &n);

		a = 1;
		z.clear();
		for (int i = 1; i <= n; ++i) {
			bool flag = false;
			for (map<int, int>::const_iterator j = x[i].begin(); j != x[i].end(); ++j) {
				if (z[j->first] < j->second) {
					z[j->first] = j->second;
					flag = true;
				}
			}
			if (flag) {
				++a;
			}
		}

		b = (n == 1 ? 1 : 0);
		z = y[n];
		for (int i = n; i >= 1; --i) {
			bool flag = false;
			for (map<int, int>::const_iterator j = x[i].begin(); j != x[i].end(); ++j) {
				if (z[j->first] == j->second) {
					z[j->first] = -1;
					flag = true;
				}
			}
			if (flag) {
				++b;
			}
		}

		printf("Case #%d: %d\n", ri, a - b);
	}

	return 0;
}

