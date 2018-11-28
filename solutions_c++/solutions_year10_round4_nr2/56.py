#include <cstdio>
#include <algorithm>

using namespace std;

const int MAXN = 1 << 10;
const int INF = 0x7FFFFFFF;

int m[MAXN];
int p;

int maxval[MAXN][12];

int price[12][MAXN];

int dp[12][12][MAXN];

int getdp(int lev, int already, int ind, int from, int to)
{
	int &ret = dp[lev][already][ind];
	if (ret != -1) return ret;
	ret = INF;
	if (lev == 0) {
		int mx = maxval[from][lev + 1];
		if (already >= mx) {
			return ret = 0;
		}
		else {
			return ret = price[lev][ind];
		}
	}
	else {
		int mx = maxval[from][lev + 1];
		if (already + lev >= mx) {
			ret = getdp(lev - 1, already, ind * 2, from, (from + to) >> 1) + getdp(lev - 1, already, ind * 2 + 1, (from + to) >> 1, to);
		}
		ret = min(ret, price[lev][ind] + getdp(lev - 1, already + 1, ind * 2, from, (from + to) >> 1) + getdp(lev - 1, already + 1, ind * 2 + 1, (from + to) >> 1, to));
		return ret;
	}
}

int run()
{
	scanf("%d", &p);
	for (int i = 0; i < (1 << p); ++i) {
		scanf("%d", m + i);
		m[i] = p - m[i];
		maxval[i][0] = m[i];
	}
	for (int j = 1; j <= p; ++j) {
		int step = (1 << j);
		int half = step / 2;
		for (int i = 0; i < (1 << p); i += step) {
			maxval[i][j] = max(maxval[i][j - 1], maxval[i + half][j - 1]);
		}
	}
	for (int i = 0; i < p; ++i) {
		for (int j = 0; j < (1 << (p - i - 1)); ++j) {
			scanf("%d", &price[i][j]);
		}
	}
	memset(dp, -1, sizeof(dp));
	return getdp(p - 1, 0, 0, 0, (1 << p));
}

int main()
{
	freopen("B1.in", "r", stdin);
	freopen("B1.out", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		printf("Case #%d: %d\n", i, run());
	}
	return 0;
}