#include <iostream>
#include <cstdio>

using namespace std;

int n, k, b, t;
int pos[50], speed[50];

inline void task() {
	scanf("%d %d %d %d", &n, &k, &b, &t);
	for (int i = 0; i < n; i++)
		scanf("%d", pos + i);
	for (int i = 0; i < n; i++)
		scanf("%d", speed + i);
	
	int r = 0, swaps = 0;	
	for (int i = n - 1; i >= 0; i--) {
		if (!k) {
			printf("%d\n", r);
			return;
		}
	
		if ((b - pos[i] + speed[i] - 1) / speed[i] <= t) {
			r += swaps;
			k--;
		} else {
			swaps++;
		}
	}
	
	if (!k) {
		printf("%d\n", r);
		return;
	}
	
	printf("IMPOSSIBLE\n");
}

int main() {
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		task();
	}
}

