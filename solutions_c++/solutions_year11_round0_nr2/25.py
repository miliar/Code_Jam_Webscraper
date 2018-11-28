#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <cstring>

#define MAXC 256

using namespace std;

typedef long long lint;

int combine[MAXC][MAXC], oppose[MAXC][MAXC];

int main()
{
	int ntest;

	scanf("%d", &ntest);

	for (int t = 0; t < ntest; t++) {
		int c, o, n;

		memset(combine, -1, sizeof(combine));
		memset(oppose, 0, sizeof(oppose));

		scanf("%d", &c);
		for (int i = 0; i < c; i++) {
			char c1, c2, c3;
			scanf(" %c %c %c", &c1, &c2, &c3);
			combine[c1][c2] = c3;
			combine[c2][c1] = c3;
		}

		scanf("%d", &o);
		for (int i = 0; i < o; i++) {
			char c1, c2;
			scanf(" %c %c", &c1, &c2);
			oppose[c1][c2] = 1;
			oppose[c2][c1] = 1;
		}

		vector <int> ret;

		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			char c1;
			scanf(" %c", &c1);
			int v = c1;

			if (!ret.empty() && combine[ret.back()][v] != -1) {
				int v2 = combine[ret.back()][v];
				ret.pop_back();
				ret.push_back(v2);
			} else {
				int ok = 1;
				for (int j = 0; j < (int)ret.size(); j++)
					if (oppose[v][ret[j]]) {
						ok = 0;
						break;
					}
				if (!ok)
					ret.clear();
				else
					ret.push_back(v);
			}
		}

		printf("Case #%d: [", t+1);
		for (int i = 0; i < (int)ret.size(); i++) {
			printf("%c", ret[i]);
			if (i+1 < (int)ret.size())
				printf(", ");
		}
		printf("]\n");
	}

	return 0;
}
