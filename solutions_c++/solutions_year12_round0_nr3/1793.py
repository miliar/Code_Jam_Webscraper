#include <iostream>
#include <cstdlib>
#include <cstdio>
using namespace std;
int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int test, a, b, tmp, ss, t, q[10];
	scanf("%d", &test);
	for (int tes = 1; tes <= test; ++tes) {
		scanf("%d %d", &a, &b);
		int ans = 0;
		for (int i = a; i <= b; ++i) {
			tmp = i;
			ss = 1;
			while (tmp  != 0) tmp = tmp / 10, ss *= 10; 
			tmp = i;
			ss = ss / 10;
			int t = 0;
			while (tmp / 10 + tmp % 10 * ss != i) {
				q[++t] = tmp / 10 + tmp % 10 * ss;
				if (q[t]/ss == 0) --t;
				else if (q[t] >= a && q[t] <= b) ans++;
				tmp = tmp / 10 + tmp % 10 * ss;
			}
		}
		ans /= 2;
		printf("Case #%d: %d\n", tes, ans);
	}
	return 0;
}