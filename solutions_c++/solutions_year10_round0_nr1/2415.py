#include <cstdio>

int Tests;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &Tests);
	for (int Cases = 0; Cases < Tests; ++ Cases) {
		int N, K, Mark = 1;
		scanf("%d%d", &N, &K);
		for (int i = 0; i < N; ++ i) {
			if (K % 2 != 1) {
				Mark = 0;
				break;
			}
			K /= 2;
		}
		printf("Case #%d: %s\n", Cases + 1, Mark ? "ON" : "OFF");
	}
}
