#include <cmath>
#include <cstdio>
#include <vector>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

int main() {
	int re, n, m;
	long long x, y;
	char buf[1000];
	vector<int> p;

	scanf("%d", &re);
	for (int ri = 1; ri <= re; ++ri) {
		scanf("%s", buf);
		n = strlen(buf);
		p.clear();
		for (int i = 0; i < n; ++i) {
			if (buf[i] == '?') {
				p.push_back(i);
			}
		}

		m = p.size();
		for (int i = 0; i < (1 << m); ++i) {
			for (int j = 0; j < m; ++j) {
				buf[p[j]] = '0' + ((i >> j) & 1);
			}
			y = strtoll(buf, NULL, 2);
			x = (long long)sqrt(y);
			for (int j = -2; j <= 2; ++j) {
				if (x * x == y) {
					printf("Case #%d: %s\n", ri, buf);
					goto NEXT;
				}
			}
		}
NEXT:
		continue;
	}

	return 0;
}

