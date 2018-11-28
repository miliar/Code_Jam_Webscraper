#include <iostream>
#include <algorithm>

using namespace std;

int g[1001];
int nxt[1001];
long long sum[1001];
int que[1001];
int pre[1001];

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("C-large.out", "w", stdout);
	int testcases;
	cin >> testcases;
	for (int t = 0; t < testcases; t++) {
		int r, k, n;
		cin >> r >> k >> n;
		for (int i = 0; i < n; i++) cin >> g[i];
		for (int i = 0; i < n; i++) {
			sum[i] = g[i];
			nxt[i] = (i + 1) % n;
			for (int j = 1; j < n; j++) {
				if (sum[i] + g[(i + j) % n] <= k) {
					sum[i] += g[(i + j) % n];
					nxt[i] = (i + j + 1) % n;
				}
				else
					break;
			}
			pre[i] = 0;
		}
		int top = 1;
		int st;
		que[1] = 0;
		pre[0] = 1;
		while (true) {
			if (pre[nxt[que[top]]] == 0) {
				que[top + 1] = nxt[que[top]];
				top++;
				pre[que[top]] = top;
			} else {
				st = pre[nxt[que[top]]];
				break;
			}
		}
		long long ans = 0, tot = 0;
		for (int i = 1; i < min(r, st); i++) ans += sum[que[i]];
		if (r >= st) {
			r -= st - 1;
			for (int i = st; i <= top; i++) tot += sum[que[i]];
			ans += tot * (r / (top - st + 1));
			for (int i = 0; i < r % (top - st + 1); i++) ans += sum[que[st + i]];
		}
		cout << "Case #" << t + 1 << ": " << ans << endl;
	}
}