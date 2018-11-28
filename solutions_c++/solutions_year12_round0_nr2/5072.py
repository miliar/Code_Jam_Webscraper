#include<iostream>
#include<cstdio>

using namespace std;

int main() {
	int testcase, n, s, p, ans;
	int k1, k2;
	int t;
	cin >> testcase;
	for (int i = 0; i < testcase; i++) {
		cin >> n >> s >> p;
		if (p == 1) s = 0;
		k1 = p * 3 - 4;
		k2 = p * 3 - 2;
		ans = 0;
		for (int j = 0; j < n; j++) {
			cin >> t;
			if (t >= k2) ans ++;
				else if (t >= k1 && s > 0) {
					s --;
					ans ++;
				}
		}
		printf("Case #%d: %d\n", i + 1, ans);
	}
}