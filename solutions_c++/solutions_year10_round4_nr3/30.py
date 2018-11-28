#include <iostream>
#include <algorithm>

using namespace std;

int n;
int anc[1001];
int minix[1001], maxix[1001], miniy[1001], maxiy[1001];
int x1[1001], y1[1001], x2[1001], y2[1001];

int find(int u)
{
	if (anc[u] == 0)
		return u;
	else {
		anc[u] = find(anc[u]);
		return anc[u];
	}
}

void uni(int x, int y)
{
	int i = find(x), j = find(y);
	if (i != j) anc[i] = j;
	minix[j] = min(minix[j], minix[i]);
	maxix[j] = max(maxix[j], maxix[i]);
	miniy[j] = min(miniy[j], miniy[i]);
	maxiy[j] = max(maxiy[j], maxiy[i]);
}

int main (int argc, char * const argv[])
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int test;
	cin >> test;
	for (int tt = 1; tt <= test; tt++) {
		cin >> n;
		memset(anc, 0, sizeof(anc));
		for (int i = 1; i <= n ; i++) {
			cin >> x1[i] >> y1[i] >> x2[i] >> y2[i];
			minix[i] = x1[i];
			miniy[i] = y1[i];
			maxix[i] = x2[i];
			maxiy[i] = y2[i];
			for (int j = 1; j < i; j++) {
				if (!(x1[i] > x2[j] + 1) && !(x2[i] + 1 < x1[j]) && !(y1[i] > y2[j] + 1) && !(y2[i] + 1 < y1[j]) && !(x2[i] < x1[j] && y2[i] < y1[j]) && !(x1[i] > x2[j] && y1[i] > y2[j])) {
					uni(i, j);
				}
			}
		}
		int ans = 0;
		for (int i = 1; i <= n; i++) {
			//cout << maxix[i] << ' ' << minix[i] << endl;
			int a = maxix[i] + maxiy[i];
			if (find(i) == i) {
				int s = 2000000000;
				for (int j = 1; j <= n; j++)
					if (find(j) == i) {
						s = min(s, x1[j] + y1[j]);
					}
				ans = max(ans, a - s + 1);
			}
		}
		cout << "Case #" << tt << ": " << ans << endl;
	}
}
