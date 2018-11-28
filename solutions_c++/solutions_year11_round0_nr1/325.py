#include <map>
#include <set>
#include <cmath>
#include <cstdio>
#include <vector>
#include <cstring>
#include <algorithm>
using namespace std;

int main() {
	char s[32];
	vector<int> pp[2], order;
	int cas, n, p, ans, cc[2], ic[2];
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	scanf("%d", &cas);
	for (int c = 1; c <= cas; ++c) {
		pp[0].clear();
		pp[1].clear();
		order.clear();
		scanf("%d", &n);
		for (int i = 0; i < n; ++i) {
			scanf("%s%d", s, &p);
			order.push_back(s[0] == 'B');
			pp[order.back()].push_back(p);
		}
		ans = 0;
		ic[0] = ic[1] = 0;
		cc[0] = cc[1] = 1;
		for (int i = 0; i < order.size(); ++i) {
			int ii = order[i];
			int dis = abs(cc[ii] - pp[ii][ ic[ii] ]) + 1;
			ans += dis;
			cc[ii] = pp[ii][ ic[ii]++ ];
			if (cc[1 - ii] < pp[1 - ii][ ic[1 - ii] ])
				cc[1 - ii] += min(dis, abs(pp[1 - ii][ ic[1 - ii] ] - cc[1 - ii]));
			else
				cc[1 - ii] -= min(dis, abs(pp[1 - ii][ ic[1 - ii] ] - cc[1 - ii]));
		}
		printf("Case #%d: %d\n", c, ans);
	}
	return 0;
}