#include <iostream>
using namespace std;

const int maxn = 1010;

int tc, n;
int a[maxn];
int cnt[500];

int main() {
	cin >> tc;
	for (int tt = 1; tt <= tc; tt++) {
		cin >> n;
		memset(cnt, 0, sizeof(cnt));
		int maxp = 0;
		for (int i = 0; i < n; i++) {
			scanf("%d", a+i);
			// convert
			int b = a[i], pos = 0;
			while (b > 0) {
				if (b % 2)
					cnt[pos]++;
				b = b / 2;
				pos++;
				if (pos > maxp)
					maxp = pos;
			}
		}

		bool flag = true;
		for (int i = 0; i < maxp; i++)
			if (cnt[i] % 2) {
				flag = false;
				break;
			}
		if (!flag)
			printf("Case #%d: NO\n", tt);
		else {
			int ans = 0, mina = 10000000;
			for (int i = 0; i < n; i++) {
				ans += a[i];
				if (a[i] < mina)
					mina = a[i];
			}
			ans -= mina;
			printf("Case #%d: %d\n", tt, ans);
		}

	}
}
