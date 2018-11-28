#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <map>

using namespace std;

const int oo = 1000000000;

int a, b, a1, b1;
map< pair< int, int >, int > p;

int solve(int x, int y) {
	if (x <= 0 || y <= 0)
		return 0;
	if ((x == 1 && y != 1) || (x != 1 && y == 1))
		return 1;
	if (p.find(make_pair(x, y)) != p.end())
		return p[make_pair(x, y)];
	bool can = false;
	for (int k = 1;y - k * x > 0;k++) {
		if (!solve(x, y - k * x)) {
			can = true;
			break;
		}
	}
	if (!can) {
		for (int k = 1;x - k * y > 0;k++) {
			if (!solve(x - k * y, y)) {
				can = true;
				break;
			}
		}
	}
	return p[make_pair(x, y)] = can;
}

int main() {
	freopen("C-small-attempt1.in", "r", stdin);
	// freopen("test.out", "w", stdout);
	int test;
	scanf("%d", &test);
	for (int testID = 1;testID <= test;testID++) {
		scanf("%d %d %d %d", &a, &a1, &b, &b1);
		int ans = 0;
		for (int x = a;x <= a1;x++) {
			for (int y = b;y <= b1;y++) {
				if (solve(x, y)) {
					ans++;
				}
			}
		}
		printf("Case #%d: %d\n", testID, ans);
	}
	return 0;
}
