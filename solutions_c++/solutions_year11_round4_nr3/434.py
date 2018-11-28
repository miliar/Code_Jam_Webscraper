#include <iostream>
#include <cmath>
#include <cstdio>

using namespace std;

const int MXN = 1000007;

int T;
long long n;
bool np[MXN];
int p[MXN];
int cnt;

int main()
{
	for (int i = 2; i <= 1000000; ++i) {
		if (!np[i]) p[cnt++] = i;
		for (int j = 0; j < cnt && i * p[j] <= 1000000; ++j) {
			np[i * p[j]] = true;
			if (i % p[j] == 0) break;
		}
	}
	scanf("%d", &T);
	int numCase = 0;
	while (T--) {
		scanf("%I64d", &n);
		if (n == 1) {
			printf("Case #%d: %d\n", ++numCase, 0);
			continue;
		}
		int ans = 0;
		for (int i = 0; i < cnt; ++i) {
			if (p[i] > n) break;
			ans += int(log(1.0 * n) / log(p[i])) - 1;
		}
		printf("Case #%d: %d\n", ++numCase, ans + 1);
	}
}
