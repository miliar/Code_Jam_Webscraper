#include <cstdio>
#include <cstring>

using namespace std;

int n, arr[1002];

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("c-large.out", "w", stdout);
	int nca;
	scanf("%d", &nca);
	for (int ii = 1; ii <= nca; ++ii) {
		int n, ans = 0, sum = 0, mini = 10000000;
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			scanf("%d", &arr[i]);
			ans ^= arr[i];
			if (mini > arr[i])
				mini = arr[i];
			sum += arr[i];
		}
		if (ans == 0) {
			printf("Case #%d: %d\n", ii, sum - mini);
		} else {
			printf("Case #%d: NO\n", ii);
		}
	}
	return 0;
}
