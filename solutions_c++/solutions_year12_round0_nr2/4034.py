#include <cstdio>
#include <algorithm>
#include <functional>

using namespace std;

int st[128];

int main() {
	int t;
	scanf("%d", &t);
	for (int k = 0; k < t; ++k) {
		int n, sup, thres;
		int ret = 0;
		scanf("%d%d%d", &n, &sup, &thres);
		for (int i = 0; i < n; ++i)
			scanf("%d", &st[i]);
		sort(st, st + n, greater<int>());
		for (int i = 0; i < n; ++i) {
			int residual = st[i] - thres;
			if (residual < 0) continue;
			//printf("%d %d\n", st[i], residual);
			if (residual / 2 >= thres - 1) {
				ret ++;
			} else if (sup > 0 && residual / 2 >= thres - 2) {
				ret ++;
				sup --;
			}
		}
		printf("Case #%d: %d\n", k + 1, ret);
	}
	return 0;
}

