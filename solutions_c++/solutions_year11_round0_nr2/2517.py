#include <cstdio>
#include <list>
#include <map>
#include <utility>

using namespace std;

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		int c;
		scanf("%d", &c);
		map<pair<char, char>, char> cmap;
		while (c--) {
			char c1, c2, c3;
			scanf(" %c%c%c ", &c1, &c2, &c3);
			cmap[make_pair(c1, c2)] = c3;
			cmap[make_pair(c2, c1)] = c3;
		}

		int d;
		scanf("%d", &d);
		map<pair<char, char>, bool> dmap;
		while (d--) {
			char c1, c2;
			scanf(" %c%c ", &c1, &c2);
			dmap[make_pair(c1, c2)] = true;
			dmap[make_pair(c2, c1)] = true;
		}


		list<char> es;
		int n;
		scanf("%d", &n);
		while (n--) {
			char e;
			scanf(" %c ", &e);

			bool opp = false;
			while (!es.empty()) {
				char et = es.back();
				char emap = cmap[make_pair(e, et)];
				if (!emap) emap = cmap[make_pair(et, e)];
				if (emap) {
					es.pop_back();
					e = emap;
					continue;
				} else {
					for (list<char>::iterator it = es.begin(); it != es.end(); ++it) {
						if (dmap[make_pair(*it, e)] || dmap[make_pair(e, *it)]) {
							es.clear();
							opp = true;
							break;
						}
					}
				}
				break;
			}
			if (!opp) es.push_back(e);
		}



		printf("Case #%d: [", i);
		for (list<char>::iterator it = es.begin(); it != es.end(); ++it) {
			if (it != es.begin()) printf(", ");
			printf("%c", *it);
		}
		printf("]\n");
	}
	return 0;
}
