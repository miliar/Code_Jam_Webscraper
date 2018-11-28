#include <iostream>
#include <vector>
#include <cstring>

using namespace std;

const int max_n = 2000;

int r, k, n, a[max_n], g[max_n];
long long sum[max_n];
bool vis[max_n];

long long  profit(int i, int j) {
	j = (j + n) % n;
	if (j < i)
		j += n;
	return (long long)sum[j] - (long long)((i == 0)? 0: sum[i - 1]);
}

int main() {
	freopen("C-large.in", "r", stdin);
	freopen("out.out", "w", stdout);
	int test;
	scanf("%d", &test);
	for (int testID = 1;testID <= test;testID++) {
		long long ans = 0;
		memset(sum, 0, sizeof(sum));
		memset(g, 0, sizeof(g));
		memset(vis, false, sizeof(vis));
		scanf("%d %d %d", &r, &k, &n);
		for (int i = 0;i < n;i++) {
			scanf("%d", &a[i]);
			if (i > 0)
				sum[i] += sum[i - 1];
			sum[i] += a[i];
		}
		for (int i = n;i < n + n;i++)
			sum[i] = sum[i - 1] + a[i - n];
		for (int i = 0;i < n;i++) {
			long long ss = (i == 0)? 0: sum[i - 1];
			for (int j = i;j < n + i && sum[j] - ss <= k;j++) {
				g[i] = j % n;
			}
		}
		for (int i = 0;i < n;i++)
			g[i] = (g[i] + 1) % n;
		int node = 0;
		vector< int > c;
		while (!vis[node]) {
			vis[node] = true;
			c.push_back(node);
			node = g[node];
		}
		int cyc = g[c[c.size() - 1]];
		while (c[0] != cyc) {
			ans += profit(c[0], g[c[0]] - 1);
			c.erase(c.begin());
			r--;
		}
		if (r && c.size() > 1) {
			long long full = r / c.size(), part = r % c.size();
			for (int i = 0;i < c.size();i++) {
				ans += (long long)full * (long long)profit(c[i], g[c[i]] - 1);
				if (i < part) {
					ans += (long long)profit(c[i], g[c[i]] - 1);
				}
			}
		}
		else if (r && c.size() == 1) {
			if ((long long)profit(c[0], c[0] - 1) <= k) {
				ans += (long long)r * (long long)profit(c[0], c[0] - 1);
			}
			else if (a[c[0]] <= k){
				ans += (long long)r * (long long)a[c[0]];
			}
		}
		printf("Case #%d: %lld\n", testID, ans);
	}
	return 0;
}