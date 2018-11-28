#include <iostream>
using namespace std;

const int limit = 20000000 + 10;

int tcase, totp;
int pr[limit + 10];
bool notp[limit + 10];
long long n;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	//get prime
	totp = 0;
	for (int i = 2; i < limit; ++i) {
		if (!notp[i]) pr[totp ++] = i;
		for (int j = 0; j < totp; ++j) {
			if ((long long)i * pr[j] >= limit) break;
			notp[i * pr[j]] = 1;
			if (i % pr[j] == 0) break;
		}
	}

	//main procedure
	scanf("%d", &tcase);
	for (int k = 1; k <= tcase; ++k) {
		scanf("%d", &n);
		long long ans = 0;
		for (int i = 0; (long long)pr[i] * pr[i] <= n; ++i) {
			long long tmp = pr[i];
			int cnt = 0;
			while (tmp <= n) {
				tmp *= pr[i];
				++ cnt;
			}
			ans += cnt - 1;
		}
		if (n > 1) ans += 1;
		printf("Case #%d: %d\n", k, ans);
	}
	return 0;
}

