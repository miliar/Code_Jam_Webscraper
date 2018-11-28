#include <cstdio>
using namespace std;
#include <vector>
const int MAXN = 510;
const int MOD = 100003;

long long a[MAXN][MAXN];
long long C[MAXN][MAXN];

void init() {
	C[0][0] = 1;
	for (int i = 1; i < MAXN; ++i) {
		C[i][0] = C[i][i] = 1;
		for (int j = 0; j < i; ++j) {
			C[i][j] = (C[i - 1][j] + C[i - 1][j - 1]) % MOD;
		}
	}
	a[1][0] = 1;
	for (int n = 2; n < MAXN; ++n) {
		a[n][0] = 0;
		a[n][1] = 1;
		for (int k = 2; k < n; ++k) {
			a[n][k] = 0;
			for (int in_first = 0; in_first <= k - 2; ++in_first) {
				//(in_first)... k ... (in_second) ... n
				int in_second = k - in_first - 2;
				if ((in_second >= 0) && (in_second <= n - k - 1)) {
					a[n][k] += a[k][in_first + 1] * C[n - k - 1][in_second];
					a[n][k] %= MOD;
				}
			}
		}
	}
}

int get(int n) {
	int ans = 0;
	for (int i = 1; i < n; ++i)
		ans = (ans + a[n][i]) % MOD;
	return ans;
}

bool check(vector<int> a) {
	int t = a.size();
	while (t != 1) {
		bool found = false;
		for (int i = 0; i < a.size(); ++i)
			if (a[i] == t) {
				found = true;
				t = i + 1;
				break;
			}
		if (!found)
			return false;
	}
//	for (int i = 0; i < a.size(); ++i)
//		printf("%d ", a[i]);
//		printf("\n");
	return true;
}

int naiveget(int n) {
	int ans = 0;
	for (int k = 0; k < (1 << n); ++k) {
		vector<int> r;
		r.clear();
		for (int i = 0; i < n; ++i)
			if ((k & (1 << i)) != 0)
				r.push_back(i + 1);
		if (((k & (1 << 0)) == 0) && ((k & (1 << (n - 1))) != 0) && check(r))
			++ans;
	}
	return ans;
}

int main() {
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	init();
	int T;
	scanf("%d", &T);
	for (int i = 0; i < T; ++i) {
		int n;
		scanf("%d", &n);
		printf("Case #%d: %d\n", i + 1, get(n));
	}
}
