#include <set>
#include <string>
#include <cstdio>
#include <algorithm>

using namespace std;

int main() {
	int re, p, n, m;

	scanf("%d", &re);
	for (int ri = 1; ri <= re; ++ri) {
		scanf("%d", &p);
		n = 1 << p;
		set<string> ss;
		for (int i = 0; i < n; ++i) {
			scanf("%d", &m);
			m = p - m;
			string s = "";
			for (int j = 0; j < m; ++j) {
				s += ((i >> (p - j)) & 1) ? '1' : '0';
				ss.insert(s);
				// printf("%d: %s\n", i, s.c_str());
			}
		}
		for (int i = 1; i < n; ++i) {
			scanf("%*d");
		}
		printf("Case #%d: %d\n", ri, ss.size());
	}

	return 0;
}

