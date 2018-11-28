#include <iostream>
#include <algorithm>

#define REP(i, n) for (int i = 0; i < (n); ++i)
#define FOR(i, l, r) for (int i = (l); i <= (r); ++i)
#define ROF(i, r, l) for (int i = (r); i >= (l); --i)

using namespace std;

int T, R, k, N;
int g[2007], where[2007];
long long s[2007];

int main()
{
	scanf("%d", &T);
	FOR(testcase, 1, T) {
		scanf("%d%d%d", &R, &k, &N);
		FOR(i, 1, N) {
			scanf("%d", g + i);
			g[i + N] = g[i];
		}
		FOR(i, 1, N << 1)
			s[i] = s[i - 1] + g[i];
		printf("Case #%d: ", testcase);
		int p = 1;
		long long ans = 0;
		FOR(i, 1, N) {
			int j = i;
			long long tmp = 0;
			while (j <= (N << 1)) {
				tmp += g[j];
				if (tmp > k) break;
				++j;
			}
			where[i] = j;
		}
		REP(i, R) {
//			int j = lower_bound(s + 1, s + (N << 1) + 1, s[p - 1] + k + 1) - s;
			int j = where[p];
			if (j - p >= N) j = p + N;
			ans += s[j - 1] - s[p - 1];
			p = j;
			if (p > N) p -= N;
		}
		printf("%I64d\n", ans);
	}
}
