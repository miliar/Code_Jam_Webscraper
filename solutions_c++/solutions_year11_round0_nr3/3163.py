#include <algorithm>
#include <cstdio>
#include <vector>

using namespace std;

int main() {
	int nt;
	scanf("%d", &nt);
	for (int it = 1; it <= nt; it++) {
		int n;
		scanf("%d", &n);
		vector<int> a(n);
		int res = 0;
		for (int i = 0; i < n; i++) {
			scanf("%d", &a[i]);
			res ^= a[i];
		}
		if (res != 0) {
			printf("Case #%d: NO\n", it);
			continue;
		}
		sort(a.begin(), a.end());
		res = 0;
		for (int i = 1; i < (int)a.size(); i++) {
			res += a[i];
		}
		printf("Case #%d: %d\n", it, res);
	}
	return 0;
}
