
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;

typedef long long LL;

inline LL getGcd(LL a, LL b) {
	while (a > 0 && b > 0)
		if (a > b) a %= b; else b %= a;
	return a + b;
}

inline LL getLcm(LL a, LL b) {
	LL c = (a / getGcd(a, b));
	if (double(c) * double(b) > (1LL << 61LL))
		return 1LL << 61LL;
	return (a / getGcd(a, b)) * b;
}

int main() {
	int tst;
	scanf("%d", &tst);
	for (int cas = 0; cas < tst; ++cas) {
		LL N, L, H;
		scanf("%lld %lld %lld", &N, &L, &H);
		vector<LL> nums(N);
		for (int i = 0; i < N; ++i)
			scanf("%lld", &nums[i]);
		sort(nums.begin(), nums.end());
		bool done = false;
		for (int i = 0; i <= N && !done; ++i) {
			LL lcm = 1LL;
			LL gcd = 0LL;
			for (int j = 0; j < i; ++j) lcm = getLcm(lcm, nums[j]);
			for (int j = i; j < N; ++j)	gcd = getGcd(gcd, nums[j]);
			if (gcd % lcm != 0) continue;
			LL ratio = gcd / lcm;
			if (H < lcm || gcd < L) continue;
			LL res = -1LL;
			for (LL div = 1LL; div * div <= ratio; ++div)
				if (ratio % div == 0) {
					LL p = div * lcm;
					LL q = ratio / div * lcm;
					if (p >= L && p <= H && (res < 0 || p < res))
						res = p;
					if (q >= L && q <= H && (res < 0 || q < res))
						res = q;
				}
			if (res > 0) {
				printf("Case #%d: %lld\n", cas + 1, res);
				done = true;
			}
		}
		LL lcm = 1LL;
		for (int i = 0; i < N; ++i) lcm = getLcm(lcm, nums[i]);
		LL times = L / lcm;
		for (LL more = -2; more <= 2 && !done; ++more) {
			LL res = (times + more) * lcm;
			if (res >= L && res <= H) {
				printf("Case #%d: %lld\n", cas + 1, res);
				done = true;
			}
		}
		if (!done)
			printf("Case #%d: NO\n", cas + 1);
	}
	return 0;
}