#include <cstdio>
#include <algorithm>
using namespace std;

int main() {
	int task;
	scanf("%d", &task);
	for (int oo = 0; oo < task; oo++) {
		int n;
		scanf("%d", &n);
		int sum = 0, mmin, xsum = 0;
		for (int i = 0; i < n; i++) {
			int buffer;
			scanf("%d", &buffer);
			mmin = i ? min(mmin, buffer) : buffer;
			sum += buffer;
			xsum ^= buffer;
		}
		printf("Case #%d: ", oo + 1);
		if (xsum) {
			puts("NO");
		} else {
			printf("%d\n", sum - mmin);
		}
	}
	return 0;
}
