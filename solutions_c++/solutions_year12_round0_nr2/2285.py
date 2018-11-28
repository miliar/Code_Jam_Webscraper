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

int main(void) {
	int tn;
	scanf("%d", &tn);
	for (int tc=1; tc<=tn; ++tc) {
		int n, s, p, ret = 0;
		scanf("%d%d%d", &n, &s, &p);
		while (n--) {
			int t;
			scanf("%d", &t);
			if (t < p) continue;
			if ((t+2)/3 >= p) {
				++ret;
			} else if (s && (t+4)/3 >= p) {
				++ret;
				--s;
			}
		}
		printf("Case #%d: %d\n", tc, ret);
	}
	return 0;
}
