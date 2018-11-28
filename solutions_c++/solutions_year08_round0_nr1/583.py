#include <cstdio>
#include <string>
#include <set>
using namespace std;

set<string> engine;
char buf[128];

int main()
{
	int t, s, q;

	//freopen("A-large.in", "r",stdin);
	//freopen("A-large.out", "w", stdout);

	scanf("%d", &t);
	for (int i = 0; i < t; ++i) {
		engine.clear();
		scanf("%d", &s);
		gets(buf);
		for (int j = 0; j < s; ++j)
			gets(buf);
		scanf("%d", &q);
		gets(buf);
		int res = 0;
		while (q--) {
			gets(buf);
			if (!engine.count(buf)) {
				if (engine.size() == s - 1) {
					engine.clear();
					++res;
				}
				engine.insert(buf);
			}
		}
		printf("Case #%d: %d\n", i + 1, res);
	}
	return 0;
}