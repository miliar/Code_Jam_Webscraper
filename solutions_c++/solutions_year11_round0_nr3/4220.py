#include <iostream>
#include <cstdio>
#include <cmath>

using namespace std;

int i, n, m, j, mini, x, s, ans;

int main() {
	freopen("c.in", "r", stdin);
	freopen("c.cout", "w", stdout);

	cin >> n;
	for (i = 1; i <= n; ++i) {
		cin >> m;
		mini = 1000 * 1000 * 1000;
		s = 0;
		ans = 0;
		for (j = 1; j <= m; ++j) {
			cin >> x;
			s += x;
			mini = min(mini, x);
			ans ^= x;
		}
		cout << "Case #" << i << ":" << " ";
		if (ans == 0)
			cout << s - mini << endl;
		else 
			cout << "NO" << endl;
	}

}
