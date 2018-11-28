#include <iostream>
using namespace std;

int a[1001], b[1001], n, l, c, task;
long long t;

bool cmp(int i, int j)
{
	return a[i] > a[j];
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin >> task;
	for (int tt = 1; tt <= task; ++tt) {
		cout << "Case #" << tt << ": ";
		cin >> l >> t >> n >> c; t /= 2;
		memset(a, 0, sizeof(a));
		memset(b, 0, sizeof(b));
		
		int k = 0, now = 0, s = 0, m = n / c, x = n % c, w, R, cur = 0, y = 0;
		long long ans, pre = 0;
		for (int i = 0; i < c; ++i) {cin >> a[i]; s += a[i];}
		ans = s * 2; ans = ans * m;
		for (int i = 0; i < x; ++i) ans += 2 * a[i];
		
		if (ans <= t * 2) {cout << ans << endl; continue;}
		
		for (; now < m; ++now) 
			if (pre + s > t) break;
			else pre += s;
		
		if (now == m) {
			for (; k < x && pre + a[k] <= t; ++k) pre += a[k];
			y = k; w = 0; R = x - k;
		}
		else {
			for (; pre + a[k] <= t; ++k) pre += a[k];
			y = -1; w = m - now - 1; R = w * c + c - k + 1 + x;
		}
		
		for (int i = 0; i < c; ++i) b[i] = i;
		sort(b, b + c, cmp);
		if (l < R) R = l;
		
		while (R > 0) {
			long long o, p;
			if (pre + a[k] - t > a[b[cur]]) {
				o = 1; p = a[k] - t + pre; pre = t - a[k];
			}
			else {
				o = w + (b[cur] > k && now < m) + (b[cur] < x && b[cur] > y);
				p = a[b[cur]]; ++cur;
			}
			if (R < o) o = R; R -= o; ans -= o * p;
		}
		cout << ans << endl;
	}
	return 0;
}

