#include <cstdio>
#include <cstring>
typedef long long LL;

int main() {
	int t, r, k, n;
	scanf("%d", &t);
	for (int z=1; z<=t; z++) {
		scanf("%d%d%d", &r, &k, &n);
		int g[n], idx[n];
		LL bef[n], aft[n];
		memset(idx, -1, sizeof(idx));
		for (int i=0; i<n; i++)
			scanf("%d", g + i);
		LL in = 0;
		int i = 0, cnt = 0, last = -1;
		while (cnt < r && idx[i] == -1) {
			idx[i] = cnt++;
			bef[i] = in;
			last = i;
			LL pass = 0;
			for (int j = 0; j < n && pass + g[i] <= k; j++, i++, i%=n) {
				pass += g[i];
			}
			in += pass;
			aft[last] = in;
		}
		LL ans = in;
		if (cnt < r) {
			int per = idx[last] - idx[i] + 1;
			int mul = (r - cnt) / per;
			int rem = (r - cnt) % per;
			int tar = idx[i] + rem;
			ans += (aft[last] - bef[i]) * mul;
			for (int j = 0; j < n; j++)
				if (idx[j] == tar) {
					ans += bef[j] - bef[i];
				}
		}
		printf("Case #%d: %lld\n", z, ans);
	}
	return 0;
}
