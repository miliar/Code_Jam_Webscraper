#include<cstdio>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;

int win(int i, int j)
{
	if (i >= 2*j)
		return 1;
	int k = win(j, i - j);
	return 1 - k;
}

int chk(int i, int j)
{
	if (i > j)
		return win(i, j);
	else
		return win(j, i);
}

int main()
{
	freopen("C-large.in", "r", stdin);
	freopen("output123.txt", "w", stdout);
	int kase, a1, a2, b1, b2;
	cin >> kase;
	for (int kk = 1; kk <= kase; kk++) {
		cout << "Case #" << kk << ": ";
		cin >> a1 >> a2 >> b1 >> b2;
		long long ans = 0;
		for (int a = a1; a <= a2; a++) {
			int l = 0, r = a, p;
			while (l + 1 < r) {
				int m = (l + r) / 2;
				if (chk(a, m) == 0)
					r = m;
				else
					l = m;
			}
			p = r;
			l = a, r = 2 * a + 5;
			while (l + 1 < r) {
				int m = (l + r) / 2;
				if (chk(a, m) == 0)
					l = m;
				else
					r = m;
			}
			r = l, l = p;
			l = max(l, b1);
			r = min(r, b2);
			ans += b2 - b1+1;
			if (r >= l)
				ans -= r - l + 1;
		}
		cout << ans << endl;
	}
}
