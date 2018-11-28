#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int test;
	cin >> test;
	for (int tt = 1; tt <= test; tt++) {
		cout << "Case #" << tt << ": ";
		int n;
		cin >> n;
		int f1 = 0, f2 = 0, p1 = 1, p2 = 1, ans = 0;
		for (int i = 0; i < n; i++) {
			char c;
			int x;
			cin >> c >> x;
			if (c == 'O') {
				f1 = max(ans + 1, f1 + (1 + abs(x - p1)));
				p1 = x;
				ans = max(f1, ans);
			} else {
				f2 = max(ans + 1, f2 + (1 + abs(x - p2)));
				p2 = x;
				ans = max(f2, ans);
			}
		}
		cout << ans << endl;
	}
}
