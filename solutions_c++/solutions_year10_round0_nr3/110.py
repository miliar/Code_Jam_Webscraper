#include <cstdio>
#include <cstring>

const int MAXN = 1024;

long long r, k, n;
long long g[MAXN];
long long lastround[MAXN];
long long lastsum[MAXN];

long long run()
{
	scanf("%lld %lld %lld", &r, &k, &n);
	long long sum = 0;
	for (int i = 0; i < n; ++i) {
		scanf("%lld", g + i);
		sum += g[i];
		lastround[i] = -1;
	}
	if (sum <= k) {
		return sum * r;
	}
	long long curround = 0;
	long long curind = 0;
	long long cursum = 0;
	for (; curround < r; ++curround) {
		if (lastround[curind] != -1) {
			long long rdiff = curround - lastround[curind];
			long long sumdiff = cursum - lastsum[curind];
			long long rleft = r - curround;
			long long ncount = rleft / rdiff;
			cursum += sumdiff * ncount;
			curround += ncount * rdiff;
			--curround;
			memset(lastround, -1, sizeof(lastround));
		}
		else {
			lastround[curind] = curround;
			lastsum[curind] = cursum;
			long long thissum = 0;
			while (thissum + g[curind] <= k) {
				 thissum += g[curind];
				 ++curind;
				 if (curind == n) curind = 0;
			}
			cursum += thissum;
		}
	}
	return cursum;
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("Cout2.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		printf("Case #%d: %lld\n", i, run());
	}
	return 0;
}
