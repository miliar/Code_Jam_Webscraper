#include <iostream>

using namespace std;


int main() {
	freopen ("input.txt", "rt", stdin);
	freopen ("output.txt", "wt", stdout);

	int ts;
	cin >> ts;
	for (int tt=0; tt<ts; ++tt) {

		int ans = 0;
		int prev[2] = { 0 },
			pos[2] = { 0 };
		int cnt;
		cin >> cnt;
		for (int i=1; i<=cnt; ++i) {
			char who;  int npos;
			scanf (" %c %d", &who, &npos);
			--npos;
			int id = (who == 'O') ? 0 : 1;

			ans = prev[id] = max (prev[id] + abs (pos[id] - npos), ans) + 1;
			pos[id] = npos;
		}

		printf ("Case #%d: %d\n", tt+1, ans);

	}

}