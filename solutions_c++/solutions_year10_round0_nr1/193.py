#include <iostream>
using namespace std;

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int t, n, k;
	cin >> t;
	for(int i = 1; i <= t; i ++) {
		cin >> n >> k;
		int mask = (1<<n) - 1;
		if((k & mask) == mask) {
			printf("Case #%d: ON\n", i);
		} else {
			printf("Case #%d: OFF\n", i);
		}
	}
	return 0;
}
