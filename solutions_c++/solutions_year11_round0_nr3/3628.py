#include <cstdio>
#include <algorithm>

using namespace std;

int n;
int candy[1000];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int r;
	int case_no = 0;
	scanf("%d", &r);
	while (r--) {
		scanf("%d", &n);
		int chk = 0;
		int sum = 0;
		for (int i = 0; i < n; ++i) {
			scanf("%d", &candy[i]);
			chk ^= candy[i];
			sum += candy[i];
		}

		sort(candy, candy + n);
		sum -= candy[0];
		if (chk != 0) {
			printf("Case #%d: NO\n", ++case_no);
		} else {
			printf("Case #%d: %d\n", ++case_no, sum);
		}

	}
}