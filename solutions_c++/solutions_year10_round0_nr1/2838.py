#include <iostream>
#include <cstdio>
#include <set>

using namespace std;

//int state[32];
//set<int> d[32];

int main() {
	//freopen("input.txt", "r", stdin);
	int t;
	cin >> t;
	/*for (int n = 2; n <= 32; n++) {
		fill(state, state + 32, false);
		int pow = 0;
		for (int k = 0; k <= 1000000001; ++k) {
			if (pow == n) {
				d[n].insert(k);
				printf("%d\n", k);
			}
			for (int p = 0; p <= pow; ++p) {
				state[p] = !state[p];
			}
			pow = 0;
			while (pow < n && state[pow]) {
				++pow;
			}
		}
	}*/

	for (int i = 1; i <= t; ++i) {
		printf("Case #%d:", i);
		int n, k;
		cin >> n >> k;
		int expn = 1 << n;
		bool res = ( (k % expn) == (expn - 1) );
		if (res) {
			printf(" ON\n");
		}
		else {
			printf(" OFF\n");
		}
	}
}
