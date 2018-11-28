#include <cstdio>
#include <vector>
#include <cstring>
#include <string>
#include <map>
#include <utility>
#include <algorithm>
#include <set>
#include <queue>
#include <stack>
#include <list>
#include <cmath>

using namespace std;

int tab[600];
int main(void) {
	int t;
	scanf("%d", &t);
	for (int tc=1; tc<=t; ++tc) {
		int n;
		scanf("%d", &n);
		for (int i=0; i<n; ++i) scanf("%d", tab+i);
		printf("Case #%d:\n", tc);
		map<unsigned, unsigned> mp; 
		bool ok = false;
		for (unsigned u=1; u<(1u<<n); ++u) {
			unsigned s = 0;
			for (unsigned v = u, i=0; v; v /= 2, ++i) {
				if (v&1) s += tab[i];
			}
			if (mp.count(s)) {
				for (unsigned v = mp[s], i=0; v; v /= 2, ++i) {
					if (v&1) {
						printf("%d%c", tab[i], (v/2) ? ' ' : '\n');
					}
				}
				for (unsigned v = u, i=0; v; v /= 2, ++i) {
					if (v&1) {
						printf("%d%c", tab[i], (v/2) ? ' ' : '\n');
					}
				}
				ok = true;
				break;
			} else {
				mp[s] = u;
			}
		}
		if (!ok) printf("Impossible\n");
	}
	return 0;
}
