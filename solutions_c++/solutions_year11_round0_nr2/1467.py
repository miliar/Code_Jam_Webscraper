#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <stack>

using namespace std;

namespace gcj {
	
	const int N = 110;
	const int D = 30;

	char trans[D][D];
	bool oppo[D][D];

	int c, d;

	char str[N];
	

	void solve() {
		int tc, l;
		scanf("%d", &tc);
		for (int ti = 1; ti <= tc; ti++) {
			memset(trans, '\0', sizeof(trans));
			memset(oppo, false, sizeof(oppo));
			scanf("%d", &c);
			for (int i = 0; i < c; i++) {
				scanf("%s", str);
				trans[str[0] - 'A'][str[1] - 'A'] = str[2];
				trans[str[1] - 'A'][str[0] - 'A'] = str[2];
			}
			scanf("%d", &d);
			for (int i = 0; i < d; i++) {
				scanf("%s", str);
				oppo[str[0] - 'A'][str[1] - 'A'] = true;
				oppo[str[1] - 'A'][str[0] - 'A'] = true;
			}
			scanf("%d", &l);
			scanf("%s", str);
			int p = 1;
			for (int i = 1; i < l; i++, p++) {
				str[p] = str[i];
				if (trans[str[p - 1] - 'A'][str[p] - 'A'] != '\0') {
					str[p - 1] = trans[str[p - 1] - 'A'][str[p] - 'A'];
					p--;
				}
				for (int j = p - 1; j >= 0; j--) {
					if (oppo[str[j] - 'A'][str[p] - 'A']) {
						p = -1;
						break;
					}
				}
			}
			printf("Case #%d: [", ti);
			for (int i = 0; i < p; i++) {
				if (i != 0)
					printf(", ");
				printf("%c", str[i]);
			}
			printf("]\n");
		}
 	}
}

int main() {

	gcj::solve();
	return 0;
}