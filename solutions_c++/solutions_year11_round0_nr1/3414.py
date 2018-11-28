#include <iostream>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
	int nTests, test;
	scanf("%d", &nTests);
	for (test = 1; test <= nTests; ++test) {
		int n;
		scanf("%d", &n);
		int pos[] = {1, 1};
		int t[] = {0, 0};
		for (int i = 0; i < n; ++i) {
			int x;
			char c;
			scanf(" %c %d", &c, &x);
			int id = (c == 'B') ? 0 : 1;
			t[id] = max(t[id] + abs(pos[id] - x) + 1, t[1 - id] + 1);
			pos[id] = x;
		}
		printf("Case #%d: %d\n", test, max(t[0], t[1]));
	}
	return 0;
}
