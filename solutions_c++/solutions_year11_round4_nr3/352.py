#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>

using namespace std;

const int MAXN = 1000005;

int minp[MAXN + 1], plist[MAXN + 1];

int prime(int n = MAXN) {
	int num = 0;
	memset(minp, 0, sizeof(minp));
	for (int i = 2; i <= n; ++i) {
		if (!minp[i]) plist[num++] = i, minp[i] = i;;
		for (int j = 0; j < num && i * plist[j] <= n; ++j) {
			minp[i * plist[j]] = plist[j];
			if (i % plist[j] == 0) break;
		}
	}
	return num;
}

int T;
long long n;

int main() {
	prime();
	scanf("%d", &T);
	for (int caseNum = 1; caseNum <= T; ++caseNum) {
		scanf("%lld", &n);
		long long res = n != 1 ? 1 : 0;
		for (int i = 0; (long long)plist[i] * plist[i] <= n; ++i) {
			int times = 0;
			for (long long j = 1; j * plist[i] <= n; j *= plist[i], ++times);
			res += times - 1;
		}
		printf("Case #%d: %lld\n", caseNum, res);
	}
	return 0;
}
