#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;

int _a[4000000];
bool test[50000];
int *a = _a + 2000000;

int solve() {
	memset(_a, 0, sizeof(_a));
	memset(test, 0, sizeof(test));
	int c;
	scanf("%d", &c);
	int left = 0, right = 0;
	for (int i = 0; i < c; ++i) {
		int p, v;
		scanf("%d%d", &p, &v);
		a[p] += v;
		left = min(left, p);
		right = max(right, p);
		test[(p+ 2100000)/512] = 1;
	}
	bool flag;
	int ans = 0;
	do {
		flag = false;
		for (int i = left; i <= right; ++i) {
			if (!test[(i+2100000)/512]) i=((i+2100000)|511)-2100000;
			if (a[i] >= 2) {
				flag = true;
				int t = a[i] / 2;
				a[i] %= 2;
				a[i-1] += t;
				a[i+1] += t;
				ans += t;
				left = min(left, i - 1);
				right = max(right,  i + 1);
				test[(i-1+2100000)/512] = 1;
				test[(i+1+2100000)/512] = 1;
				break;
			}
		}
	} while (flag);
	return ans;
}

int main() {
	freopen("C-small-attempt3.in", "r", stdin);
	freopen("C.out", "w", stdout);
	int T, tc = 0;
	scanf("%d", &T);
	while (T -- > 0) {
		// linux user should change I64d to lld .
		printf("Case #%d: %d\n", ++tc, solve());
		cerr << tc << endl;
	}
	return 0;
}
