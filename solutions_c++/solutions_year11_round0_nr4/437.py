#include <cstdio>

int main() {
	int task;
	scanf("%d", &task);
	for (int oo = 0; oo < task; oo++) {
		int n, m = 0;
		scanf("%d", &n);
		for (int i = 0; i < n; i++) {
			int buffer;
			scanf("%d", &buffer);
			m += buffer - 1 != i;
		}
		printf("Case #%d: %d\n", oo + 1, m);
	}
	return 0;
}
