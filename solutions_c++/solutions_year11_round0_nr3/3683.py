#include <iostream>
#include <string>

using namespace std;

int N;
int a[1000];

void solve() {
	cin >> N;
	for (int i = 0; i < N; i++) cin >> a[i];
	sort(a, a + N);
	int r = 0;
	int s = 0;
	for (int i = 0; i < N; i++) r ^= a[i], s += a[i];
	if (r) cout << "NO" << endl; else cout << s - a[0] << endl;
}

int main() {
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++) {
		cout << "Case #" << test << ": ";
		solve();
	}
	return 0;
}
