#include <iostream>
using namespace std;

void solve()
{
	int n;
	cin >> n;

	int x = 1, y = 1;
	int t1 = 0, t2 = 0;

	char c, last_c; int pos;
	cin >> c >> pos;
	last_c = c;
	if (c == 'B') {
		t1 += abs(x - pos) + 1;
		x = pos;
	} else {
		t2 += abs(y - pos) + 1;
		y = pos;
	}
	for(int i = 1; i < n; ++i) {
		cin >> c >> pos;
		if (c == last_c) {
			if (c == 'B') {
				t1 += abs(x - pos) + 1;
				x = pos;
			} else {
				t2 += abs(y - pos) + 1;
				y = pos;
			}
		} else {
			if (c == 'B') {
				t1 += abs(x - pos) + 1;
				x = pos;
				if (t1 <= t2)
					t1 = t2 + 1;
			} else {
				t2 += abs(y - pos) + 1;
				y = pos;
				if (t2 <= t1)
					t2 = t1 + 1;
			}
		}
		last_c = c;
	}
	cout << max(t1, t2) << '\n';
}

int main()
{
	freopen("in.txt", "rt", stdin);
	freopen("out.txt", "wt", stdout);
	int t; 
	cin >> t;
	for(int i = 0; i < t; ++i) {
		printf("Case #%d: ", i + 1);
		solve();
	}
	return (0);
}
