#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

typedef long long ll;
typedef pair<ll, ll> pii;

const int h = 505;

int T, n, m, d;
ll w[h][h], W[h][h];
pii a[h][h], A[h][h];
char c[h];

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d", &T);
	for (int t = 0; t < T; t++) {
		scanf("%d%d%d%*c", &n, &m, &d);
		for (int i = 0; i <= n; i++)
			for (int j = 0; j <= m; j++) {
				W[i][j] = w[i][j] = 0;
				A[i][j] = a[i][j] = make_pair(0, 0);
			}
		for (int i = 0; i < n; i++) {
			gets(c);
			for (int j = 0; j < m; j++) {
				W[i+1][j+1] = w[i+1][j+1] = c[j] - '0' + d;
				A[i+1][j+1] = a[i+1][j+1] = make_pair((i+1)*2*w[i+1][j+1], (j+1)*2*w[i+1][j+1]);
			}
		}
		for (int i = 1; i <= n; i++)
			for (int j = 1; j <= m; j++) {
				w[i][j] = w[i][j] + w[i-1][j] + w[i][j-1] - w[i-1][j-1];
				a[i][j].first = a[i][j].first + a[i-1][j].first + a[i][j-1].first - a[i-1][j-1].first;
				a[i][j].second = a[i][j].second + a[i-1][j].second + a[i][j-1].second - a[i-1][j-1].second;
			}
		int ans = 0;
		for (int k = 3; k < h; k++) {
			for (int i = 1; i <= n-k+1; i++) {
				for (int j = 1; j <= m-k+1; j++) {
					pii c = make_pair(i + i + k - 1, j + j + k - 1);
					pii pmp = make_pair(a[i+k-1][j+k-1].first - a[i-1][j+k-1].first - a[i+k-1][j-1].first + a[i-1][j-1].first,
						a[i+k-1][j+k-1].second - a[i-1][j+k-1].second - a[i+k-1][j-1].second + a[i-1][j-1].second);
					pmp.first -= A[i][j].first + A[i][j+k-1].first + A[i+k-1][j].first + A[i+k-1][j+k-1].first;
					pmp.second -= A[i][j].second + A[i][j+k-1].second + A[i+k-1][j].second + A[i+k-1][j+k-1].second;
					ll mp = w[i+k-1][j+k-1] - w[i-1][j+k-1] - w[i+k-1][j-1] + w[i-1][j-1];
					mp -= W[i][j] + W[i][j+k-1] + W[i+k-1][j] + W[i+k-1][j+k-1];
					pii cmp = make_pair(c.first * mp, c.second * mp);
					if (pmp.first == cmp.first && pmp.second == cmp.second)
						ans = k;
				}
			}
		}
		printf("Case #%d: ", t+1);
		if (ans == 0)
			puts("IMPOSSIBLE");
		else
			printf("%d\n", ans);
	}
	return 0;
}