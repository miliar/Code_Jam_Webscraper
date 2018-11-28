#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int nCase;
	scanf("%d", &nCase);
	for (int re = 1; re <= nCase; ++re) {
		int n;
		scanf("%d", &n);
		vector<int> candy(n);
		int res = 0, minc = 10000000, sum = 0;;
		for (int i = 0; i < n; ++i) {
			scanf("%d", &candy[i]);
			res ^= candy[i];
			sum += candy[i];
			minc = min(minc, candy[i]);
		}
		printf("Case #%d: ", re);
		if (res != 0) {
			puts("NO");
		} else {
			printf("%d\n", sum - minc);
		}
	}
	return 0;
}
