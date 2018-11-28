#include <iostream>
using namespace std;

int a[500010];
int n;
int cnt[500010];

void process() {
	cin >> n;
	for (int i = 0; i < n; i++)
		cin >> a[i];

	int res = 1;
	cnt[0] = 1;
	for (int i = 1; i < n; i++) {
		cnt[i] = 1;
		for (int j = 0; j < i; j++)
			if (a[j] < a[i]) {
				cnt[i] += cnt[j];
				cnt[i] %= 1000000007;
			}
		res += cnt[i];
		res %= 1000000007;
	}
	cout << res << endl;
}

int main() {
	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		cout <<"Case #" <<i << ": ";
		process();
	}
}

