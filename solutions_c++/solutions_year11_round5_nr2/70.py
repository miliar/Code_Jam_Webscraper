#include <map>
#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

const int MAXN = 1024;

int main() {
	int re, n, a;
	vector<int> v;
	map<int, int> c;

	scanf("%d", &re);
	for (int ri = 1; ri <= re; ++ri) {
		scanf("%d", &n);
		v.clear();
		c.clear();
		for (int i = 0; i < n; ++i) {
			scanf("%d", &a);
			c[a - 1];
			++c[a];
		}

		for (map<int, int>::const_iterator i = c.begin(); i != c.end(); ++i) {
			if (i->second == 0) {
				continue;
			}
			for (int j = c[i->first - 1]; j < i->second; ++j) {
				v.push_back(i->first);
			}
		}
	
		printf("Case #%d: ", ri);
		if (n == 0) {
			puts("0");
		} else {
			for (int t = 0; ; ++t) {
				for (vector<int>::iterator i = v.begin(); i != v.end(); ++i) {
					if (c[*i] == 0) {
						printf("%d\n", t);
						goto END;
					} else {
						--c[*i];
						++*i;
					}
				}
			}
END:
			;
		}
	}

	return 0;
}
